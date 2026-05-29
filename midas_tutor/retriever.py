"""
MIDAS API 检索引擎
==================
从知识库中快速搜索和检索 API 接口。
支持：关键词搜索、按章节筛选、按参数名搜索、模糊匹配。
"""

import json
import re
from collections import defaultdict


class APIRetriever:
    """API 检索器 —— 从知识库中找到你需要的接口。"""

    # 中英文关键词映射（帮助中文搜索匹配英文 API）
    CN_EN_MAP = {
        # ── 结构构件 ──
        "节点": "node nodal NODE",
        "梁单元": "beam element BEM BEAM ELEM frame",
        "梁": "beam BEM girder frame",
        "柱单元": "column COLUMN pier",
        "柱": "column COLUMN pier",
        "板单元": "plate slab PLATE wall",
        "板": "plate slab PLATE",
        "墙": "wall WALL plate",
        "桁架": "truss TRUSS",
        "索": "cable tendon CABLE",
        "实体单元": "solid SOLID",
        "单元": "element elem ELEM",
        "弹簧": "spring SPRING NSPR ESPR SSPS",

        # ── 项目与单位 ──
        "单位系统": "unit UNIT",
        "项目": "project new PJCF",
        # ── 材料与截面 ──
        "材料": "material matl MATL",
        "截面": "section sect SECT",
        "特性": "property PROP SECTPROP",

        # ── 荷载相关 ──
        "节点荷载": "nodal load CNLD CONL NODAL",
        "梁单元荷载": "beam load BMLD BEAM",
        "压力荷载": "pressure load PRES PSLT",
        "自重": "self-weight DEAD SELFWEIGHT gravity",
        "温度荷载": "temperature TEMP thermal BTMP",
        "预应力": "prestress TENDON TDNT",
        "移动荷载": "moving load MVLD MVHL traffic lane",
        "沉降": "settlement SETTLE SMST",
        "地震": "seismic earthquake response spectrum RESP SPECTRUM SPLC POSL",
        "风荷载": "wind load WIND",
        "施加荷载": "load apply LOAD CNLD BMLD PRES PSLT nodal beam pressure",
        "荷载工况": "load case LC LCNAME BODF",
        "荷载组合": "load combination COMB COMBINATION LCOM LCBN COMBW",
        "荷载": "load LOAD pressure",

        # ── 边界条件 ──
        "约束": "constraint support CONS boundary restraint",
        "边界条件": "boundary condition CONS support restraint BNGR",
        "边界": "boundary BNGR CONS support",
        "支座": "support CONS restraint bearing",
        "固结": "fixed support CONS",
        "铰接": "hinge release",

        # ── 内力与结果 ──
        "梁单元内力": "beam force BEAMFORCE FORCE beam result",
        "内力": "force FORCE result BEAMFORCE TRUSSFORCE",
        "应力": "stress STRESS",
        "弯矩": "moment MOMENT bending",
        "剪力": "shear SHEAR",
        "轴力": "axial AXIAL",
        "反力": "reaction REACTION",
        "位移": "displacement DISPLACE DISPLACEMENT",
        "变形": "deformation DEFORM",
        "振型": "mode shape MODE EIGEN eigenvalue",
        "周期": "period PERIOD",

        # ── 分析 ──
        "分析": "analysis ANAL ANALY",
        "模态分析": "modal eigenvalue EIGEN MODE",
        "屈曲分析": "buckling BUCKLING BUCKLE",
        "时程分析": "time history THIS TH",
        "反应谱": "response spectrum RESP SPECTRUM",
        "静力分析": "static analysis linear",
        "非线性": "nonlinear NLCT",
        "施工阶段": "construction stage STAGE CS STCT",
        "推覆": "pushover PUSHOVER",

        # ── 结果提取 ──
        "提取位移": "displacement result DISPLACE DISPLACEMENT",
        "提取内力": "force result BEAMFORCE FORCE TRUSSFORCE",
        "提取应力": "stress result STRESS",
        "提取反力": "reaction result REACTION",
        "提取结果": "result extract table RESULT",
        "结果": "result RESULT output extract",
        "表格": "table TABLE tabular",
        "后处理": "post POST result extract",

        # ── 创建与建模 ──
        "创建节点": "create node NODE new",
        "创建单元": "create element ELEM BEM TRUSS",
        "创建材料": "create material MATL",
        "创建截面": "create section SECT",
        "创建": "create new CREATE NEW add make",
        "定义": "define set create assign",
        "批量": "batch multiple loop assign",

        # ── 项目操作 ──
        "新建项目": "new project PJCF",
        "打开项目": "open project OPEN",
        "保存项目": "save project SAVE SAVEAS",
        "关闭项目": "close project CLOSE",
        "项目": "project PROJECT PJCF",

        # ── 网格 ──
        "网格划分": "mesh automesh divide DIVIDEELEM",
        "网格": "mesh automesh DIVIDEELEM divide",
        "划分": "divide mesh DIVIDEELEM automesh",

        # ── 视图与显示 ──
        "截图": "capture CAPTURE screenshot",
        "选择": "select SELECT",
        "显示": "display DISPLAY view show",
        "隐藏": "hide HIDE invisible",
        "视图": "view display",

        # ── 操作 ──
        "修改": "modify update PUT change edit",
        "删除": "delete DELETE remove clear",
        "查询": "query get GET retrieve info status",
        "获取": "get retrieve GET fetch",
        "导出": "export EXPORT save output",
        "导入": "import IMPORT load",
        "保存": "save SAVE SAVEAS",
        "打开": "open OPEN",
        "关闭": "close CLOSE",

        # ── 桥梁专用 ──
        "主梁": "girder main beam",
        "桥墩": "pier column",
        "桥台": "abutment",
        "桥面": "deck bridge",
        "拉索": "cable tendon stay",
        "钢束": "tendon prestress TDNT",
        "车道": "lane MVLD traffic",

        # ── 截面形状 ──
        "矩形": "RECT rectangular rectangle",
        "矩形截面": "RECT rectangular SECT section DBUSER shape",
        "圆形": "CIRC circular circle round",
        "圆形截面": "CIRC circular SECT section shape",
        "H型钢": "H-Section H-Beam steel shape SECT",
        "H型截面": "H-Section H-Beam SECT shape",
        "钢管": "PIPE tube hollow steel",
        "钢管截面": "PIPE tube steel SECT shape",
        "箱型": "BOX box rectangular hollow",
        "箱型截面": "BOX box SECT shape section",
        "角钢": "ANGLE steel angle L-Section",
        "槽钢": "CHANNEL C channel",
        "工字钢": "H-Section I-beam steel shape",
        "T型钢": "T-Section steel shape",
        "组合截面": "COMBINED composite SECT section",
        "圆管": "PIPE tube round CIRC circular",
        "方管": "BOX square tube rectangular",
        "截面形状": "SHAPE SECT section shape type DBUSER",
        "定义截面": "SECT DBUSER SHAPE define create section",

        # ── 单元类型 ──
        "梁单元": "BEAM beam element ELEM TYPE",
        "桁架单元": "TRUSS truss element ELEM TYPE",
        "索单元": "CABLE cable TENSTR element TYPE",
        "板单元": "PLATE plate element ELEM TYPE",
        "平面应力": "PLSTRS plane stress element TYPE",
        "平面应变": "PLSTRN plane strain element TYPE",
        "实体单元": "SOLID solid element ELEM TYPE",
        "只受拉": "TENSTR tension only element TYPE",
        "只受压": "COMPTR compression only element TYPE",
        "墙单元": "WALL wall element TYPE",
        "单元类型": "TYPE ELEM element type BEAM TRUSS",
        "创建单元": "ELEM element create TYPE BEAM",

        # ── 其他 ──
        "水化热": "hydration heat HHYD HHCT",
        "质量": "mass MASS weight",
        "重量": "weight mass MASS",
        "组": "group GRUP GRUPNAME",
        "分组": "group GRUP",
        "单位": "unit UNIT",
        "结构类型": "structure type STYP",
        "坐标系": "coordinate system COOR",
        "桩": "pile PILING",
        "土": "soil ground",
        "地基": "foundation ground soil",
        "设计": "design DESIGN",
        "组合": "combination COMB COMBINATION",
        "静力荷载工况": "static load cases STLD",
        "静力荷载": "static load STLD",
        "命名平面": "named plane NPLN",
        "释放": "release FRLS PRLS",
        "梁端释放": "beam end release FRLS",
        "弹性连接": "elastic link ELNK",
        "刚性连接": "rigid link RIGD",
        "一般连接": "general link NLNK NLLP",
        "塑性材料": "plastic material EPMT",
        "纤维": "fiber FIBR FIMP",
        "阻尼": "damping GRDP",
        "阻尼器": "damper SDVI SDVE SDST",
        "隔震": "isolator SDHY SDIS",
        "主控数据": "main control ACTL",
        "特征值": "eigenvalue EIGV eigen",
        "影响面": "influence surface SINF",
        "并发": "concurrent CRGR CJFG",
        "冲击系数": "impact factor IMPF",
        "动力系数": "dynamic factor DYFG DYNF",
        "地面加速度": "ground acceleration THGA",
        "多点激励": "multiple support THMS",
        "徐变": "creep CRPC TDMT",
        "收缩": "shrinkage TDMT",
        "预拱度": "camber CMCS CAMB",
        "管道冷却": "pipe cooling HPCE",
        "热源": "heat source HSFC HAHS",
        "对流": "convection CCFC HECB",
        "水化": "hydration HHCT HHYD",
        "回退": "setback STBK",
        "波浪": "wave WVLD",
        "忽略": "ignore IELC IEPI",
        "初始力": "initial force INMF IFGS EFCT",
        "长细比": "slenderness LTSR",
        "配筋": "rebar RCHK reinforcement RPSC",
        "地下": "underground ULCT",
        "楼面": "floor FBLA FBLD",
        "楼板": "floor FBLA FBLD diaphragm DRLS",
        "装饰": "finishing FMLD",
        "土压力": "earth pressure EPST POSP",
        "先张拉": "pretension PTNS EXLD",
        "钢束": "tendon TDNT TDNA TDPL TDCS",
        "车道": "lane LLAN SLAN MVLD",
        "车辆": "vehicle MVHL MVHC",
        "铁路": "railway DYFG DYNF",
        "等级": "class MVHC",
        "标志": "mark WMAK",
        "平面": "plane NPLN PNLD PNLA",
        "温度梯度": "temperature gradient GTMP",
        "系统温度": "system temperature STMP",
        "节点温度": "nodal temperature NTMP",
        "截面温度": "beam section temperature BTMP",
        "单元温度": "element temperature ETMP",
        "环境温度": "ambient temperature ETFC",
        "节点质量": "nodal mass NMAS",
        "质量转换": "load to mass LTOM",
        "体力": "body force NBOF",
        "指定位移": "specified displacement SDSP",
        "偏移": "offset OFFS",
        "节点区": "panel zone PZEF",
        "约束方向": "constraint direction CLDR",
        "线性约束": "linear constraint MCON",
        "跨度": "span SPAN",
        "楼层": "story STOR",
        "颜色": "color CO_M CO_S CO_T CO_F",
        "局部轴": "local axis SKEW",
        "域": "domain MADO SBDO DOEL",
        "子域": "subdomain SBDO",
        "有效宽度": "effective width EWSF",
        "刚度": "stiffness SECF ESSF",
        "比例系数": "scale factor PSSF EWSF ESSF",
        "虚拟梁": "virtual beam VBEM",
        "虚拟截面": "virtual section VSEC",
        "铰": "hinge IEHC IEHG PHGE",
        "滞回": "hysteretic SDHY",
        "粘滞": "viscous SDVI",
        "粘弹性": "viscoelastic SDVE",
        "钢阻尼": "steel damper SDST",
        "力-变形": "force deformation MLFC",
        "时变": "time dependent TDMF TDMT TDME TMAT",
        "抗压强度": "compressive strength TDME",
        "非弹性": "inelastic IMFM IEHC IEHG FIMP",
        "时变荷载": "time varying THSL",
        "加载顺序": "load sequence LDSQ",
        "预组合": "pre composite PLCB",
        "几何刚度": "geometric stiffness IFGS",
        "大位移": "large displacement IFGS",
        "小位移": "small displacement EFCT INMF",
        "梁格": "girder GSBG",
        "截面线": "cutting line CUTL CLWP",
        "未知荷载系数": "unknown load factor ULFC",
        "时程图表": "time history graph THRE THRG THRI THRS",
        "桩土": "pile soil POSP",
        "长度": "length LENG",
        "框架": "frame DCTL",
        "构件": "member MEMB MBTP",
        "变截面": "tapered TSGR",
        "端点": "end FRLS PRLS OFFS",
    }

    # 路径→中文名称 直接映射表
    PATH_TO_CN_NAME = {
        # ── 项目操作 DOC ──
        "/doc/NEW": "新建项目",
        "/doc/OPEN": "打开项目",
        "/doc/CLOSE": "关闭项目",
        "/doc/SAVE": "保存项目",
        "/doc/SAVEAS": "另存项目",
        "/doc/STAGAS": "保存当前阶段为",
        "/doc/IMPORT": "导入JSON",
        "/doc/IMPORTMXT": "导入MCT/MGT",
        "/doc/EXPORT": "导出JSON",
        "/doc/EXPORTMXT": "导出MCT/MGT",
        "/doc/ANAL": "运行分析",

        # ── 项目信息 DB ──
        "/db/PJCF": "项目信息",
        "/db/UNIT": "单位系统",
        "/db/STYP": "结构类型",
        "/db/STYP-M1ᴴˢ⁾": "结构类型(变温)",
        "/db/GRUP": "结构组",
        "/db/BNGR": "边界组",
        "/db/LDGR": "荷载组",
        "/db/TDGR": "钢束组",
        "/db/NPLN": "命名平面",
        "/db/CO_M": "材料颜色",
        "/db/CO_S": "截面颜色",
        "/db/CO_T": "厚度颜色",
        "/db/CO_F": "楼面荷载颜色",
        "/db/SPAN": "跨度信息",
        "/db/STOR": "楼层数据",

        # ── 节点与单元 ──
        "/db/NODE": "节点",
        "/db/ELEM": "单元",
        "/db/SKEW": "节点局部轴",
        "/db/MADO": "定义域",
        "/db/SBDO": "定义子域",
        "/db/DOEL": "域-单元",

        # ── 材料 ──
        "/db/MATL": "材料属性",
        "/db/MATL-M1ᴴˢ⁾": "材料属性(变温)",
        "/db/IMFM": "纤维模型非弹性材料",
        "/db/IMFM-M1ᴴˢ⁾": "非弹性材料自动生成连接",
        "/db/TDMF": "用户定义时变材料",
        "/db/TDMT": "徐变/收缩时变材料",
        "/db/TDME": "抗压强度时变材料",
        "/db/EDMP": "修改属性",
        "/db/TMAT": "时变材料连接",
        "/db/EPMT": "塑性材料",
        "/db/EPMT-M1ᴴˢ⁾": "塑性材料(变温)",

        # ── 截面与厚度 ──
        "/db/SECT": "截面属性",
        "/db/THIK": "厚度值",
        "/db/TSGR": "变截面组",
        "/db/SECF": "截面刚度",
        "/db/RPSC": "截面配筋",
        "/db/STRPSSM": "截面应力点",
        "/db/PSSF": "板刚度比例系数",
        "/db/VBEM": "虚拟梁截面",
        "/db/VSEC": "虚拟截面",
        "/db/EWSF": "有效宽度比例系数",

        # ── 非弹性铰 ──
        "/db/IEHC": "非弹性铰控制数据",
        "/db/IEHG": "分配非弹性铰属性",
        "/db/IEHG-BEAM-M1ᴴˢ⁾": "分配非弹性铰-梁",
        "/db/IEHG-TRUSS-M1ᴴˢ⁾": "分配非弹性铰-桁架",
        "/db/IEHG-GL-M1ᴴˢ⁾": "分配非弹性铰-一般连接",
        "/db/IEHG-PSS-M1ᴴˢ⁾": "分配非弹性铰-点弹簧",
        "/db/FIMP": "非弹性材料属性",
        "/db/FIBR": "截面纤维划分",
        "/db/GRDP": "组阻尼",
        "/db/ESSF": "单元刚度比例系数",

        # ── 边界条件 ──
        "/db/CONS": "约束/支座",
        "/db/NSPR": "点弹簧",
        "/db/GSTP": "一般弹簧类型",
        "/db/GSPR": "一般弹簧支承",
        "/db/SSPS": "面弹簧",
        "/db/ELNK": "弹性连接",
        "/db/RIGD": "刚性连接",
        "/db/NLLP": "一般连接属性",
        "/db/NLNK": "一般连接",
        "/db/NLNK-M1ᴴˢ⁾": "一般连接(变温)",
        "/db/CGLP": "修改一般连接属性",
        "/db/FRLS": "梁端释放",
        "/db/OFFS": "梁端偏移",
        "/db/PRLS": "板端释放",
        "/db/MCON": "线性约束",
        "/db/PZEF": "节点区效应",
        "/db/CLDR": "定义约束方向",
        "/db/DRLS": "楼板断开",

        # ── 抗震装置 ──
        "/db/MLFC": "力-变形函数",
        "/db/SDVI": "粘滞阻尼器",
        "/db/SDVE": "粘弹性阻尼器",
        "/db/SDST": "钢阻尼器",
        "/db/SDHY": "滞回隔震器(MSS)",
        "/db/SDIS": "隔震器(MSS)",

        # ── 静力荷载 ──
        "/db/STLD": "静力荷载工况",
        "/db/BODF": "自重",
        "/db/CNLD": "节点荷载",
        "/db/BMLD": "梁单元荷载",
        "/db/SDSP": "指定支承位移",
        "/db/NMAS": "节点质量",
        "/db/LTOM": "荷载转为质量",
        "/db/NBOF": "节点体力",

        # ── 压力/平面/楼面荷载 ──
        "/db/PSLT": "压力荷载类型",
        "/db/PRES": "分配压力荷载",
        "/db/PNLD": "平面荷载类型",
        "/db/PNLA": "分配平面荷载",
        "/db/FBLD": "楼面荷载类型",
        "/db/FBLA": "分配楼面荷载",
        "/db/FMLD": "装饰材料荷载",
        "/db/POSP": "土压力参数",
        "/db/EPST": "静止土压力",
        "/db/POSL": "地震荷载参数",

        # ── 温度荷载 ──
        "/db/ETMP": "单元温度",
        "/db/GTMP": "温度梯度",
        "/db/BTMP": "梁截面温度",
        "/db/STMP": "系统温度",
        "/db/NTMP": "节点温度",

        # ── 预应力/钢束 ──
        "/db/TDNT": "钢束属性",
        "/db/TDNA": "钢束线型",
        "/db/TDCS": "组合截面钢束位置",
        "/db/TDPL": "钢束预应力",
        "/db/PRST": "预应力梁荷载",
        "/db/PTNS": "先张拉荷载",
        "/db/EXLD": "先张拉外部荷载工况",

        # ── 移动荷载 ──
        "/db/MVCD": "移动荷载规范",
        "/db/LLAN": "车道线",
        "/db/LLANch": "车道线-中国",
        "/db/LLANid": "车道线-印度",
        "/db/LLANtr": "车道线-横向",
        "/db/LLANop": "车道线-优化",
        "/db/SLAN": "车道面",
        "/db/SLANch": "车道面-中国",
        "/db/SLANop": "车道面-优化",
        "/db/MVHL": "车辆-AASHTO标准",
        "/db/MVHLtr": "车辆-横向",
        "/db/MVLD": "移动荷载工况",
        "/db/MVLDch": "移动荷载工况-中国",
        "/db/MVLDid": "移动荷载工况-印度",
        "/db/MVLDbs": "移动荷载工况-BS",
        "/db/MVLDeu": "移动荷载工况-欧规",
        "/db/MVLDpl": "移动荷载工况-波兰",
        "/db/MVLDtr": "移动荷载工况-横向",
        "/db/CRGR": "并发反力组",
        "/db/CJFG": "并发节点力组",
        "/db/MVHC": "车辆等级",
        "/db/SINF": "影响面板单元",
        "/db/MLSP": "车道支承-负弯矩",
        "/db/MLSR": "车道支承-反力",
        "/db/DYLA": "动力荷载容许值",
        "/db/IMPF": "附加冲击系数",
        "/db/DYFG": "铁路动力系数",
        "/db/DYNF": "铁路单元动力系数",

        # ── 反应谱 ──
        "/db/SPFC": "反应谱函数",
        "/db/SPLC": "反应谱荷载工况",

        # ── 时程分析 ──
        "/db/THGC": "时程全局控制",
        "/db/THGC-M1ᴴˢ⁾": "时程全局控制(变温)",
        "/db/THOO-M1ᴴˢ⁾": "时程输出选项",
        "/db/THIS": "时程荷载工况",
        "/db/THIS-M1ᴴˢ⁾": "时程荷载工况(变温)",
        "/db/THFC": "时程函数",
        "/db/THGA": "地面加速度",
        "/db/THNL": "动力节点荷载",
        "/db/THSL": "时变静力荷载",
        "/db/THMS": "多点支承激励",

        # ── 施工阶段 ──
        "/db/STAG": "施工阶段定义",
        "/db/CSCS": "施工阶段组合截面",
        "/db/TMLD": "施工阶段时间荷载",
        "/db/STBK": "非线性施工阶段回退荷载",
        "/db/CMCS": "施工阶段预拱度",
        "/db/CRPC": "施工阶段徐变系数",

        # ── 水化热 ──
        "/db/ETFC": "环境温度函数",
        "/db/CCFC": "对流系数函数",
        "/db/HECB": "单元对流边界",
        "/db/HSPT": "指定温度",
        "/db/HSFC": "热源函数",
        "/db/HAHS": "分配热源",
        "/db/HPCE": "管道冷却",
        "/db/HSTG": "水化热施工阶段",

        # ── 沉降 ──
        "/db/SMPT": "沉降组",
        "/db/SMLC": "沉降荷载工况",

        # ── 其他荷载 ──
        "/db/PLCB": "预组合截面",
        "/db/LDSQ": "非线性加载顺序",
        "/db/WVLD": "波浪荷载",
        "/db/IELC": "忽略荷载工况单元",
        "/db/IFGS": "大位移初始力-几何刚度",
        "/db/EFCT": "小位移初始力控制数据",
        "/db/INMF": "小位移初始单元力",
        "/db/GALDᴶ⁾": "网格分析荷载",

        # ── 分析控制 ──
        "/db/ACTL": "主控数据",
        "/db/ACTL-M1ᴴˢ⁾": "主控数据(变温)",
        "/db/PDEL": "P-Delta分析控制",
        "/db/BUCK": "屈曲分析控制",
        "/db/EIGV": "特征值分析控制",
        "/db/EIGV-M1ᴴˢ⁾": "特征值分析控制(变温)",
        "/db/HHCT": "水化热分析控制",
        "/db/HHCT-M1ᴴˢ⁾": "水化热分析控制(变温)",
        "/db/MVCT": "移动荷载分析控制",
        "/db/MVCTch": "移动荷载分析控制-中国",
        "/db/MVCTid": "移动荷载分析控制-印度",
        "/db/MVCTbs": "移动荷载分析控制-BS",
        "/db/MVCTtr": "移动荷载分析控制-横向",
        "/db/SMCT": "沉降分析控制",
        "/db/NLCT": "非线性分析控制",
        "/db/NLCT-M1ᴴˢ⁾": "非线性分析控制(变温)",
        "/db/STCT": "施工阶段分析控制",
        "/db/STCT-M1ᴴˢ⁾": "施工阶段分析控制(变温)",
        "/db/BCCT": "边界条件变化分配",
        "/db/BCGD-M1ᴴˢ⁾": "定义边界组合",
        "/db/BCGA-M1ᴴˢ⁾": "分配边界组合",

        # ── 荷载组合 ──
        "/db/LCOM-GEN": "荷载组合-一般",
        "/db/LCOM-CONC": "荷载组合-混凝土设计",
        "/db/LCOM-STEEL": "荷载组合-钢结构设计",
        "/db/LCOM-SRC": "荷载组合-SRC设计",
        "/db/LCOM-STLCOMP": "荷载组合-组合梁设计",
        "/db/LCOM-SEISMIC": "荷载组合-抗震设计",

        # ── 桥梁 ──
        "/db/CUTL": "截面线",
        "/db/CLWP": "板截面线图",
        "/db/GSBG": "桥梁梁格图",
        "/db/GCMB": "一般预拱度控制",
        "/db/CAMB": "FCM预拱度控制",
        "/db/ULFC": "未知荷载系数约束",

        # ── 时程图表 ──
        "/db/THRE": "时程图表-单元力",
        "/db/THRG": "时程图表-一般连接",
        "/db/THRI": "时程图表-非弹性铰",
        "/db/THRS": "时程图表-抗震装置",
        "/db/HHND": "水化热结果图表",

        # ── 推覆分析 ──
        "/db/POGD": "推覆分析控制数据",
        "/db/POGD-M1ᴴˢ⁾": "推覆全局控制(变温)",
        "/db/IEPI": "推覆初始荷载忽略单元",
        "/db/PHGE": "分配推覆铰属性",
        "/db/POLC": "推覆荷载工况",
        "/db/POLC-M1ᴴˢ⁾": "推覆荷载工况(变温)",

        # ── 设计 ──
        "/db/DCON": "RC设计规范",
        "/db/MATD": "修改混凝土材料",
        "/db/RCHK": "梁柱配筋检查",
        "/db/LENG": "无支撑长度",
        "/db/MEMB": "构件分配",
        "/db/DCTL": "框架定义",
        "/db/LTSR": "限制长细比",
        "/db/ULCT": "地下荷载组合类型",
        "/db/MBTP": "修改构件类型",
        "/db/WMAK": "修改墙标记设计",
        "/db/DSTL": "钢结构设计规范",

        # ── OPE 操作 ──
        "/ope/PROJECTSTATUS": "项目状态",
        "/ope/DIVIDEELEM": "划分单元",
        "/ope/SECTPROP": "截面特性计算结果",
        "/ope/USLC": "使用荷载组合",
        "/ope/LINEBMLD": "线梁荷载",
        "/ope/AUTOMESH": "自动网格划分",
        "/ope/SSPS": "面弹簧",
        "/ope/EDMP": "修改属性",
        "/ope/STOR": "楼层计算",
        "/ope/STORY_PARAM": "楼层检查参数",
        "/ope/STORY_IRR_PARAM": "楼层不规则检查参数",
        "/ope/STORPROP": "楼层属性",
        "/ope/MEMB": "构件分配",

        # ── POST 分析结果 ──
        "Element Weight": "单元重量表格",
        "Nodal Body Force": "节点体力表格",
        "Mass Summary": "质量汇总表格",
        "Load Summary": "荷载汇总表格",
        "Material": "材料表格",
        "Section": "截面表格",
        "Restraint Supports": "约束支承表格",
        "Story Mass Summary": "楼层质量汇总",
        "Story Load Summary": "楼层荷载汇总",
        "Story Weight": "楼层重量",
        "Reaction-LocalReaction-GlobalReaction-Local-Surface Spring": "反力-分析结果表格",
        "Displacement-LocalDisplacement-Global": "位移-分析结果表格",
        "Truss Force - Analysis Result Table": "桁架内力-分析结果表格",
        "Cable Force - Analysis Result Table": "索力-分析结果表格",
        "Beam Force - Analysis Result Table": "梁内力-分析结果表格",
        "Plate Force-Local": "板内力(局部)-分析结果表格",
        "Plane Stress Force-Local": "平面应力内力(局部)-分析结果表格",
        "Plane Strain Force-Local": "平面应变内力(局部)-分析结果表格",
        "Axisymmetric Force-Local": "轴对称内力(局部)-分析结果表格",
        "Solid Force-Local": "实体内力(局部)-分析结果表格",
        "Elastic LinkView by Max Value Item": "弹性连接-分析结果表格",
        "General Link ForceGeneral Link Force-View by Max Value ItemGeneral Link Deformation": "一般连接-分析结果表格",
        "Resultant ForceResultant Force-View by Max Value Item": "合力-分析结果表格",
        "Vibartion Mode-EigenvalueVibartion Mode-Participation Vector": "振型-分析结果表格",
        "Buckling Mode": "屈曲模态-分析结果表格",
        "Effective Span Length-TrussEffective Span Length-BeamEffective Span Length-Plate": "有效跨度长度-分析结果表格",
        "Nodal Results of RS-Inertia ForceNodal Results of RS-Acceleration": "反应谱节点结果-分析结果表格",
        "Tendon Coordinates": "钢束坐标-分析结果表格",
        "Composite Section for C.S. ForceComposite Section for C.S. Stress": "施工阶段组合截面(内力与应力)-分析结果表格",
        "Element Properties at Each Stage": "各阶段单元属性-分析结果表格",
        "Lack of Fit Force-Truss": "桁架安装误差力-分析结果表格",
        "Equilibrium Element Nodal Force": "平衡单元节点力-分析结果表格",
        "Initial Element Force": "初始单元力-分析结果表格",
        "Wall Force/Moment": "墙内力/弯矩-分析结果表格",
        "Story Drift (X,Y,Combined)": "层间位移角(X,Y,组合)-楼层结果表格",
        "Story Displacement (X,Y,Combined)": "楼层位移(X,Y,组合)-楼层结果表格",
        "Story Shear(R.S Analysis) - Story Shear(for R.S)Story Shear(R.S.Analysis) - Story Shear Force Coefficient": "楼层剪力(反应谱)-楼层结果表格",
        "Story Mode Shape": "楼层振型-楼层结果表格",
        "Story Shear Force Ratio": "楼层剪力比-楼层结果表格",
        "Story Eccentricity": "楼层偏心-楼层结果表格",
        "Overturning Moment": "倾覆弯矩-楼层结果表格",
        "Story Axial Force Sum": "楼层轴力合计-楼层结果表格",
        "Story Stability Coefficient": "楼层稳定系数-楼层结果表格",
        "Torsional Irregularity Check": "扭转不规则检查-楼层结果表格",
        "Torsional Amplification Factor": "扭转放大系数-楼层结果表格",
        "Stiffness Irregularity Check (Soft Story)": "刚度不规则检查(软弱层)-楼层结果表格",
        "Capacity Irregularity Check(Weak Story)": "承载力不规则检查(薄弱层)-楼层结果表格",
        "Criteria for Regularity in Plan": "平面规则性准则-楼层结果表格",
        "Ultimate Story Shear For Check": "极限楼层剪力检查-楼层结果表格",
        "DisplacementVelocityAbsolute AccelerationRelative Acceleration": "位移/速度/加速度-时程结果表格",
        "Beam Force": "梁内力-时程结果表格",
        "Truss Force": "桁架内力-时程结果表格",
        "General Link ForceDeformation": "一般连接-时程结果表格",
        "Event Time-LumpedEvent Time-DistributedEvent Time-WallEvent Time-TrussEvent Time-Spring": "非弹性铰事件时间-时程结果表格",
        "Beam Summary-DXBeam Summary-DYBeam Summary-DZBeam Summary-RYBeam Summary-RZ": "非弹性铰梁摘要-时程结果表格",
        "Truss Summary-DX": "非弹性铰桁架摘要-时程结果表格",
        "General Link Summary-DXGeneral Link Summary-DYGeneral Link Summary-DZGeneral Link Summary-RXGeneral Link Summary-RYGeneral Link Summary-RZ": "非弹性铰一般连接摘要-时程结果表格",
        "Force-LumpedForce-DistributedForce-WallForce-TrussForce-Spring": "非弹性铰内力-时程结果表格",
        "Deformation-LumpedDeformation-DistributedDeformation-WallDeformation-TrussDeformation-Spring": "非弹性铰变形-时程结果表格",
        "Element Rotation-BeamElement Rotation-Wall": "非弹性铰单元转动-时程结果表格",
        "Ductility Factor(D/D1)-LumpedDuctility Factor(D/D1)-DistributedDuctility Factor(D/D1)-WallDuctility Factor(D/D1)-TrussDuctility Factor(D/D1)-Spring": "延性系数(D/D1)-时程结果表格",
        "Ductility Factor(D/D2)-LumpedDuctility Factor(D/D2)-DistributedDuctility Factor(D/D2)-WallDuctility Factor(D/D2)-TrussDuctility Factor(D/D2)-Spring": "延性系数(D/D2)-时程结果表格",
        "Estimate Yield Strength": "纤维截面估算屈服强度-时程结果表格",
        "Elastic Modulus Retention Rateᴶ⁾": "纤维截面弹性模量保留率-时程结果表格",
        "Maximum Strain of The Cellᴶ⁾": "纤维截面单元最大应变-时程结果表格",
        "Event Stepᴶ⁾": "纤维截面事件步-时程结果表格",
        "Average Compression Strainᴶ⁾": "纤维截面平均压缩应变-时程结果表格",
        "Stress-LocalStress-Global": "应力-水化热结果表格",
        "Temperature": "温度-水化热结果表格",
        "Displacement": "位移-水化热结果表格",
        "Tensile Stress": "拉应力-水化热结果表格",
        "Pipe Cooling Nodal Temperature": "管道冷却节点温度-水化热结果表格",
        "Node Results": "时程文本-节点结果",
        "Element Result(Truss, Beam, Plane Stress/Strain, Solid)": "时程文本-单元结果(桁架/梁/平面应力应变/实体)",
        "Element Result(Plate)": "时程文本-单元结果(板)",
        "Element Result(Wall)": "时程文本-单元结果(墙)",
        "General Link Result": "时程文本-一般连接结果",
        "Displacement Result": "推覆文本-位移结果",
        "Element Result(Beam, Truss)": "推覆文本-单元结果(梁/桁架)",
        "Element Result(Wall)": "推覆文本-单元结果(墙)",
        "General Link Result": "推覆文本-一般连接结果",
        "Elastic Link Result": "推覆文本-弹性连接结果",
        "/post/PM": "P-M交互图",
        "/post/STEELCODECHECK": "钢结构验算",
        "/post/BEAMDESIGNFORCES": "混凝土设计-梁设计内力",
        "/post/COLUMNDESIGNFORCES": "混凝土设计-柱设计内力",
        "/post/BRACEDESIGNFORCES": "混凝土设计-支撑设计内力",
        "/post/WALLDESIGNFORCES": "混凝土设计-墙设计内力",
        "/post/STEELMEMBERDESIGNFORCES": "钢结构设计-钢构件设计内力",
        "/post/SRCBEAMDESIGNFORCES": "SRC设计-SRC梁设计内力",
        "/post/SRCCOLUMNDESIGNFORCES SRC": "SRC设计-SRC柱设计内力",
        "/post/COLDFORMEDSTEELMEMBERDESIGNFORCES": "冷弯设计-冷弯钢构件设计内力",

        # ── VIEW 视图 ──
        "/view/SELECT": "选择对象",
        "/view/CAPTURE": "截图",
        "/view/PRECAPTURE": "对话框截图",
        "/view/ANGLE": "视角设置",
        "/view/ACTIVE": "激活窗口",
        "/view/DISPLAY": "显示控制",
        "/view/RESULTGRAPHIC": "结果显示类型",
    }

    def __init__(self, kb_path="midas_api_knowledge_base.json"):
        self.kb_path = kb_path
        self.kb = None
        self.endpoints = []          # 扁平化的所有端点
        self.search_index = []       # 每条记录的搜索文本
        self.section_counts = {}     # 每个章节的接口数
        self._load()

    def _load(self):
        """加载知识库并构建搜索索引。"""
        with open(self.kb_path, "r", encoding="utf-8") as f:
            self.kb = json.load(f)

        api_data = self.kb.get("api_data", {})
        self.endpoints = []
        self.search_index = []

        def walk(data, section, subsection=""):
            if not isinstance(data, dict):
                return
            for key, value in data.get("endpoints", {}).items():
                if isinstance(value, dict) and "api_name" in value:
                    self._add_endpoint(value, section, subsection, key)
            for key, value in data.get("subsections", {}).items():
                walk(value, section, key)
            for key, value in data.items():
                if key in ("endpoints", "subsections"):
                    continue
                if isinstance(value, dict) and "api_name" in value:
                    self._add_endpoint(value, section, subsection, key)

        for sec_name, sec_data in api_data.items():
            walk(sec_data, sec_name)

        # 统计
        self.section_counts = defaultdict(int)
        for ep in self.endpoints:
            self.section_counts[ep["section"]] += 1

    def _add_endpoint(self, data, section, subsection, path):
        """添加一个端点并构建搜索文本。"""
        ep = {
            "section": section,
            "subsection": subsection,
            "path": path,
            "data": data,
        }
        self.endpoints.append(ep)

        api_name = data.get("api_name", "")

        # 查找预定义的中文名称（api_name 优先，更精确）
        cn_name = self.PATH_TO_CN_NAME.get(data.get("api_name", ""), "")
        if not cn_name:
            cn_name = self.PATH_TO_CN_NAME.get(path, "")

        # 构建搜索文本（权重：api_name > cn_name > path > description > param keys）
        search_parts = [
            api_name + " " + api_name,                       # 英文名称加倍权重
            cn_name + " " + cn_name + " " + cn_name,         # 中文名称三倍权重（确保中文能搜到）
            path,
            section,
            subsection,
            self._infer_cn_keywords(api_name, path, section, subsection, data.get("http_method", [])),
        ]
        # 参数描述
        for p in data.get("parameters", []):
            search_parts.append(p.get("key", ""))
            search_parts.append(p.get("description", ""))
        # JSON 示例中的键
        for ex in data.get("json_examples", []):
            content = ex.get("content", {})
            if isinstance(content, dict):
                search_parts.append(" ".join(self._extract_keys(content)))

        # 参考表中的可选值（如截面形状、单元类型等）— 加3倍权重确保能搜到
        for rt in data.get("reference_tables", []):
            for row in rt.get("rows", []):
                vals = row.get("values", [])
                for v in vals:
                    # 去掉引号后的纯值也加入索引
                    clean_v = v.strip('"').strip("'")
                    search_parts.append(v + " " + v + " " + v)  # 3x weight
                    if clean_v != v:
                        search_parts.append(clean_v + " " + clean_v + " " + clean_v)

        self.search_index.append(" ".join(search_parts).lower())

    def _infer_cn_keywords(self, api_name, path, section, subsection, http_methods):
        """根据 API 名称、路径、HTTP方法、所属类别推断中文关键词和显示名称。"""
        keywords = []
        name_lower = api_name.lower()
        path_lower = path.lower()
        sub_lower = subsection.lower()
        all_text = name_lower + " " + path_lower + " " + sub_lower

        # HTTP 方法 → 中文动词
        if isinstance(http_methods, str):
            http_methods = [http_methods]
        methods_upper = [m.upper() for m in http_methods]
        cn_verbs = []
        if "POST" in methods_upper:
            cn_verbs = ["创建", "新建", "添加", "设置", "定义", "施加", "分配", "生成"]
        if "GET" in methods_upper:
            cn_verbs += ["查询", "获取", "查看", "读取", "提取", "导出"]
        if "PUT" in methods_upper:
            cn_verbs += ["修改", "更新", "编辑", "更改"]
        if "DELETE" in methods_upper:
            cn_verbs += ["删除", "移除", "清除"]

        if cn_verbs:
            keywords.append(" ".join(cn_verbs))

        # 按关键词匹配生成中文标签
        mappings = [
            (["pjcf", "project info"], "项目信息"),
            (["unit"], "单位"),
            (["styp", "struct type"], "结构类型"),
            (["grup", "group"], "分组"),
            (["bngr", "boundary group"], "边界组"),
            (["ldgr", "load group"], "荷载组"),
            (["tdgr", "tendon group"], "钢束组"),
            (["node", "nodal"], "节点"),
            (["elem", "element", "beam elem", "truss elem"], "单元"),
            (["bem", "beam"], "梁单元"),
            (["truss"], "桁架单元"),
            (["plate", "wall", "plane"], "板单元"),
            (["solid"], "实体单元"),
            (["matl", "material"], "材料"),
            (["sect", "section", "sectprop"], "截面"),
            (["cons", "constraint", "restraint", "support", "bngr"], "约束/支座"),
            (["spring", "nspr", "ssps", "espr"], "弹簧"),
            (["cnld", "nodal load", "conl"], "节点荷载"),
            (["bmld", "beam load"], "梁单元荷载"),
            (["pres", "pslt", "pressure"], "压力荷载"),
            (["temp", "thermal", "btmp"], "温度荷载"),
            (["tdnt", "tendon", "prestress"], "预应力/钢束"),
            (["mvld", "mvhl", "moving", "traffic", "lane"], "移动荷载"),
            (["settle", "smst"], "沉降"),
            (["seismic", "earthquake", "resp spec"], "地震/反应谱"),
            (["wind"], "风荷载"),
            (["self", "dead", "gravity"], "自重"),
            (["bodf", "lcname", "load case"], "荷载工况"),
            (["lcom", "comb", "combination", "combw", "lcbn"], "荷载组合"),
            (["displace", "displ"], "位移结果"),
            (["beamforce", "beam force"], "梁单元内力"),
            (["trussforce", "truss force"], "桁架内力"),
            (["stress"], "应力结果"),
            (["reaction"], "反力结果"),
            (["moment", "bend"], "弯矩"),
            (["shear"], "剪力"),
            (["axial"], "轴力"),
            (["mode", "eigen", "modal", "eigenvalue"], "模态/振型"),
            (["buckling"], "屈曲"),
            (["period"], "周期"),
            (["time", "hist", "this", "th"], "时程结果"),
            (["construct", "stage", "stct", "cs"], "施工阶段"),
            (["nonlinear", "nlct"], "非线性分析"),
            (["pushover"], "推覆分析"),
            (["anal", "analysis"], "分析控制"),
            (["result", "output", "extract"], "结果提取"),
            (["table"], "表格"),
            (["capture", "screenshot"], "截图"),
            (["select"], "选择对象"),
            (["display", "view show"], "显示控制"),
            (["save", "saveas"], "保存项目"),
            (["open"], "打开项目"),
            (["close"], "关闭项目"),
            (["new"], "新建项目"),
            (["mesh", "automesh", "divide"], "网格划分"),
            (["property", "prop"], "截面特性"),
            (["design"], "设计"),
            (["girder", "main beam"], "主梁"),
            (["pier", "column"], "桥墩/柱"),
            (["cable", "stay"], "拉索"),
            (["heat", "hydrat", "hhyd"], "水化热"),
            (["mass"], "质量"),
            (["weight"], "重量"),
            (["grid", "coor"], "坐标系/网格"),
            (["import"], "导入"),
            (["export"], "导出"),
            (["delete", "remove"], "删除"),
            (["update", "put", "modify"], "修改"),
            (["query", "get", "retrieve", "info", "status"], "查询状态"),
        ]

        cn_labels = []
        for eng_terms, cn_label in mappings:
            for term in eng_terms:
                if term in all_text:
                    cn_labels.append(cn_label)
                    keywords.append(cn_label)
                    break

        # ── 生成"动词+名词"组合关键词 ──
        cn_nouns = set()
        for kw_group in keywords:
            for word in kw_group.split():
                if len(word) >= 2 and not any(w in cn_verbs for w in [word]):
                    cn_nouns.add(word)

        if cn_verbs and cn_nouns:
            combined = []
            for verb in cn_verbs[:4]:
                for noun in list(cn_nouns)[:6]:
                    combined.append(verb + noun)
            keywords.append(" ".join(combined))

        return " ".join(keywords)

    # 综合建模意图检测：当用户查询包含这些词时，自动扩展为包含所有建模步骤
    MODELING_INTENT_KEYWORDS = [
        "建立", "建模", "创建模型", "建个模型", "搭个模型", "建一个",
        "连续梁", "简支梁", "框架", "桥梁", "结构模型",
        "帮我建", "帮我建立", "做一个", "做个",
    ]
    # 建模必须覆盖的核心端点及其中文搜索词
    MODELING_CORE_KEYWORDS = [
        "新建项目 new project",
        "单位系统 unit system 单位",
        "材料 material 混凝土 钢材 MATL",
        "截面 section SECT 箱型",
        "节点 node NODE 坐标",
        "单元 element ELEM 梁单元",
        "边界条件 约束 支座 constraint CONS",
    ]

    def _expand_query(self, query):
        """将中文关键词扩展为包含英文映射的搜索字符串，提高中文搜索命中率。"""
        seen = set()
        terms = [query]
        seen.add(query.lower())

        # 检测综合建模意图：自动注入所有建模步骤关键词
        if any(kw in query for kw in self.MODELING_INTENT_KEYWORDS):
            for kw_group in self.MODELING_CORE_KEYWORDS:
                for word in kw_group.lower().split():
                    if word not in seen:
                        seen.add(word)
                        terms.append(word)

        for cn, en in self.CN_EN_MAP.items():
            if cn in query:
                for word in en.lower().split():
                    if word not in seen:
                        seen.add(word)
                        terms.append(word)
        return " ".join(terms)

    @staticmethod
    def _extract_keys(obj, depth=0):
        """递归提取 JSON 对象中的所有键名。"""
        if depth > 5:
            return []
        keys = []
        if isinstance(obj, dict):
            for k, v in obj.items():
                keys.append(k)
                keys.extend(APIRetriever._extract_keys(v, depth + 1))
        elif isinstance(obj, list) and obj:
            keys.extend(APIRetriever._extract_keys(obj[0], depth + 1))
        return keys

    # ── 搜索方法 ─────────────────────────────────────────────────────────

    def search(self, query, section=None, top_k=10):
        if not query.strip():
            results = [(ep, 0.0) for ep in self.endpoints]
        else:
            expanded_query = self._expand_query(query)
            query_lower = expanded_query.lower()
            query_original = query.strip().lower()
            terms = query_lower.split()
            cn_terms_in_query = [t for t in terms if any('一' <= c <= '鿿' for c in t)]

            scores = []
            for i, doc_text in enumerate(self.search_index):
                score = 0.0
                ep = self.endpoints[i]
                api_name_lower = ep["data"].get("api_name", "").lower()
                path_lower = ep["path"].lower()
                name_path_text = api_name_lower + " " + path_lower

                # ── 路径匹配（最高权重）──
                if query_original == path_lower.lstrip("/"):
                    score += 800
                elif query_original in path_lower:
                    score += 300
                path_parts = path_lower.replace("/", " ").replace("-", " ").split()
                for term in terms:
                    if len(term) >= 2:
                        for pp in path_parts:
                            if term == pp:
                                score += 120
                            elif term in pp and len(pp) >= 4:
                                score += 35

                # ── API 名称匹配 ──
                if query_original in api_name_lower:
                    score += 200
                name_parts = api_name_lower.replace("-", " ").split()
                for term in terms:
                    if len(term) >= 2 and len(term) <= 30:
                        for np in name_parts:
                            if term == np:
                                score += 80

                # ── 中文关键词在搜索索引中直接匹配 ──
                for ct in cn_terms_in_query:
                    if ct in doc_text:
                        # 中文匹配权重更高（中文名称在索引中有3x权重）
                        count = doc_text.count(ct)
                        score += 60 * min(count, 5)
                    elif len(ct) >= 3:
                        # 中文无空格分词，拆成2字子串匹配（如"混凝土材料"→"材料"）
                        sub_score = 0
                        for ci in range(len(ct) - 1):
                            sub = ct[ci:ci+2]
                            if sub in doc_text:
                                sub_score += 15
                        score += min(sub_score, 60)

                # ── 英文扩展词匹配 ──
                en_terms = [t for t in terms if t not in cn_terms_in_query and 2 <= len(t) <= 30]
                for term in en_terms:
                    count_in_core = name_path_text.count(term)
                    if count_in_core > 0:
                        score += count_in_core * 12
                    else:
                        desc_count = max(0, doc_text.count(term) - count_in_core)
                        # 参考表值的匹配权重（较高，因为截面形状、单元类型等关键信息都在这）
                        score += min(desc_count * 20, 150)

                # ── 章节语义匹配 ──
                create_words = {"创建", "新建", "添加", "定义", "施加", "分配", "设置", "生成",
                               "create", "new", "add", "apply", "assign", "define", "set",
                               "建模", "建立", "输入", "指定"}
                query_words = {"获取", "查询", "提取", "导出", "查看", "读取", "结果",
                              "get", "query", "retrieve", "fetch", "extract", "export",
                              "验算", "校核", "检查", "设计"}
                section_name = ep["section"]
                if any(w in query_original for w in create_words):
                    if section_name in ("DB", "DOC", "OPE"):
                        score += 60
                    elif section_name == "POST":
                        score -= 30
                if any(w in query_original for w in query_words):
                    if section_name == "POST":
                        score += 40
                    elif section_name in ("DB", "DOC"):
                        score -= 10

                # ── HTTP方法语义匹配 ──
                methods = ep["data"].get("http_method", [])
                if isinstance(methods, str):
                    methods = [methods]
                methods_lower = [m.lower() for m in methods]
                if any(w in query_original for w in create_words) and "post" in methods_lower:
                    score += 25
                if any(w in query_original for w in query_words) and "get" in methods_lower:
                    score += 20

                # ── M1变体惩罚：M1端点仅用于Hyper-S求解器，标准建模排除 ──
                if "-m1" in path_lower and not any(w in query_lower for w in ("m1", "hyper")):
                    score -= 200

                # ── 建模意图：核心端点直接加分确保不被遗漏 ──
                if any(kw in query_original for kw in self.MODELING_INTENT_KEYWORDS):
                    if path_lower in ("/doc/new", "/db/unit", "/db/matl", "/db/sect",
                                      "/db/node", "/db/elem", "/db/cons"):
                        score += 800

                if score > 0:
                    scores.append((i, score))

            scores.sort(key=lambda x: x[1], reverse=True)
            results = [(self.endpoints[i], s) for i, s in scores[:top_k * 2]]

        if section and section != "全部":
            results = [(ep, s) for ep, s in results if ep["section"] == section]

        return results[:top_k]

    def get_by_path(self, path):
        """根据路径精确获取一个端点。"""
        for ep in self.endpoints:
            if ep["path"] == path:
                return ep
        return None

    def get_sections(self):
        """获取所有章节及其接口数量。"""
        return dict(self.section_counts)

    def get_endpoints_by_section(self, section):
        """获取某个章节的所有端点。"""
        return [ep for ep in self.endpoints if ep["section"] == section]

    def get_subsections(self, section):
        """获取某个章节的所有子章节。"""
        subs = defaultdict(list)
        for ep in self.endpoints:
            if ep["section"] == section and ep["subsection"]:
                subs[ep["subsection"]].append(ep)
        return dict(subs)

    def get_total_count(self):
        """总接口数。"""
        return len(self.endpoints)

    def get_cn_display_name(self, ep):
        """为端点生成中文显示名称。优先使用预定义映射，否则从 API 名称推断。"""
        d = ep["data"]
        api_name = d.get("api_name", "")
        path = ep["path"]

        # 优先：api_name 更精确（POST 端点用它区分不同子类）
        cn_name = self.PATH_TO_CN_NAME.get(api_name, "")
        # 其次：path 查找
        if not cn_name:
            cn_name = self.PATH_TO_CN_NAME.get(path, "")
        # 兜底
        if not cn_name:
            cn_name = api_name[:40]

        return cn_name

    def format_endpoint_detail(self, ep):
        """格式化端点详情为可读文本（用于显示和发给 LLM）。

        关键设计：JSON 模板放在最前面，参数表仅做值参考。LLM 必须先看模板结构，
        再用参数表填充值，而不是根据参数表自己编造结构。"""
        d = ep["data"]
        lines = []
        lines.append(f"## {d.get('api_name', '')} — `{ep['path']}`")

        methods = d.get("http_method", [])
        if isinstance(methods, str):
            methods = [methods]
        lines.append(f"**方法**: {', '.join(methods)} | **章节**: {ep['section']}")

        # ── 第1优先级：强制包装规则 ──
        templates = d.get("request_templates", {})
        wrapper_info = templates.get("_wrapper_info", "")
        if wrapper_info:
            lines.append(f"\n### 🚨 包装规则")
            lines.append(wrapper_info)

        # ── 第1优先级：完整 JSON 模板（必须放在参数表前面！）──
        template_methods = [m for m in ["POST", "GET", "PUT", "DELETE"] if m in templates]
        if template_methods:
            lines.append(f"\n### 🚨 必须复制的 JSON 结构（替换 <> 占位符为实际值，禁止增删改字段名）")
            for method in template_methods:
                tmpl = templates[method]
                lines.append(f"\n**{method}**:")
                lines.append("```json")
                lines.append(json.dumps(tmpl, indent=2, ensure_ascii=False))
                lines.append("```")
                note = templates.get(f"{method}_note", "")
                if note:
                    lines.append(f"> {note}")

        # ── 第2优先级：字段值指南（仅用于填充模板中的占位符）──
        field_guide = d.get("request_field_guide", {})
        if field_guide:
            lines.append(f"\n### 字段取值说明（字段名以上方模板为准，此处仅说明值的含义）")
            for key, info in field_guide.items():
                req = "必填" if info.get("required") else "可选"
                dtype = info.get("type", "")
                desc = (info.get("desc") or "")[:150]
                default = info.get("default")
                extra = f" 默认={default}" if default is not None and default != "" else ""
                lines.append(f"- `{key}` [{req}] [{dtype}]: {desc}{extra}")

        # ── 第3优先级：参数详情（仅供参考，不覆盖模板结构）──
        params = d.get("parameters", [])
        if params:
            lines.append(f"\n### 参数详情（仅供参考，字段名以模板为准）")
            lines.append("| 参数名 | 类型 | 必填 | 说明 |")
            lines.append("|--------|------|------|------|")
            for p in params:
                req = "**是**" if p.get("required") else "否"
                desc = (p.get("description") or "")[:80]
                lines.append(f"| `{p['key']}` | {p.get('value_type', '')} | {req} | {desc} |")

        # ── 参考表（可选值）──
        ref_tables = d.get("reference_tables", [])
        if ref_tables:
            lines.append(f"\n### 参数可选值")
            for rt in ref_tables[:5]:  # 限制数量，避免上下文过长
                header = rt.get("table_header", "")
                rows = rt.get("rows", [])
                if not rows:
                    continue
                lines.append(f"\n**{header}**:")
                for row in rows[:20]:
                    vals = row.get("values", [])
                    if vals:
                        lines.append(f"- {' | '.join(vals)}")

        # ── JSON 示例（原始文档中的）──
        examples = d.get("json_examples", [])
        if examples:
            real_examples = [ex for ex in examples if not ex.get("note")]
            if real_examples:
                lines.append(f"\n### 原始文档示例")
                for ex in real_examples[:2]:
                    lines.append(f"**{ex.get('name', '示例')}**:")
                    lines.append("```json")
                    lines.append(json.dumps(ex.get("content", {}), indent=2, ensure_ascii=False))
                    lines.append("```")

        return "\n".join(lines)

    def format_endpoints_summary(self, endpoints, max_items=15):
        """格式化端点列表摘要。"""
        lines = []
        for ep, score in endpoints[:max_items]:
            d = ep["data"]
            n_params = len(d.get("parameters", []))
            methods = d.get("http_method", [])
            if isinstance(methods, str):
                methods = [methods]
            lines.append(
                f"- **{d.get('api_name', '')}** `{ep['path']}` "
                f"[{ep['section']}] {', '.join(methods)} "
                f"({n_params} 参数)"
            )
        return "\n".join(lines)
