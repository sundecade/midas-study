# DB — 模型数据库 API

DB（Database）部分是 MIDAS API 的核心，包含 225 个接口，覆盖了结构建模的方方面面：节点、单元、材料、截面、边界条件、各种荷载……几乎所有你在 MIDAS 界面里手动操作的建模步骤，都可以通过 DB API 来完成。

本章共 **225** 个接口。

## 工程背景

这是工程师用得最多的部分。如果你需要批量建模型、参数化建模、或者从其他软件导入模型，DB API 就是你的主要工具。

## 接口列表

| 接口 | 方法 | 参数数 | 说明 |
|------|------|--------|------|
| `/db/ACTL` | POST, GET, PUT, DELETE | 9 (2 必填) | Auto Rotational DOF Constraint for Truss / Plane Stress / So |
| `/db/ACTL-M1ᴴˢ⁾` | GET, PUT, DELETE | 11 (0 必填) | Auto Rotational DOF Constraint |
| `/db/BCCT` | POST, GET, PUT, DELETE | 16 (5 必填) | Support |
| `/db/BCGA-M1ᴴˢ⁾` | POST, GET, PUT, DELETE | 5 (4 必填) | Assign Boundary Combination to Analyses & Load Cases |
| `/db/BCGD-M1ᴴˢ⁾` | POST, GET, PUT, DELETE | 2 (2 必填) | Boundary Combination Name |
| `/db/BMLD` | POST, GET, PUT, DELETE | 20 (6 必填) | Beam Loads• Insert the data as an object |
| `/db/BNGR` | POST, GET, PUT | 2 (1 必填) | Boundary Group Name |
| `/db/BODF` | POST, GET, PUT, DELETE | 3 (2 必填) | Load Case Name |
| `/db/BTMP` | POST, GET, PUT, DELETE | 8 (3 必填) | Section Temperature List• Insert the data as an object |
| `/db/BUCK` | POST, GET, PUT, DELETE | 10 (3 必填) | Number of Modes |
| `/db/CAMB` | POST, GET, PUT, DELETE | 3 (3 必填) | Bridge Girder Element Group |
| `/db/CCFC` | POST, GET, PUT, DELETE | 7 (7 必填) | Function Name |
| `/db/CGLP` | POST, GET, PUT, DELETE | 3 (2 必填) | General Link ID Number |
| `/db/CJFG` | POST, GET, PUT, DELETE | 1 (1 必填) | Structure Group Names |
| `/db/CLDR` | POST, GET, PUT | 1 (1 必填) | Constraint Label Direction• Local x (+): 0• Local x (-): 1•  |
| `/db/CLWP` | POST, GET, PUT, DELETE | 14 (11 必填) | Name of Cutting Line |
| `/db/CMCS` | POST, GET, PUT, DELETE | 2 (2 必填) | Deformation |
| `/db/CNLD` | POST, GET, PUT, DELETE | 10 (2 必填) | Nodal Load• Insert the data as an object |
| `/db/CONS` | POST, GET, PUT, DELETE | 4 (2 必填) | Constraint Supports• Insert the data as an object |
| `/db/CO_F` | GET, PUT | 15 (1 必填) | Floor Load Type Name |
| `/db/CO_M` | GET, PUT | 11 (0 必填) | Wire Frame Red |
| `/db/CO_S` | GET, PUT | 11 (0 必填) | Wire Frame Red |
| `/db/CO_T` | GET, PUT | 11 (0 必填) | Wire Frame Red |
| `/db/CRGR` | POST, GET, PUT, DELETE | 1 (1 必填) | Structure Group Names |
| `/db/CRPC` | POST, GET, PUT, DELETE | 4 (2 必填) | Creep Coefficient for Construction Stage• Insert the data as |
| `/db/CSCS` | POST, GET, PUT, DELETE | 21 (6 必填) | Section ID |
| `/db/CUTL` | POST, GET, PUT, DELETE | 12 (8 必填) | Name of Cutting Line |
| `/db/DCON` | POST, GET, PUT, DELETE | 1 (1 必填) | Design Code¹⁾ |
| `/db/DCTL` | POST, GET, PUT, DELETE | 4 (0 必填) | X-Direction of Frame• Unbraced | Sway: “Unbraced Sway”• Brac |
| `/db/DOEL` | POST, GET, PUT, DELETE | 3 (3 必填) | Domain Type• Main-Domain: 0• Sub-Domain: 1 |
| `/db/DRLS` | POST, GET, PUT, DELETE | 2 (1 必填) | dummy |
| `/db/DSTL` | POST, GET, PUT, DELETE | 1 (1 必填) | Design Code¹⁾ |
| `/db/DYFG` | POST, GET, PUT, DELETE | 6 (5 必填) | Input Type• Auto Input: 0• User Input: 1 |
| `/db/DYLA` | POST, GET, PUT, DELETE | 2 (2 必填) | Impact Factor (%) |
| `/db/DYNF` | POST, GET, PUT, DELETE | 6 (5 必填) | Input Type• Auto Input: 0• User Input: 1 |
| `/db/EDMP` | POST, GET, PUT, DELETE | 2 (2 必填) | Change Property Method• Notional Size of Member: "NSM"• Volu |
| `/db/EFCT` | POST, GET, PUT, DELETE | 6 (3 必填) | Use Add Initial Force to Element Force |
| `/db/EIGV` | POST, GET, PUT, DELETE | 15 (9 必填) | Type of Analysis• Subspace Iteration: "EIGEN"• Lanczos: "LAN |
| `/db/EIGV-M1ᴴˢ⁾` | GET, PUT, DELETE | 13 (7 必填) | Eigen Vectors• Eigen Vectors (Lanczos): LANCZOS• Ritz Vector |
| `/db/ELEM` | POST, GET, PUT, DELETE | 16 (7 必填) | Element Type¹⁾ |
| `/db/ELNK` | POST, GET, PUT, DELETE | 12 (5 必填) | Assigned Node Number• [i Node, j Node] |
| `/db/EPMT` | POST, GET, PUT, DELETE | 30 (24 必填) | Plastic Material Name |
| `/db/EPMT-M1ᴴˢ⁾` | POST, GET, PUT, DELETE | 32 (30 必填) | Name |
| `/db/EPST` | POST, GET, PUT, DELETE | 19 (9 必填) | Prameters of Soil Properties Name |
| `/db/ESSF` | POST, GET, PUT, DELETE | 11 (1 必填) | Items |
| `/db/ETFC` | POST, GET, PUT, DELETE | 10 (6 必填) | Function Name |
| `/db/ETMP` | POST, GET, PUT, DELETE | 5 (3 必填) | Element Temperature• Insert the data as an object |
| `/db/EWSF` | POST, GET, PUT, DELETE | 10 (5 必填) | Effective Width Scale Factor• Insert the data as an object |
| `/db/EXLD` | POST, GET, PUT, DELETE | 1 (1 必填) | Load Case Name• Only load cases with pre-tension load |
| `/db/FBLA` | POST, GET, PUT, DELETE | 14 (3 必填) | Floor Load Type Name |
| `/db/FBLD` | POST, GET, PUT, DELETE | 6 (4 必填) | Floor Load Type Name |
| `/db/FIBR` | POST, GET, PUT, DELETE | 21 (16 必填) | Fiber Division Name |
| `/db/FIMP` | POST, GET, PUT, DELETE | 21 (19 必填) | Material Name |
| `/db/FMLD` | POST, GET, PUT, DELETE | 10 (4 必填) | Finishing Material Loads• Insert the data as an object |
| `/db/FRLS` | POST, GET, PUT, DELETE | 8 (3 必填) | Beam End Release• Insert the data as an object |
| `/db/GALDᴶ⁾` | POST, GET, PUT, DELETE | 18 (17 必填) | Load Case Name |
| `/db/GCMB` | POST, GET, PUT, DELETE | 4 (3 必填) | Set Start Point Zero |
| `/db/GRDP` | POST, GET, PUT, DELETE | 37 (30 必填) | Stiffness Proportional Value• Direct Specification: User Inp |
| `/db/GRUP` | POST, GET, PUT | 4 (1 必填) | Structure Group Name |
| `/db/GSBG` | POST, GET, PUT, DELETE | 10 (3 必填) | Group Name |
| `/db/GSPR` | POST, GET, PUT, DELETE | 4 (2 必填) | General Spring• Insert the data as an object |
| `/db/GSTP` | POST, GET, PUT, DELETE | 7 (1 必填) | General Spring Name |
| `/db/GTMP` | POST, GET, PUT, DELETE | 11 (5 必填) | Temperature Gradient• Insert the data as an object |
| `/db/HAHS` | POST, GET, PUT, DELETE | 1 (1 必填) | Heat Source Function Name |
| `/db/HECB` | POST, GET, PUT, DELETE | 6 (4 必填) | Element Convection Boundary• Insert the data as an object |
| `/db/HHCT` | POST, GET, PUT, DELETE | 15 (2 必填) | Final Stage• Last Stage: true• Other Stage: false |
| `/db/HHND` | POST, GET, PUT, DELETE | 5 (3 必填) | Name |
| `/db/HPCE` | POST, GET, PUT, DELETE | 10 (2 必填) | Pipe Cooling Name |
| `/db/HSFC` | POST, GET, PUT, DELETE | 14 (6 必填) | Function Name |
| `/db/HSPT` | POST, GET, PUT, DELETE | 4 (2 必填) | Prescribed Temperature• Insert the data as an object |
| `/db/HSTG` | POST, GET, PUT, DELETE | 11 (5 必填) | Hydration Stage Name |
| `/db/IEHC` | POST, GET, PUT, DELETE | 17 (17 必填) | Reference Location for Distributed Hinges• I-End: 0• Center: |
| `/db/IEHG` | POST, GET, PUT, DELETE | 2 (2 必填) | Name of Inelastic Hinge Property |
| `/db/IEHG-BEAM-M1ᴴˢ⁾` | POST, GET, PUT, DELETE | 1 (1 必填) | Inelastic Hinge Property |
| `/db/IEHG-GL-M1ᴴˢ⁾` | POST, GET, PUT, DELETE | 1 (1 必填) | Inelastic Hinge Property |
| `/db/IEHG-PSS-M1ᴴˢ⁾` | POST, GET, PUT, DELETE | 1 (1 必填) | Inelastic Hinge Property |
| `/db/IEHG-TRUSS-M1ᴴˢ⁾` | POST, GET, PUT, DELETE | 1 (1 必填) | Inelastic Hinge Property |
| `/db/IELC` | POST, GET, PUT, DELETE | 3 (3 必填) | Element |
| `/db/IEPI` | POST, GET, PUT, DELETE | 1 (0 必填) | Ignore Elements for NL. Analysis Initial Load |
| `/db/IFGS` | POST, GET, PUT | 2 (2 必填) | Direction |
| `/db/IMFM` | POST, GET, PUT, DELETE | 4 (0 必填) | Inelastic Material of Concrete |
| `/db/IMFM-M1ᴴˢ⁾` | POST, GET, PUT, DELETE | 6 (3 必填) | Material Type - Concrete |
| `/db/IMPF` | POST, GET, PUT, DELETE | 10 (9 必填) | Items |
| `/db/INMF` | POST, GET, PUT, DELETE | 4 (3 必填) | Element Type• Beam: "BEAM"• Truss: "TRUSS"• Elastic Link: "E |
| `/db/LCOM-CONC` | POST, GET, PUT, DELETE | 11 (5 必填) | Combination Number |
| `/db/LCOM-GEN` | POST, GET, PUT, DELETE | 10 (5 必填) | Combination Number |
| `/db/LCOM-SEISMIC` | POST, GET, PUT, DELETE | 10 (5 必填) | Combination Number |
| `/db/LCOM-SRC` | POST, GET, PUT, DELETE | 10 (5 必填) | Combination Number |
| `/db/LCOM-STEEL` | POST, GET, PUT, DELETE | 10 (5 必填) | Combination Number |
| `/db/LCOM-STLCOMP` | POST, GET, PUT, DELETE | 10 (5 必填) | Combination Number |
| `/db/LDGR` | POST, GET, PUT, DELETE | 1 (1 必填) | Load Group Name |
| `/db/LDSQ` | POST, GET, PUT, DELETE | 1 (1 必填) | Load Case Name |
| `/db/LENG` | POST, GET, PUT, DELETE | 6 (0 必填) | Unbraced Length Ly |
| `/db/LLAN` | POST, GET, PUT, DELETE | 19 (7 必填) | Common Items |
| `/db/LLANch` | POST, GET, PUT, DELETE | 18 (7 必填) | Common Items |
| `/db/LLANid` | POST, GET, PUT, DELETE | 18 (7 必填) | Common Items |
| `/db/LLANop` | POST, GET, PUT, DELETE | 23 (8 必填) | Name of Line Lane |
| `/db/LLANtr` | POST, GET, PUT, DELETE | 5 (4 必填) | Name of Line Lane |
| `/db/LTOM` | POST, GET, PUT, DELETE | 9 (4 必填) | Mass Direction• X: "X"• Y: "Y"• Z: "Z"• X, Y: "XY"• Y, Z: "Y |
| `/db/LTSR` | POST, GET, PUT, DELETE | 3 (2 必填) | Do not check for Slenderness Ratio |
| `/db/MADO` | POST, GET, PUT, DELETE | 5 (5 必填) | Domain Name |
| `/db/MATD` | GET, PUT, DELETE | 30 (8 必填) | Material Type• Concrete: "CONC" |
| `/db/MATL` | POST, GET, PUT, DELETE | 23 (15 必填) | Material Type• Concrete: "CONC"• Steel: "STEEL"• SRC: "SRC"• |
| `/db/MATL-M1ᴴˢ⁾` | POST, GET, PUT, DELETE | 23 (8 必填) | Name |
| `/db/MBTP` | POST, GET, PUT, DELETE | 1 (1 必填) | Member Type• Column : "COLUMN"• Beam : "BEAM"• Brace : "BRAC |
| `/db/MCON` | POST, GET, PUT, DELETE | 6 (4 必填) | Linear Constraints• Insert the data as an object |
| `/db/MEMB` | POST, GET, PUT, DELETE | 2 (1 必填) | Element Lists |
| `/db/MLFC` | POST, GET, PUT, DELETE | 7 (4 必填) | Function Name |
| `/db/MLSP` | POST, GET, PUT, DELETE | 5 (5 必填) | Input Type• Auto: "Auto Input"◦ Only for AASHTO LRFD |
| `/db/MLSR` | POST, GET, PUT, DELETE | 1 (1 必填) | Fixed Value: 0 |
| `/db/MVCD` | POST, GET, PUT, DELETE | 1 (1 必填) | Moving Load Code¹⁾ |
| `/db/MVCT` | POST, GET, PUT, DELETE | 31 (12 必填) | Analysis Method¹⁾• Exact: "EXACT"• Pivot: "PIVOT"• Quick: "Q |
| `/db/MVCTbs` | POST, GET, PUT, DELETE | 22 (8 必填) | Influence Generating Points• Number/Line Element: 0• Distanc |
| `/db/MVCTch` | POST, GET, PUT, DELETE | 111 (91 必填) | Load Point Selection• Influence Line Dependent Point: "INF"• |
| `/db/MVCTid` | POST, GET, PUT, DELETE | 29 (9 必填) | Influence Generating Points• Number/Line Element: 0• Distanc |
| `/db/MVCTtr` | POST, GET, PUT, DELETE | 9 (4 必填) | Load Point Selection• Influence Line Dependent Point: 1• All |
| `/db/MVHC` | POST, GET, PUT, DELETE | 2 (2 必填) | Vehicle Class Name |
| `/db/MVHL` | POST, GET, PUT, DELETE | 20 (9 必填) | Function Name• AASHTO Standard: 1 |
| `/db/MVHLtr` | POST, GET, PUT, DELETE | 12 (10 必填) | Vehicular Load Name |
| `/db/MVLD` | POST, GET, PUT, DELETE | 35 (32 必填) | Load Case Name |
| `/db/MVLDbs` | POST, GET, PUT, DELETE | 22 (19 必填) | Load Case Name |
| `/db/MVLDch` | POST, GET, PUT, DELETE | 21 (18 必填) | Load Case Name |
| `/db/MVLDeu` | POST, GET, PUT, DELETE | 33 (31 必填) | Load Case Name |
| `/db/MVLDid` | POST, GET, PUT, DELETE | 20 (15 必填) | Load Case Name |
| `/db/MVLDpl` | POST, GET, PUT, DELETE | 20 (17 必填) | Load Case Name |
| `/db/MVLDtr` | POST, GET, PUT, DELETE | 7 (6 必填) | Load Case Name |
| `/db/NBOF` | POST, GET, PUT, DELETE | 10 (2 必填) | Load Case Name |
| `/db/NLCT` | POST, GET, PUT, DELETE | 19 (11 必填) | Nonlinear Type• Geometry Nonlinear: "GEOM"• Material Nonline |
| `/db/NLCT-M1ᴴˢ⁾` | GET, PUT, DELETE | 24 (11 必填) | Nonlinear Analysis Type• Global: ALL• Load Case: SELECT |
| `/db/NLLP` | POST, GET, PUT, DELETE | 28 (0 必填) | General Link Property Name |
| `/db/NLNK` | POST, GET, PUT, DELETE | 12 (8 必填) | Node 1 ID Number |
| `/db/NLNK-M1ᴴˢ⁾` | POST, GET, PUT, DELETE | 11 (10 必填) | General Link Property Name |
| `/db/NMAS` | POST, GET, PUT, DELETE | 6 (1 必填) | Translational Lumped Mass in GCS X-direction |
| `/db/NODE` | POST, GET, PUT, DELETE | 3 (0 必填) | Coordinates - x |
| `/db/NPLN` | POST, GET, PUT, DELETE | 6 (4 必填) | Plane Name |
| `/db/NSPR` | POST, GET, PUT, DELETE | 15 (6 必填) | Point Spring• Insert the data as an object |
| `/db/NTMP` | POST, GET, PUT, DELETE | 5 (3 必填) | Nodal Temperature• Insert the data as an object |
| `/db/OFFS` | POST, GET, PUT, DELETE | 10 (2 必填) | Beam End Offsets• Insert the data as an object |
| `/db/PDEL` | POST, GET, PUT, DELETE | 5 (4 必填) | Number of Iterations |
| `/db/PHGE` | POST, GET, PUT, DELETE | 4 (4 必填) | ID |
| `/db/PJCF` | POST, GET, PUT, DELETE | 21 (0 必填) | Project Name |
| `/db/PLCB` | POST, GET, PUT, DELETE | 1 (1 必填) | Static Load Case Name |
| `/db/PNLA` | POST, GET, PUT, DELETE | 16 (11 必填) | Load Case Name |
| `/db/PNLD` | POST, GET, PUT, DELETE | 15 (7 必填) | Load Type Name |
| `/db/POGD` | POST, GET, PUT, DELETE | 73 (51 必填) | Geometric Nonlinearity Type• None: "NONE"• Large Displacemen |
| `/db/POGD-M1ᴴˢ⁾` | GET, PUT, DELETE | 31 (18 必填) | Geometric Nonlinearity Type• None: 0• Large Displacements: 1 |
| `/db/POLC` | POST, GET, PUT, DELETE | 26 (19 必填) | Load Case Name |
| `/db/POLC-M1ᴴˢ⁾` | POST, GET, PUT, DELETE | 21 (20 必填) | Load Case |
| `/db/POSL` | POST, GET, PUT, DELETE | 14 (5 必填) | Parameters of Seismic Earth Name |
| `/db/POSP` | POST, GET, PUT, DELETE | 13 (11 必填) | Parameters of Soil Properties Name |
| `/db/PRES` | POST, GET, PUT, DELETE | 13 (6 必填) | Pressure Loads• Insert the data as an object |
| `/db/PRLS` | POST, GET, PUT, DELETE | 7 (5 必填) | Plate End Release• Insert the data as an object |
| `/db/PRST` | POST, GET, PUT, DELETE | 9 (3 必填) | Prestress Beam Loads• Insert the data as an object |
| `/db/PSLT` | POST, GET, PUT, DELETE | 10 (7 必填) | Pressure Load Type Name |
| `/db/PSSF` | POST, GET, PUT, DELETE | 11 (1 必填) | Plate Stiffness Scale Factor• Insert the data as an object |
| `/db/PTNS` | POST, GET, PUT, DELETE | 5 (3 必填) | Pretension Loads• Insert the data as an object |
| `/db/PZEF` | POST, GET, PUT | 3 (3 必填) | Calculation Option• Auto Calculate Panel Zone Offset Distanc |
| `/db/RCHK` | POST, GET, PUT, DELETE | 9 (8 必填) | Member Type• Beam: "BEAM"• Column: "COLUMN" |
| `/db/RIGD` | POST, GET, PUT, DELETE | 5 (3 必填) | Rigid Link• Insert the data as an object |
| `/db/RPSC` | POST, GET, PUT, DELETE | 35 (11 必填) | Same Rebar Data at i and j-end (Longitudinal) |
| `/db/SBDO` | POST, GET, PUT, DELETE | 22 (8 必填) | Sub Domain Name |
| `/db/SDHY` | POST, GET, PUT, DELETE | 18 (17 必填) | Common Data |
| `/db/SDIS` | POST, GET, PUT, DELETE | 32 (30 必填) | Common Data |
| `/db/SDSP` | POST, GET, PUT, DELETE | 5 (2 必填) | Specified Displacement of Support• Insert the data as an obj |
| `/db/SDST` | POST, GET, PUT, DELETE | 23 (21 必填) | Common Data |
| `/db/SDVE` | POST, GET, PUT, DELETE | 23 (22 必填) | Common Data |
| `/db/SDVI` | POST, GET, PUT, DELETE | 25 (23 必填) | Common Data |
| `/db/SECF` | POST, GET, PUT, DELETE | 21 (1 必填) | Stiffness• Insert the data as an object |
| `/db/SECT` | POST, GET, PUT, DELETE | 15 (4 必填) | Section Data Type¹⁾ |
| `/db/SINF` | POST, GET, PUT, DELETE | 1 (1 必填) | Assigned Element List |
| `/db/SKEW` | POST, GET, PUT, DELETE | 31 (3 必填) | Input Method• Angle: 1• 3 points: 2• Vector: 3• Line Vector: |
| `/db/SLAN` | POST, GET, PUT, DELETE | 19 (5 必填) | Name of Surface Lane |
| `/db/SLANch` | POST, GET, PUT, DELETE | 13 (5 必填) | Name of Surface Lane |
| `/db/SLANop` | POST, GET, PUT, DELETE | 21 (8 必填) | Name of Surface Lane |
| `/db/SMCT` | POST, GET, PUT, DELETE | 2 (0 必填) | Plate Concurrent Force• Active: true• Inactive: false |
| `/db/SMLC` | POST, GET, PUT, DELETE | 7 (7 必填) | Settlement Load Case Name |
| `/db/SMPT` | POST, GET, PUT, DELETE | 3 (3 必填) | Settlement Group Name |
| `/db/SPAN` | POST, GET, PUT, DELETE | 8 (8 必填) | Span Name |
| `/db/SPFC` | POST, GET, PUT, DELETE | 120 (7 必填) | RS Function Name |
| `/db/SPLC` | POST, GET, PUT, DELETE | 46 (19 必填) | Spectrum Load Case Name |
| `/db/SSPS` | POST, GET, PUT, DELETE | 8 (4 必填) | Surface Spring• Insert the data as an object |
| `/db/STAG` | POST, GET, PUT, DELETE | 20 (7 必填) | CS Stage Name |
| `/db/STBK` | POST, GET, PUT, DELETE | 7 (3 必填) | Node 1 |
| `/db/STCT` | POST, GET, PUT, DELETE | 66 (7 必填) | Final Stage Option• Last Stage: true• Other Stage: false |
| `/db/STCT-M1ᴴˢ⁾` | GET, PUT, DELETE | 45 (9 必填) | Final Stage |
| `/db/STLD` | POST, GET, PUT, DELETE | 4 (2 必填) | Ordering Index in GUI |
| `/db/STMP` | POST, GET, PUT, DELETE | 3 (1 必填) | System Temperature |
| `/db/STOR` | POST, GET, PUT, DELETE | 15 (15 必填) | Story Name |
| `/db/STRPSSM` | POST, GET, PUT, DELETE | 7 (6 必填) | Same Additional Stress Points Data at i and j-end |
| `/db/STYP` | GET, PUT | 10 (0 必填) | Structure Type• 3-D: 0• X-Z Plane: 1• Y-Z Plane: 2• X-Y Plan |
| `/db/STYP-M1ᴴˢ⁾` | GET, PUT, DELETE | 10 (5 必填) | Structure Type• 3-D: 3D• X-Z Plane: XZ• Y-Z Plane: YZ• X-Y P |
| `/db/TDCS` | POST, GET, PUT, DELETE | 3 (3 必填) | Tendon Profile |
| `/db/TDGR` | POST, GET, PUT, DELETE | 1 (1 必填) | Tendon Group Name |
| `/db/TDME` | POST, GET, PUT, DELETE | 23 (21 必填) | Material Name |
| `/db/TDMF` | POST, GET, PUT, DELETE | 10 (8 必填) | Material Function Name |
| `/db/TDMT` | POST, GET, PUT, DELETE | 63 (43 必填) | Creep Function Name |
| `/db/TDNA` | POST, GET, PUT, DELETE | 42 (13 必填) | Tendon Name |
| `/db/TDNT` | POST, GET, PUT, DELETE | 25 (9 必填) | Tendon Name |
| `/db/TDPL` | POST, GET, PUT, DELETE | 10 (5 必填) | Tendon Prestress• Insert the data as an object |
| `/db/THFC` | POST, GET, PUT, DELETE | 16 (14 必填) | Time History Function Name |
| `/db/THGA` | POST, GET, PUT, DELETE | 11 (7 必填) | Time History Load Case Name |
| `/db/THGC` | POST, GET, PUT, DELETE | 28 (8 必填) | Time History Energy Result |
| `/db/THGC-M1ᴴˢ⁾` | GET, PUT, DELETE | 11 (6 必填) | Geometric Nonlinearity Type• None: 0• Large Displacements: 1 |
| `/db/THIK` | POST, GET, PUT, DELETE | 7 (4 必填) | Thickness Name |
| `/db/THIS` | POST, GET, PUT, DELETE | 58 (12 必填) | Common Setting |
| `/db/THIS-M1ᴴˢ⁾` | POST, GET, PUT, DELETE | 54 (46 必填) | Name |
| `/db/THMS` | POST, GET, PUT, DELETE | 13 (4 必填) | Multiple Support Excitation• Insert the data as an object |
| `/db/THNL` | POST, GET, PUT, DELETE | 7 (6 必填) | Dynamic Nodal Loads• Insert the data as an object |
| `/db/THOO-M1ᴴˢ⁾` | GET, PUT, DELETE | 10 (2 必填) | Nonlinear Analysis Result Output Option |
| `/db/THRE` | POST, GET, PUT, DELETE | 8 (3 必填) | Time History Load Cases |
| `/db/THRG` | POST, GET, PUT, DELETE | 5 (2 必填) | Name |
| `/db/THRI` | POST, GET, PUT, DELETE | 7 (2 必填) | Name |
| `/db/THRS` | POST, GET, PUT, DELETE | 4 (2 必填) | Name |
| `/db/THSL` | POST, GET, PUT, DELETE | 5 (4 必填) | Time History Load Case Name |
| `/db/TMAT` | POST, GET, PUT, DELETE | 2 (2 必填) | Creep/Shrinkage Name |
| `/db/TMLD` | POST, GET, PUT, DELETE | 4 (2 必填) | Time Load for Construction Stage• Insert the data as an obje |
| `/db/TSGR` | POST, GET, PUT, DELETE | 10 (6 必填) | Tapered Group Name |
| `/db/ULCT` | POST, GET, PUT, DELETE | 1 (0 必填) | Assign Member• For Underground Loads : true• For None-underg |
| `/db/ULFC` | POST, GET, PUT, DELETE | 13 (8 必填) | Constraint Name |
| `/db/UNIT` | GET, PUT | 4 (0 必填) | Force (Mass)• N (kg): "N"• kN (ton): "KN"• kgf (kg): "KGF"•  |
| `/db/VBEM` | POST, GET, PUT, DELETE | 2 (2 必填) | Virtual Section 1 |
| `/db/VSEC` | POST, GET, PUT, DELETE | 10 (10 必填) | Name |
| `/db/WMAK` | POST, GET, PUT, DELETE | 2 (2 必填) | Wall Mark Name |
| `/db/WVLD` | POST, GET, PUT, DELETE | 53 (1 必填) | Wave Load Name |
| `db/HHCT-M1ᴴˢ⁾` | GET, PUT, DELETE | 23 (10 必填) | Final Stage• Last Stage: true• Other Stage: false |


---

# 详细教程

## Project Information — `/db/PJCF`

**HTTP 方法**: POST, GET, PUT, DELETE | **参数总数**: 21（0 必填 + 21 可选）

### 1. 这是什么？（工程含义）

**Project Information** — 这是模型数据库的创建和查询操作，属于 Project 类别。

Project Name

> 简单说：这个接口用来**Project Information**。

### 2. JSON 结构（逐层解释）

下面按照从外到内的顺序解释每一层的 JSON 结构：

```json
{
  "PJCF": {
    "PROJECT (可选)": "<PROJECT>",
    "REVISION (可选)": "<REVISION>",
    "USER (可选)": "<USER>",
    "EMAIL (可选)": "<EMAIL>",
    "ADDRESS (可选)": "<ADDRESS>",
    "TEL (可选)": "<TEL>",
    "FAX (可选)": "<FAX>",
    "CLIENT (可选)": "<CLIENT>",
    "TITLE (可选)": "<TITLE>",
    "ENGINEER (可选)": "<ENGINEER>",
    "EDATE (可选)": "<EDATE>",
    "CHECK1 (可选)": "<CHECK1>",
    "CDATE1 (可选)": "<CDATE1>",
    "CHECK2 (可选)": "<CHECK2>",
    "CDATE2 (可选)": "<CDATE2>",
    "CHECK3 (可选)": "<CHECK3>",
    "CDATE3 (可选)": "<CDATE3>",
    "APPROVE (可选)": "<APPROVE>",
    "ADATE (可选)": "<ADATE>",
    "COMMENT (可选)": "<COMMENT>"
  },
  "APROVE (可选)": "<APROVE>"
}
```

**第 1 层：`PJCF`** — 20 个参数在这一层

- `"PROJECT"`: 文字（字符串） — Project Name
- `"REVISION"`: 文字（字符串） — Revision Info
- `"USER"`: 文字（字符串） — Username
- `"EMAIL"`: 文字（字符串） — E-mail
- `"ADDRESS"`: 文字（字符串） — Address
- `"TEL"`: 文字（字符串） — Telephone Numbers
- `"FAX"`: 文字（字符串） — Fax Numbers
- `"CLIENT"`: 文字（字符串） — Client Information
- ... *还有 12 个参数*

**第 2 层：最外层**
这是整个 JSON 的入口。
- `"APROVE"`: 文字（字符串） — Reviewer Name 5


### 3. 必填 vs 可选参数

**可选参数**（填不填都行）：

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `PROJECT` | 文字（字符串） | `无` | Project Name |
| `REVISION` | 文字（字符串） | `无` | Revision Info |
| `USER` | 文字（字符串） | `无` | Username |
| `EMAIL` | 文字（字符串） | `无` | E-mail |
| `ADDRESS` | 文字（字符串） | `无` | Address |
| `TEL` | 文字（字符串） | `无` | Telephone Numbers |
| `FAX` | 文字（字符串） | `无` | Fax Numbers |
| `CLIENT` | 文字（字符串） | `无` | Client Information |
| `TITLE` | 文字（字符串） | `无` | Title |
| `ENGINEER` | 文字（字符串） | `无` | Reviewer Name 1 |
| `EDATE` | 文字（字符串） | `无` | Reviewed Date 1 |
| `CHECK1` | 文字（字符串） | `无` | Reviewer Name 2 |
| `CDATE1` | 文字（字符串） | `无` | Reviewed Data 2 |
| `CHECK2` | 文字（字符串） | `无` | Reviewer Name 3 |
| `CDATE2` | 文字（字符串） | `无` | Reviewed Data 3 |


### 4. 可选参数放在哪里？

可选参数必须放在正确的 JSON 层级中。以下是每个可选参数的具体位置：

- `PROJECT` 的路径：**"PJCF" → "PROJECT"**
  意思是：在 JSON 中依次打开 PJCF, PROJECT，最后填入 `PROJECT` 的值
- `REVISION` 的路径：**"PJCF" → "REVISION"**
  意思是：在 JSON 中依次打开 PJCF, REVISION，最后填入 `REVISION` 的值
- `USER` 的路径：**"PJCF" → "USER"**
  意思是：在 JSON 中依次打开 PJCF, USER，最后填入 `USER` 的值
- `EMAIL` 的路径：**"PJCF" → "EMAIL"**
  意思是：在 JSON 中依次打开 PJCF, EMAIL，最后填入 `EMAIL` 的值
- `ADDRESS` 的路径：**"PJCF" → "ADDRESS"**
  意思是：在 JSON 中依次打开 PJCF, ADDRESS，最后填入 `ADDRESS` 的值
- `TEL` 的路径：**"PJCF" → "TEL"**
  意思是：在 JSON 中依次打开 PJCF, TEL，最后填入 `TEL` 的值
- `FAX` 的路径：**"PJCF" → "FAX"**
  意思是：在 JSON 中依次打开 PJCF, FAX，最后填入 `FAX` 的值
- `CLIENT` 的路径：**"PJCF" → "CLIENT"**
  意思是：在 JSON 中依次打开 PJCF, CLIENT，最后填入 `CLIENT` 的值
- `TITLE` 的路径：**"PJCF" → "TITLE"**
  意思是：在 JSON 中依次打开 PJCF, TITLE，最后填入 `TITLE` 的值
- `ENGINEER` 的路径：**"PJCF" → "ENGINEER"**
  意思是：在 JSON 中依次打开 PJCF, ENGINEER，最后填入 `ENGINEER` 的值

**理解 JSON 路径**：想象你在文件夹里找文件——`A.B.C` 就像 `A文件夹/B文件夹/C文件`。


### 5. 参数之间的关系

以下参数之间存在关联关系：

这个接口的参数之间没有复杂的依赖关系。每个参数可以独立填写。

**一般规律**：`TYPE` 类参数决定结构类型，然后 `PARAM` 类参数的格式由 `TYPE` 决定。


### 6. 最小可运行代码

以下是能跑起来的最简代码：

```python
import requests
import urllib3
urllib3.disable_warnings()  # 关闭 SSL 警告

# MIDAS 服务地址（根据你的产品修改端口）
BASE = "https://127.0.0.1:1102"

url = f"{BASE}/db/PJCF"

# JSON 数据 — 这是你要发给 MIDAS 的内容
data = {}

# 发送请求
r = requests.post(url, json=data, verify=False)

# 检查结果
if r.status_code == 200:
    print("成功！")
    print(r.json())
else:
    print(f"失败，错误码：{r.status_code}")
```

**运行前确认**：MIDAS Civil 已经打开，并且加载了一个项目。


### 7. 工程意义

参数化建模的核心。一旦掌握，你可以用几十行代码代替几小时的点鼠标操作。参数变化时，重新生成模型只需要几秒钟。

### 8. 常见错误

使用这个接口时最容易犯的错误：

1. **没有必填参数**——这个接口比较宽容，但你至少要发一个空的 JSON 对象 `{}`。
2. **JSON 层级放错**：这个接口有 2 个层级，参数放错层级就不会生效。注意看每个参数的 `json_path`。
4. **URL 写错**：确认路径是 `/db/PJCF`——多一个斜杠或少一个都会导致 404 错误。


### 9. Python 批量生成案例

如果你需要创建多个类似的调用（例如创建 100 个节点），可以用列表+循环来生成：

```python
import requests
import urllib3
urllib3.disable_warnings()

BASE = "https://127.0.0.1:1102"

# 定义基础数据模板
def make_data(**kwargs):
    """根据参数生成 Project Information 的 JSON 数据。"""
    data = {}
    # 在这里修改需要变化的值
    for key, value in kwargs.items():
        # 根据 json_path 更新对应位置的值
        pass  # 具体逻辑见下面的 for 循环例子
    return data

# 批量调用
results = []
for i in range(1, 11):  # 生成 10 个
    data = make_data()    # 在这里修改参数
    r = requests.post(f"{BASE}/db/PJCF", json=data, verify=False)
    results.append(r.json())
    print(f'第 {i} 个完成')
```


### 10. for 循环优化案例

对于批量操作，直接写 for 循环每次发一个请求效率不够高。以下是优化技巧：

**技巧 1：利用 Assign 结构一次发送多个对象**

很多 DB 接口支持在一次请求中发送多个对象，通过 `Assign` 下的编号 `"1"`, `"2"`, ... 区分。

```python
# ❌ 慢：循环 100 次，每次发一个节点
for i in range(100):
    data = {"Assign": {"1": {"X": i, "Y": 0, "Z": 0}}}
    requests.post(url, json=data, verify=False)

# ✅ 快：一次发 100 个节点
nodes = {}
for i in range(100):
    nodes[str(i+1)] = {"X": i, "Y": 0, "Z": 0}
data = {"Assign": nodes}
requests.post(url, json=data, verify=False)
```

**技巧 2：使用列表推导式预生成数据**（在 Project Information 中适用）

```python
# 列表推导式 — 一行代码生成所有节点的坐标
nodes = {str(i+1): {"X": i*5.0, "Y": 0, "Z": 0} for i in range(100)}
data = {"Assign": nodes}
requests.post(url, json=data, verify=False)
```

**通用优化原则**：

1. 能一次发多个就不要循环发单个
2. 用 `requests.Session()` 代替 `requests.post()` 做批量请求
3. 先生成所有数据，再统一发送，不要在循环里逐个生成+发送



---

### Unit System — `/db/UNIT`

**方法**: GET, PUT | **参数**: 0 必填 + 4 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `FORCE` | 文字（字符串） | 否 | Force (Mass)• N (kg): "N"• kN (ton): "KN"• kgf (kg): "KGF"• tonf (ton): "TONF"•  |
| `DIST` | 文字（字符串） | 否 | Length• m: "M"• cm: "CM"• mm: "MM"• ft: "FT"• in: "IN" |
| `HEAT` | 文字（字符串） | 否 | Heat• cal: "CAL"• kcal: "KCAL"• J: "J"• kJ: "KJ"• Btu: "BTU" |
| `TEMPER` | 文字（字符串） | 否 | Temperature Unit• Celsius: "C"• Fahrenheit: "F" |

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "FORCE": "KIPS",
      "DIST": "FT",
      "HEAT": "BTU",
      "TEMPER": "C"
    }
  }
}
```


---

### Structure Type — `/db/STYP`

**方法**: GET, PUT | **参数**: 0 必填 + 10 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `STYP` | 整数 | 否 | Structure Type• 3-D: 0• X-Z Plane: 1• Y-Z Plane: 2• X-Y Plane: 3• Constraint RZ: |
| `MASS` | 整数 | 否 | Mass Type• Lumped Mass: 1• Consistent Mass: 2 |
| `bMASSOFFSET` | 是/否（布尔值） | 否 | Consider Off-diagonal Masses |
| `bSELFWEIGHT` | 是/否（布尔值） | 否 | Convert Self-weight into Masses |
| `SMASS` | 整数 | 否 | Structure Mass Type• Convert to X, Y, Z: 1• Convert to X, Y: 2• Convert to Z: 3 |
| `GRAV` | 数字 | 否 | Gravity Acceleration |
| `TEMP` | 数字 | 否 | Initial Temperature |
| `bALIGNBEAM` | 是/否（布尔值） | 否 | Align Top of Beam Section |
| `bALIGNSLAB` | 是/否（布尔值） | 否 | Align the Top of the Slab (Plate) |
| `bROTRIGID` | 是/否（布尔值） | 否 | Considering Rotational Rigid Body Mode for Modal Participation Factor |

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "STYP": 0,
      "MASS": 1,
      "bMASSOFFSET": false,
      "bSELFWEIGHT": false,
      "GRAV": 9.806,
      "TEMP": 0,
      "bALIGNBEAM": false,
      "bALIGNSLAB": false,
      "bROTRIGID": false
    }
  }
}
```


---

### Structure Type — `/db/STYP-M1ᴴˢ⁾`

**方法**: GET, PUT, DELETE | **参数**: 5 必填 + 5 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `MASS_CONTROL` | 对象（一组键值对） | **是** | Mass Control Parameter |
| `MASS_TYPE` | string (enum) | **是** | Mass Type• Lumped Mass: LUMPED• Consistent Mass: CONSISTENT |
| `MASS_POS` | string (enum) | **是** | Mass Position• Consider Mass at the Centroid of Section: CENTROID• Consider Mass |
| `SELFWEIGHT` | 是/否（布尔值） | **是** | Convert Self-weight into Masses |
| `MASS_AXIS` | string (enum) | **是** | Convert to X, Y, Z / Convert to X, Y / Convert to Z• X, Y, Z: XYZ• X, Y: XY• Z:  |
| `STYPE` | string (enum) | 否 | Structure Type• 3-D: 3D• X-Z Plane: XZ• Y-Z Plane: YZ• X-Y Plane: XY• Constraint |
| `GRAV` | 数字 | 否 | Gravity Acceleration |
| `TEMP` | 数字 | 否 | Initial Temperature |
| `ALIGNBEAM` | 是/否（布尔值） | 否 | Align Top of Beam Section with Center Line (X-Y Plane) for Display |
| `ALIGNSLAB` | 是/否（布尔值） | 否 | Align Top of Slab(Plate) Section with Center Line (X-Y Plane) for Display |

**最简 JSON**：
```json
{
  "MASS_CONTROL": {},
  "MASS_TYPE": {},
  "MASS_POS": {},
  "SELFWEIGHT": true,
  "MASS_AXIS": {}
}
```


---

### Structure Group — `/db/GRUP`

**方法**: POST, GET, PUT | **参数**: 1 必填 + 3 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Structure Group Name |
| `P_TYPE` | 整数 | 否 | Plane Type |
| `N_LIST` | 整数数组 | 否 | Node List |
| `E_LIST` | 整数数组 | 否 | Element List |

**最简 JSON**：
```json
{
  "GRUP": {
    "NAME": "<NAME>"
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "NAME": "CENTER_",
      "P_TYPE": 0,
      "N_LIST": [
        1,
        2,
        3,
        4,
        5
      ],
      "E_LIST": [
        1,
        2,
        3,
        4,
        5
      ]
    }
  }
}
```


---

### Boundary Group — `/db/BNGR`

**方法**: POST, GET, PUT | **参数**: 1 必填 + 1 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Boundary Group Name |
| `AUTOTYPE` | 整数 | 否 | The Autogenerated boundary groups for CR/SH in a Composite Section¹⁾• Creep Boun |

**最简 JSON**：
```json
{
  "BNGR": {
    "NAME": "<NAME>"
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "NAME": "fix1",
      "AUTOTYPE": 0
    },
    "2": {
      "NAME": "fix2",
      "AUTOTYPE": 0
    },
    "3": {
      "NAME": "fix3",
      "AUTOTYPE": 0
    }
  }
}
```


---

## Load Group — `/db/LDGR`

**HTTP 方法**: POST, GET, PUT, DELETE | **参数总数**: 1（1 必填 + 0 可选）

### 1. 这是什么？（工程含义）

**Load Group** — 这是模型数据库的创建和查询操作，属于 Project 类别。

Load Group Name

> 简单说：这个接口用来**Load Group**。

### 2. JSON 结构（逐层解释）

下面按照从外到内的顺序解释每一层的 JSON 结构：

```json
{
  "LDGR": {
    "NAME": "<NAME>"
  }
}
```

**第 1 层：`LDGR`** — 1 个参数在这一层

- `"NAME"`: 文字（字符串） — Load Group Name


### 3. 必填 vs 可选参数

**必填参数**（不填会报错）：

| 参数名 | 类型 | JSON 路径 | 说明 |
|--------|------|-----------|------|
| `NAME` | 文字（字符串） | `LDGR.NAME` | Load Group Name |


### 6. 最小可运行代码

以下是能跑起来的最简代码：

```python
import requests
import urllib3
urllib3.disable_warnings()  # 关闭 SSL 警告

# MIDAS 服务地址（根据你的产品修改端口）
BASE = "https://127.0.0.1:1102"

url = f"{BASE}/db/LDGR"

# JSON 数据 — 这是你要发给 MIDAS 的内容
data = {
#     "LDGR": {
#         "NAME": "<NAME>"
#     }
# }

# 发送请求
r = requests.post(url, json=data, verify=False)

# 检查结果
if r.status_code == 200:
    print("成功！")
    print(r.json())
else:
    print(f"失败，错误码：{r.status_code}")
```

**运行前确认**：MIDAS Civil 已经打开，并且加载了一个项目。


### 7. 工程意义

参数化建模的核心。一旦掌握，你可以用几十行代码代替几小时的点鼠标操作。参数变化时，重新生成模型只需要几秒钟。

### 8. 常见错误

使用这个接口时最容易犯的错误：

1. **忘记填必填参数**：NAME 是必填的，漏掉任何一个都会报错。
4. **URL 写错**：确认路径是 `/db/LDGR`——多一个斜杠或少一个都会导致 404 错误。


### 9. Python 批量生成案例

如果你需要创建多个类似的调用（例如创建 100 个节点），可以用列表+循环来生成：

```python
import requests
import urllib3
urllib3.disable_warnings()

BASE = "https://127.0.0.1:1102"

# 定义基础数据模板
def make_data(**kwargs):
    """根据参数生成 Load Group 的 JSON 数据。"""
    data = {"LDGR": {"NAME": "<NAME>"}}
    # 在这里修改需要变化的值
    for key, value in kwargs.items():
        # 根据 json_path 更新对应位置的值
        pass  # 具体逻辑见下面的 for 循环例子
    return data

# 批量调用
results = []
for i in range(1, 11):  # 生成 10 个
    data = make_data()    # 在这里修改参数
    r = requests.post(f"{BASE}/db/LDGR", json=data, verify=False)
    results.append(r.json())
    print(f'第 {i} 个完成')
```


### 10. for 循环优化案例

对于批量操作，直接写 for 循环每次发一个请求效率不够高。以下是优化技巧：

**技巧 1：利用 Assign 结构一次发送多个对象**

很多 DB 接口支持在一次请求中发送多个对象，通过 `Assign` 下的编号 `"1"`, `"2"`, ... 区分。

```python
# ❌ 慢：循环 100 次，每次发一个节点
for i in range(100):
    data = {"Assign": {"1": {"X": i, "Y": 0, "Z": 0}}}
    requests.post(url, json=data, verify=False)

# ✅ 快：一次发 100 个节点
nodes = {}
for i in range(100):
    nodes[str(i+1)] = {"X": i, "Y": 0, "Z": 0}
data = {"Assign": nodes}
requests.post(url, json=data, verify=False)
```

**技巧 2：使用列表推导式预生成数据**（在 Load Group 中适用）

```python
# 列表推导式 — 一行代码生成所有节点的坐标
nodes = {str(i+1): {"X": i*5.0, "Y": 0, "Z": 0} for i in range(100)}
data = {"Assign": nodes}
requests.post(url, json=data, verify=False)
```

**通用优化原则**：

1. 能一次发多个就不要循环发单个
2. 用 `requests.Session()` 代替 `requests.post()` 做批量请求
3. 先生成所有数据，再统一发送，不要在循环里逐个生成+发送



---

### Tendon Group — `/db/TDGR`

**方法**: POST, GET, PUT, DELETE | **参数**: 1 必填 + 0 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Tendon Group Name |

**最简 JSON**：
```json
{
  "TDGR": {
    "NAME": "<NAME>"
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "NAME": "TGR1"
    },
    "2": {
      "NAME": "TGR2"
    }
  }
}
```


---

### Named Plane — `/db/NPLN`

**方法**: POST, GET, PUT, DELETE | **参数**: 4 必填 + 2 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Plane Name |
| `TYPE` | 整数 | **是** | Plane Type• 3 Points: 1• X-Y Plane: 2• X-Z Plane: 3• Y-Z Plane: 4 |
| `POINT` | 对象（一组键值对） | **是** | Point Data |
| `ITEM` | 数字数组 | **是** | Cutting location• 3 Points: 1st, 2nd, 3rd points• X-Y Plane: Z Position• X-Z Pla |
| `TOL` | 数字 | 否 | Tolerance |
| `COORD` | 数字 | 否 | Coordinates |

**最简 JSON**：
```json
{
  "NPLN": {
    "NAME": "<NAME>",
    "TYPE": 0,
    "POINT": {},
    "properties": {
      "POINT": {
        "items": {
          "properties": {
            "ITEM": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "NPLN": {
    "1": {
      "NAME": "NP11",
      "TYPE": 1,
      "TOL": 1,
      "POINT": [
        {
          "ITEM": [
            0,
            235,
            0
          ]
        },
        {
          "ITEM": [
            0,
            9710,
            0
          ]
        },
        {
          "ITEM": [
            15250,
            9710,
            0
          ]
        }
      ]
    },
    "2": {
      "NAME": "NP12",
      "TYPE": 2,
      "TOL": 1,
      "COORD": -12000
    }
  }
}
```


---

### Material Color — `/db/CO_M`

**方法**: GET, PUT | **参数**: 0 必填 + 11 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `W_R` | 整数 | 否 | Wire Frame Red |
| `W_G` | 整数 | 否 | Wire Frame Green |
| `W_B` | 整数 | 否 | Wire Frame Blue |
| `HF_R` | 整数 | 否 | Hidden Fill Red |
| `HF_G` | 整数 | 否 | Hidden Fill Green |
| `HF_B` | 整数 | 否 | Hidden Fill Blue |
| `HE_R` | 整数 | 否 | Hidden Edge Red |
| `HE_G` | 整数 | 否 | Hidden Edge Green |
| `HE_B` | 整数 | 否 | Hidden Edge Blue |
| `bBLEMD` | 是/否（布尔值） | 否 | Opacity Option |
| ... | ... | ... | *还有 1 个可选参数* |

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "W_R": 131,
      "W_G": 131,
      "W_B": 131,
      "HF_R": 178,
      "HF_G": 178,
      "HF_B": 178,
      "HE_R": 131,
      "HE_G": 131,
      "HE_B": 131,
      "bBLEMD": false,
      "FACT": 0.5
    }
  }
}
```


---

### Section Color — `/db/CO_S`

**方法**: GET, PUT | **参数**: 0 必填 + 11 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `W_R` | 整数 | 否 | Wire Frame Red |
| `W_G` | 整数 | 否 | Wire Frame Green |
| `W_B` | 整数 | 否 | Wire Frame Blue |
| `HF_R` | 整数 | 否 | Hidden Fill Red |
| `HF_G` | 整数 | 否 | Hidden Fill Green |
| `HF_B` | 整数 | 否 | Hidden Fill Blue |
| `HE_R` | 整数 | 否 | Hidden Edge Red |
| `HE_G` | 整数 | 否 | Hidden Edge Green |
| `HE_B` | 整数 | 否 | Hidden Edge Blue |
| `bBLEMD` | 是/否（布尔值） | 否 | Opacity Option |
| ... | ... | ... | *还有 1 个可选参数* |

**官方示例**：
```json
{
  "Assign": {
    "2": {
      "W_R": 111,
      "W_G": 142,
      "W_B": 91,
      "HF_R": 159,
      "HF_G": 205,
      "HF_B": 131,
      "HE_R": 111,
      "HE_G": 142,
      "HE_B": 91,
      "bBLEMD": false,
      "FACT": 0.5
    }
  }
}
```


---

### Thickness Color — `/db/CO_T`

**方法**: GET, PUT | **参数**: 0 必填 + 11 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `W_R` | 整数 | 否 | Wire Frame Red |
| `W_G` | 整数 | 否 | Wire Frame Green |
| `W_B` | 整数 | 否 | Wire Frame Blue |
| `HF_R` | 整数 | 否 | Hidden Fill Red |
| `HF_G` | 整数 | 否 | Hidden Fill Green |
| `HF_B` | 整数 | 否 | Hidden Fill Blue |
| `HE_R` | 整数 | 否 | Hidden Edge Red |
| `HE_G` | 整数 | 否 | Hidden Edge Green |
| `HE_B` | 整数 | 否 | Hidden Edge Blue |
| `bBLEMD` | 是/否（布尔值） | 否 | Opacity Option |
| ... | ... | ... | *还有 1 个可选参数* |

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "W_R": 111,
      "W_G": 142,
      "W_B": 91,
      "HF_R": 159,
      "HF_G": 205,
      "HF_B": 131,
      "HE_R": 111,
      "HE_G": 142,
      "HE_B": 91,
      "bBLEMD": false,
      "FACT": 0.5
    }
  }
}
```


---

### Floor Load Color — `/db/CO_F`

**方法**: GET, PUT | **参数**: 1 必填 + 14 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Floor Load Type Name |
| `WF_R` | 整数 | 否 | WireFrame_Red |
| `WF_G` | 整数 | 否 | WireFrame_Green |
| `WF_B` | 整数 | 否 | WireFrame_Blue |
| `HF_R` | 整数 | 否 | Hidden Fill Red |
| `HF_G` | 整数 | 否 | Hidden Fill Green |
| `HF_B` | 整数 | 否 | Hidden Fill Blue |
| `HE_R` | 整数 | 否 | Hidden Edge Red |
| `HE_G` | 整数 | 否 | Hidden Edge Green |
| `HE_B` | 整数 | 否 | Hidden Edge Blue |
| `OPT_BLEND` | 是/否（布尔值） | 否 | Blending Option |
| ... | ... | ... | *还有 4 个可选参数* |

**最简 JSON**：
```json
{
  "CO_F": {
    "NAME": "<NAME>"
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "NAME": "FL",
      "WF_R": 166,
      "WF_G": 202,
      "WF_B": 240,
      "HF_R": 166,
      "HF_G": 202,
      "HF_B": 240,
      "HE_R": 166,
      "HE_G": 202,
      "HE_B": 240,
      "OPT_BLEND": true,
      "BLEND_FACTOR": 0.25
    }
  }
}
```


---

### Span Information — `/db/SPAN`

**方法**: POST, GET, PUT, DELETE | **参数**: 8 必填 + 0 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Span Name |
| `bEXACTSPAN` | 是/否（布尔值） | **是** | Exact Span Option |
| `DIRECTION` | 整数 | **是** | Inner Direction of Multiple Girders• (-) Local y: 0• (+) Local y: 1• Both: 2• No |
| `SECTTYPE` | 整数 | **是** | Assign Elements• By Selection: 0• Number: 1 |
| `SPAN_LIST` | 数字 | **是** | Span by Element Length |
| `SPAN_BASE_ITEMS` | 对象（一组键值对） | **是** | Span Items |
| `ELEM_KEY` | 整数 | **是** | Element Number |
| `SUPPORT` | 整数 | **是** | Support Location• None: 0• I: 1• J: 2 |

**最简 JSON**：
```json
{
  "SPAN": {
    "NAME": "<NAME>",
    "bEXACTSPAN": true,
    "DIRECTION": 0,
    "SECTTYPE": 0,
    "SPAN_LIST": 0,
    "SPAN_BASE_ITEMS": {},
    "properties": {
      "SPAN_BASE_ITEMS": {
        "items": {
          "properties": {
            "ELEM_KEY": 0,
            "SUPPORT": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "NAME": "s1",
      "bEXACTSPAN": true,
      "DIRECTION": 0,
      "SECTTYPE": 0,
      "SPAN_LIST": [
        2.5,
        5,
        32.5
      ],
      "SPAN_BASE_ITEMS": [
        {
          "ELEM_KEY": 1,
          "SUPPORT": 1
        },
        {
          "ELEM_KEY": 2,
          "SUPPORT": 1
        },
        {
          "ELEM_KEY": 3,
          "SUPPORT": 2
        },
        {
          "ELEM_KEY": 4,
          "SUPPORT": 0
        },
        {
          "ELEM_KEY": 5,
          "SUPPORT": 0
        },
        {
          "ELEM_KEY": 6,
          "SUPPORT": 0
        },
        {
          "ELEM_KEY": 7,
          "SUPPORT": 0
        },
        {
          "ELEM_KEY": 8,
          "SUPPORT": 0
        },
        {
          "ELEM_KEY": 9,
          "SUPPORT": 0
        },
        {
          "ELEM_KEY": 10,
          "SUPPORT": 0
        },
        {
          "ELEM_KEY": 11,
          "SUPPORT": 0
        },
        {
          "ELEM_KEY": 12,
          "SUPPORT": 0
        },
        {
          "ELEM_KEY": 13,
          "SUPPORT": 0
        },
        {
          "ELEM_KEY": 14,
          "SUPPORT": 0
        },
        {
          "ELEM_KEY": 15,
          "SUPPORT": 0
        },
        {
          "ELEM_KEY": 16,
          "SUPPORT": 2
        }
      ]
    }
  }
}
```


---

### Story Data — `/db/STOR`

**方法**: POST, GET, PUT, DELETE | **参数**: 15 必填 + 0 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `STORY_NAME` | 文字（字符串） | **是** | Story Name |
| `STORY_LEVEL` | 数字 | **是** | Story height (elevation) |
| `bFLOOR_DIAPHRAGM` | 是/否（布尔值） | **是** | whether a floor at a given story level is assumed to act as arigid diaphragmin l |
| `WIND_FLOOR_WIDTH_X` | 数字 | **是** | Effective width of the building in X-axis, subjected to GCS Y-direction wind loa |
| `WIND_FLOOR_WIDTH_Y` | 数字 | **是** | Effective width of the building in Y-axis, subjected to GCS X-direction wind loa |
| `WIND_CENTER_X` | 数字 | **是** | Coordinate of the position in GCS X-direction, to which the wind load is applied |
| `WIND_CENTER_Y` | 数字 | **是** | Coordinate of the position in GCS Y-direction, to which the wind load is applied |
| `WIND_ECCENT_X` | 数字 | **是** | Eccentricity distance in X-direction at each story in GCS Y-direction wind load |
| `WIND_ECCENT_Y` | 数字 | **是** | Eccentricity distance in Y-direction at each story in GCS X-direction wind load |
| `SEIS_ACC_ECCENT_X` | 数字 | **是** | Accidental eccentricity distance in X-direction due to the seismic loads at each |
| `SEIS_ACC_ECCENT_Y` | 数字 | **是** | Accidental eccentricity distance in Y-direction due to the seismic loads at each |
| `SEIS_INHERENT_ECCENT_X` | 数字 | **是** | Inherent eccentricity distance in X-direction due to the seismic loads at each s |
| `SEIS_INHERENT_ECCENT_Y` | 数字 | **是** | Inherent eccentricity distance in Y-direction due to the seismic loads at each s |
| `SEIS_TORSIONAL_AMP_FACTOR_X` | 数字 | **是** | Seismic Torsional Amplification Factor in X-direction |
| `SEIS_TORSIONAL_AMP_FACTOR_Y` | 数字 | **是** | Seismic Torsional Amplification Factor in Y-direction |

**最简 JSON**：
```json
{
  "Argument": {
    "STORY_NAME": "<STORY_NAME>",
    "STORY_LEVEL": 0,
    "bFLOOR_DIAPHRAGM": true,
    "WIND_FLOOR_WIDTH_X": 0,
    "WIND_FLOOR_WIDTH_Y": 0,
    "WIND_CENTER_X": 0,
    "WIND_CENTER_Y": 0,
    "WIND_ECCENT_X": 0,
    "WIND_ECCENT_Y": 0,
    "SEIS_ACC_ECCENT_X": 0,
    "SEIS_ACC_ECCENT_Y": 0,
    "SEIS_INHERENT_ECCENT_X": 0,
    "SEIS_INHERENT_ECCENT_Y": 0,
    "SEIS_TORSIONAL_AMP_FACTOR_X": 0,
    "SEIS_TORSIONAL_AMP_FACTOR_Y": 0
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "STORY_NAME": "1F",
      "STORY_LEVEL": 0,
      "bFLOOR_DIAPHRAGM": false,
      "WIND_FLOOR_WIDTH_X": 36,
      "WIND_FLOOR_WIDTH_Y": 27.6,
      "WIND_CENTER_X": 18,
      "WIND_CENTER_Y": 13.8,
      "WIND_ECCENT_X": 5.4,
      "WIND_ECCENT_Y": 4.14,
      "SEIS_ACC_ECCENT_X": 1.8,
      "SEIS_ACC_ECCENT_Y": 1.38,
      "SEIS_INHERENT_ECCENT_X": 0,
      "SEIS_INHERENT_ECCENT_Y": 0,
      "SEIS_TORSIONAL_AMP_FACTOR_X": 1,
      "SEIS_TORSIONAL_AMP_FACTOR_Y": 1
    },
    "2": {
      "STORY_NAME": "2F",
      "STORY_LEVEL": 5,
      "bFLOOR_DIAPHRAGM": true,
      "WIND_FLOOR_WIDTH_X": 36,
      "WIND_FLOOR_WIDTH_Y": 29.1,
      "WIND_CENTER_X": 18,
      "WIND_CENTER_Y": 14.55,
      "WIND_ECCENT_X": 5.4,
      "WIND_ECCENT_Y": 4.365,
      "SEIS_ACC_ECCENT_X": 1.8,
      "SEIS_ACC_ECCENT_Y": 1.455,
      "SEIS_INHERENT_ECCENT_X": 0,
      "SEIS_INHERENT_ECCENT_Y": 0,
      "SEIS_TORSIONAL_AMP_FACTOR_X": 1,
      "SEIS_TORSIONAL_AMP_FACTOR_Y": 1
    },
    "3": {
      "STORY_NAME": "3F",
      "STORY_LEVEL": 9.5,
      "bFLOOR_DIAPHRAGM": true,
      "WIND_FLOOR_WIDTH_X": 36,
      "WIND_FLOOR_WIDTH_Y": 29.1,
      "WIND_CENTER_X": 18,
      "WIND_CENTER_Y": 14.55,
      "WIND_ECCENT_X": 5.4,
      "WIND_ECCENT_Y": 4.365,
      "SEIS_ACC_ECCENT_X": 1.8,
      "SEIS_ACC_ECCENT_Y": 1.455,
      "SEIS_INHERENT_ECCENT_X": 0,
      "SEIS_INHERENT_ECCENT_Y": 0,
      "SEIS_TORSIONAL_AMP_FACTOR_X": 1,
      "SEIS_TORSIONAL_AMP_FACTOR_Y": 1
    },
    "4": {
      "STORY_NAME": "4F",
      "STORY_LEVEL": 14,
      "bFLOOR_DIAPHRAGM": true,
      "WIND_FLOOR_WIDTH_X": 36,
      "WIND_FLOOR_WIDTH_Y": 29.1,
      "WIND_CENTER_X": 18,
      "WIND_CENTER_Y": 14.55,
      "WIND_ECCENT_X": 5.4,
      "WIND_ECCENT_Y": 4.365,
      "SEIS_ACC_ECCENT_X": 1.8,
      "SEIS_ACC_ECCENT_Y": 1.455,
      "SEIS_INHERENT_ECCENT_X": 0,
      "SEIS_INHERENT_ECCENT_Y": 0,
      "SEIS_TORSIONAL_AMP_FACTOR_X": 1,
      "SEIS_TORSIONAL_AMP_FACTOR_Y": 1
    },
    "5": {
      "STORY_NAME": "5F",
      "STORY_LEVEL": 18,
      "bFLOOR_DIAPHRAGM": true,
      "WIND_FLOOR_WIDTH_X": 36,
      "WIND_FLOOR_WIDTH_Y": 29.1,
      "WIND_CENTER_X": 18,
      "WIND_CENTER_Y": 14.55,
      "WIND_ECCENT_X": 5.4,
      "WIND_ECCENT_Y": 4.365,
      "SEIS_ACC_ECCENT_X": 1.8,
      "SEIS_ACC_ECCENT_Y": 1.455,
      "SEIS_INHERENT_ECCENT_X": 0,
      "SEIS_INHERENT_ECCENT_Y": 0,
      "SEIS_TORSIONAL_AMP_FACTOR_X": 1,
      "SEIS_TORSIONAL_AMP_FACTOR_Y": 1
    },
    "6": {
      "STORY_NAME": "6F",
      "STORY_LEVEL": 22,
      "bFLOOR_DIAPHRAGM": true,
      "WIND_FLOOR_WIDTH_X": 36,
      "WIND_FLOOR_WIDTH_Y": 29.1,
      "WIND_CENTER_X": 18,
      "WIND_CENTER_Y": 14.55,
      "WIND_ECCENT_X": 5.4,
      "WIND_ECCENT_Y": 4.365,
      "SEIS_ACC_ECCENT_X": 1.8,
      "SEIS_ACC_ECCENT_Y": 1.455,
      "SEIS_INHERENT_ECCENT_X": 0,
      "SEIS_INHERENT_ECCENT_Y": 0,
      "SEIS_TORSIONAL_AMP_FACTOR_X": 1,
      "SEIS_TORSIONAL_AMP_FACTOR_Y": 1
    },
    "7": {
      "STORY_NAME": "7F",
      "STORY_LEVEL": 26,
      "bFLOOR_DIAPHRAGM": true,
      "WIND_FLOOR_WIDTH_X": 36,
      "WIND_FLOOR_WIDTH_Y": 29.1,
      "WIND_CENTER_X": 18,
      "WIND_CENTER_Y": 14.55,
      "WIND_ECCENT_X": 5.4,
      "WIND_ECCENT_Y": 4.365,
      "SEIS_ACC_ECCENT_X": 1.8,
      "SEIS_ACC_ECCENT_Y": 1.455,
      "SEIS_INHERENT_ECCENT_X": 0,
      "SEIS_INHERENT_ECCENT_Y": 0,
      "SEIS_TORSIONAL_AMP_FACTOR_X": 1,
      "SEIS_TORSIONAL_AMP_FACTOR_Y": 1
    },
    "8": {
      "STORY_NAME": "8F",
      "STORY_LEVEL": 30,
      "bFLOOR_DIAPHRAGM": true,
      "WIND_FLOOR_WIDTH_X": 36,
      "WIND_FLOOR_WIDTH_Y": 29.1,
      "WIND_CENTER_X": 18,
      "WIND_CENTER_Y": 14.55,
      "WIND_ECCENT_X": 5.4,
      "WIND_ECCENT_Y": 4.365,
      "SEIS_ACC_ECCENT_X": 1.8,
      "SEIS_ACC_ECCENT_Y": 1.455,
      "SEIS_INHERENT_ECCENT_X": 0,
      "SEIS_INHERENT_ECCENT_Y": 0,
      "SEIS_TORSIONAL_AMP_FACTOR_X": 1,
      "SEIS_TORSIONAL_AMP_FACTOR_Y": 1
    },
    "9": {
      "STORY_NAME": "9F",
      "STORY_LEVEL": 34,
      "bFLOOR_DIAPHRAGM": true,
      "WIND_FLOOR_WIDTH_X": 36,
      "WIND_FLOOR_WIDTH_Y": 29.1,
      "WIND_CENTER_X": 18,
      "WIND_CENTER_Y": 14.55,
      "WIND_ECCENT_X": 5.4,
      "WIND_ECCENT_Y": 4.365,
      "SEIS_ACC_ECCENT_X": 1.8,
      "SEIS_ACC_ECCENT_Y": 1.455,
      "SEIS_INHERENT_ECCENT_X": 0,
      "SEIS_INHERENT_ECCENT_Y": 0,
      "SEIS_TORSIONAL_AMP_FACTOR_X": 1,
      "SEIS_TORSIONAL_AMP_FACTOR_Y": 1
    },
    "10": {
      "STORY_NAME": "10F",
      "STORY_LEVEL": 38,
      "bFLOOR_DIAPHRAGM": true,
      "WIND_FLOOR_WIDTH_X": 36,
      "WIND_FLOOR_WIDTH_Y": 29.1,
      "WIND_CENTER_X": 18,
      "WIND_CENTER_Y": 14.55,
      "WIND_ECCENT_X": 5.4,
      "WIND_ECCENT_Y": 4.365,
      "SEIS_ACC_ECCENT_X": 1.8,
      "SEIS_ACC_ECCENT_Y": 1.455,
      "SEIS_INHERENT_ECCENT_X": 0,
      "SEIS_INHERENT_ECCENT_Y": 0,
      "SEIS_TORSIONAL_AMP_FACTOR_X": 1,
      "SEIS_TORSIONAL_AMP_FACTOR_Y": 1
    },
    "11": {
      "STORY_NAME": "11F",
      "STORY_LEVEL": 42,
      "bFLOOR_DIAPHRAGM": true,
      "WIND_FLOOR_WIDTH_X": 36,
      "WIND_FLOOR_WIDTH_Y": 29.1,
      "WIND_CENTER_X": 18,
      "WIND_CENTER_Y": 14.55,
      "WIND_ECCENT_X": 5.4,
      "WIND_ECCENT_Y": 4.365,
      "SEIS_ACC_ECCENT_X": 1.8,
      "SEIS_ACC_ECCENT_Y": 1.455,
      "SEIS_INHERENT_ECCENT_X": 0,
      "SEIS_INHERENT_ECCENT_Y": 0,
      "SEIS_TORSIONAL_AMP_FACTOR_X": 1,
      "SEIS_TORSIONAL_AMP_FACTOR_Y": 1
    },
    "12": {
      "STORY_NAME": "12F",
      "STORY_LEVEL": 46,
      "bFLOOR_DIAPHRAGM": true,
      "WIND_FLOOR_WIDTH_X": 36,
      "WIND_FLOOR_WIDTH_Y": 29.1,
      "WIND_CENTER_X": 18,
      "WIND_CENTER_Y": 14.55,
      "WIND_ECCENT_X": 5.4,
      "WIND_ECCENT_Y": 4.365,
      "SEIS_ACC_ECCENT_X": 1.8,
      "SEIS_ACC_ECCENT_Y": 1.455,
      "SEIS_INHERENT_ECCENT_X": 0,
      "SEIS_INHERENT_ECCENT_Y": 0,
      "SEIS_TORSIONAL_AMP_FACTOR_X": 1,
      "SEIS_TORSIONAL_AMP_FACTOR_Y": 1
    },
    "13": {
      "STORY_NAME": "Roof",
      "STORY_LEVEL": 50,
      "bFLOOR_DIAPHRAGM": true,
      "WIND_FLOOR_WIDTH_X": 36,
      "WIND_FLOOR_WIDTH_Y": 29.1,
      "WIND_CENTER_X": 18,
      "WIND_CENTER_Y": 14.55,
      "WIND_ECCENT_X": 5.4,
      "WIND_ECCENT_Y": 4.365,
      "SEIS_ACC_ECCENT_X": 1.8,
      "SEIS_ACC_ECCENT_Y": 1.455,
      "SEIS_INHERENT_ECCENT_X": 0,
      "SEIS_INHERENT_ECCENT_Y": 0,
      "SEIS_TORSIONAL_AMP_FACTOR_X": 1,
      "SEIS_TORSIONAL_AMP_FACTOR_Y": 1
    }
  }
}
```


---

### Node — `/db/NODE`

**方法**: POST, GET, PUT, DELETE | **参数**: 0 必填 + 3 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `X` | 数字 | 否 | Coordinates - x |
| `Y` | 数字 | 否 | Coordinates - y |
| `Z` | 数字 | 否 | Coordinates - z |

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "X": -1,
      "Y": -1,
      "Z": -1
    },
    "2": {
      "X": -2,
      "Y": -2,
      "Z": -2
    },
    "3": {
      "X": -3,
      "Y": -3,
      "Z": -3
    }
  }
}
```


---

### Element — `/db/ELEM`

**方法**: POST, GET, PUT, DELETE | **参数**: 7 必填 + 9 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `MATL` | 整数 | **是** | Material No. |
| `SECT` | 整数 | **是** | Section / Thickness No. |
| `NODE` | 整数数组 | **是** | Node No.²⁾ |
| `STYPE` | 整数 | **是** | Element Subtype• with Drilling DOF Inactive: 1• with Drilling DOF Active: 2 |
| `CABLE` | 整数 | **是** | Cable Type• Pretension: 1• Horizontal: 2• Lu: 3 |
| `WALL` | 整数 | **是** | Wall ID |
| `W_CON` | 整数 | **是** | Orientation (Wall Beta Angle Only)• Beta Angle: 0• Ref Point: 1• Ref Vector: 2 |
| `TYPE` | 文字（字符串） | 否 | Element Type¹⁾ |
| `ANGLE` | 数字 | 否 | Beta Angle |
| `TENS` | 数字 | 否 | Allowable Tension• Positive Value Only |
| `T_LIMIT` | 数字 | 否 | Compression Limit value• Negative Value Only |
| `T_bLMT` | 是/否（布尔值） | 否 | Compression Limit |
| `NON_LEN` | 数字 | 否 | Gap |
| `C_RAT` | 数字 | 否 | CABLELENGTHRATIO |
| `W_TYPE` | 整数 | 否 | Wall Type• Plate base: 0• CRB - Pin: 1• CRB - Fixed: 2 |
| `LCAXIS` | 整数 | 否 | LOCALAXIS |

**最简 JSON**：
```json
{
  "ELEM": {
    "MATL": 0,
    "SECT": 0,
    "NODE": 0,
    "STYPE": 0,
    "CABLE": 0,
    "WALL": 0,
    "W_CON": 0
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "198": {
      "TYPE": "BEAM",
      "MATL": 1,
      "SECT": 1,
      "NODE": [
        30,
        74
      ],
      "ANGLE": 0
    }
  }
}
```


---

### Node Local Axis — `/db/SKEW`

**方法**: POST, GET, PUT, DELETE | **参数**: 3 必填 + 28 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `REFTYPE` | 整数 | **是** | Reference Type• Ref. Point: 1Required P0, P1 Point• Global Direction: 2Required  |
| `G_DIR` | 整数 | **是** | Global Direction• Global X: 0• Global Y: 1• Global Z: 2 |
| `L_DIR` | 整数 | **是** | Local Direction• Local x: 0• Local y: 1• Local z: 2 |
| `iMETHOD` | 整数 | 否 | Input Method• Angle: 1• 3 points: 2• Vector: 3• Line Vector: 4 |
| `ANGLE_X` | 数字 | 否 | About x |
| `ANGLE_Y` | 数字 | 否 | About y |
| `ANGLE_Z` | 数字 | 否 | About z |
| `P0X` | 数字 | 否 | P0 Coordinate - X |
| `P0Y` | 数字 | 否 | P0 Coordinate - Y |
| `P0Z` | 数字 | 否 | P0 Coordinate - Z |
| `P1X` | 数字 | 否 | P1 Coordinate - X |
| `P1Y` | 数字 | 否 | P1 Coordinate - Y |
| `P1Z` | 数字 | 否 | P1 Coordinate - Z |
| ... | ... | ... | *还有 18 个可选参数* |

**最简 JSON**：
```json
{
  "SKEW": {
    "REFTYPE": 0,
    "G_DIR": 0,
    "L_DIR": 0
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "iMETHOD": 1,
      "ANGLE_X": 45,
      "ANGLE_Y": 0,
      "ANGLE_Z": 90
    }
  }
}
```


---

### Define Domain — `/db/MADO`

**方法**: POST, GET, PUT, DELETE | **参数**: 5 必填 + 0 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Domain Name |
| `TYPE` | 整数 | **是** | Element Type• Plane Stress: 3• Plate: 4• Plane Strain: 6• Axisymmetric: 7 |
| `MATL` | 整数 | **是** | Material ID |
| `PROP` | 整数 | **是** | Element Property |
| `SUB_TYPE` | 整数 | **是** | Sub Type |

**最简 JSON**：
```json
{
  "MADO": {
    "NAME": "<NAME>",
    "TYPE": 0,
    "MATL": 0,
    "PROP": 0,
    "SUB_TYPE": 0
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "NAME": "DM1",
      "TYPE": 4,
      "MATL": 0,
      "PROP": 0,
      "SUB_TYPE": 2
    }
  }
}
```


---

### Define Sub-Domain — `/db/SBDO`

**方法**: POST, GET, PUT, DELETE | **参数**: 8 必填 + 14 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `SUB_DOMAIN_NAME` | 文字（字符串） | **是** | Sub Domain Name |
| `MEMBER_TYPE` | 整数 | **是** | Member Type• None: 0• Slab: 1• Mat: 2 |
| `V1` | 数字 | **是** | Rebar Dir.1 |
| `V2` | 数字 | **是** | Rebar Dir.2 |
| `DOMAIN_NAME` | 文字（字符串） | **是** | Domain Name |
| `bUseMt` | 是/否（布尔值） | **是** | Use Mt |
| `THICKNESS` | 数字 | **是** | Thickness |
| `MEMB_TYPE_CIVIL` | 整数 | **是** | Member Type Civil• None: 0• Plate Beam (1D): 1• Plate Column (1D): 2• Shell: 3 |
| `OPT_BASIC_REBAR` | 是/否（布尔值） | 否 | Basic Rebar Option |
| `TOP_REBAR_NAME_X` | 文字（字符串） | 否 | Top Rebar Name (X-Dir)• When the Basic Rebar is True |
| `TOP_REBAR_SPACE_X` | 数字 | 否 | Top Rebar Space (X-Dir)• When the Basic Rebar is True |
| `BOTTOM_REBAR_NAME_X` | 文字（字符串） | 否 | Bottom Rebar Name (X-Dir)• When the Basic Rebar is True |
| `BOTTOM_REBAR_SPACE_X` | 数字 | 否 | Bottom Rebar Space (X-Dir)• When the Basic Rebar is True |
| `TOP_REBAR_NAME_Y` | 文字（字符串） | 否 | Top Rebar Name (Y-Dir)• When the Basic Rebar is True |
| `TOP_REBAR_SPACE_Y` | 数字 | 否 | Top Rebar Space (Y-Dir)• When the Basic Rebar is True |
| `BOTTOM_REBAR_NAME_Y` | 文字（字符串） | 否 | Bottom Rebar Name (Y-Dir)• When the Basic Rebar is True |
| `BOTTOM_REBAR_SPACE_Y` | 数字 | 否 | Bottom Rebar Space (Y-Dir)• When the Basic Rebar is True |
| `AXIS_VECTOR` | 数字 | 否 | Axis Vector• When the Rebar Direction is Reference Axis |
| ... | ... | ... | *还有 4 个可选参数* |

**最简 JSON**：
```json
{
  "SBDO": {
    "SUB_DOMAIN_NAME": "<SUB_DOMAIN_NAME>",
    "MEMBER_TYPE": 0,
    "V1": 0,
    "V2": 0,
    "DOMAIN_NAME": "<DOMAIN_NAME>",
    "bUseMt": true,
    "THICKNESS": 0,
    "MEMB_TYPE_CIVIL": 0
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "SUB_DOMAIN_NAME": "SDM1",
      "MEMBER_TYPE": 1,
      "V1": 0,
      "V2": 90,
      "DOMAIN_NAME": "DM1",
      "AXIS_VECTOR": [
        0,
        0,
        0,
        0,
        0,
        0
      ],
      "bUseMt": true,
      "STR_UCS": "",
      "MEMB_TYPE_CIVIL": 1
    }
  }
}
```


---

### Domain-Element — `/db/DOEL`

**方法**: POST, GET, PUT, DELETE | **参数**: 3 必填 + 0 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TYPE` | 整数 | **是** | Domain Type• Main-Domain: 0• Sub-Domain: 1 |
| `KEY_DOMAIN` | 整数 | **是** | Key Domain |
| `MAIN_DOMAIN_NAME` | 文字（字符串） | **是** | Main Domain Name |

**最简 JSON**：
```json
{
  "DOEL": {
    "TYPE": 0,
    "KEY_DOMAIN": 0,
    "MAIN_DOMAIN_NAME": "<MAIN_DOMAIN_NAME>"
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "163": {
      "TYPE": 1,
      "KEY_DOMAIN": 1,
      "MAIN_DOMAIN_NAME": "DM1"
    },
    "164": {
      "TYPE": 1,
      "KEY_DOMAIN": 1,
      "MAIN_DOMAIN_NAME": "DM1"
    },
    "165": {
      "TYPE": 0,
      "KEY_DOMAIN": 1,
      "MAIN_DOMAIN_NAME": "DM1"
    },
    "170": {
      "TYPE": 0,
      "KEY_DOMAIN": 1,
      "MAIN_DOMAIN_NAME": "DM1"
    },
    "171": {
      "TYPE": 0,
      "KEY_DOMAIN": 1,
      "MAIN_DOMAIN_NAME": "DM1"
    },
    "172": {
      "TYPE": 0,
      "KEY_DOMAIN": 1,
      "MAIN_DOMAIN_NAME": "DM1"
    }
  }
}
```


---

### Material Properties — `/db/MATL`

**方法**: POST, GET, PUT, DELETE | **参数**: 15 必填 + 8 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TYPE` | 文字（字符串） | **是** | Material Type• Concrete: "CONC"• Steel: "STEEL"• SRC: "SRC"• Aluminum: "ALUMINUM |
| `NAME` | 文字（字符串） | **是** | Material Name |
| `PARAM` | 对象（一组键值对） | **是** | Material Parameter |
| `P_TYPE` | 整数 | **是** | Material Type• Standard: 1• Isotropic: 2• Orthotropic: 3 |
| `STANDARD` | 文字（字符串） | **是** | Standard Name |
| `DB` | 文字（字符串） | **是** | DB Name |
| `ELAST` | 数字 | **是** | Modulus of Elasticity |
| `POISN` | 数字 | **是** | Poisson’s Ratio |
| `THERMAL` | 数字 | **是** | Thermal Coefficient |
| `DEN` | 数字 | **是** | Weight of Density |
| `MASS` | 数字 | **是** | Mass Density |
| `ELAST_M` | 数字数组 | **是** | Modulus of Elasticity |
| `POISN_M` | 数字数组 | **是** | Poisson’s Ratio |
| `THERMAL_M` | 数字数组 | **是** | Thermal Coefficient |
| `SHEAR_M` | 数字数组 | **是** | Shear Modulus |
| `HE_SPEC` | 数字 | 否 | Specific heat |
| `HE_COND` | 数字 | 否 | Heat Conduction |
| `PLMT` | 整数 | 否 | Plastic Material No. |
| `P_NAME` | 文字（字符串） | 否 | Plastic Material Name |
| `bMASS_DENS` | 是/否（布尔值） | 否 | Use Mass Density |
| `DAMP_RAT` | 数字 | 否 | Damping Ratio |
| `CODE` | 文字（字符串） | 否 | Code Name |
| `bELAST` | 是/否（布尔值） | 否 | Youngs Modulus for User Define Option• JTG3362-18(S) |

**最简 JSON**：
```json
{
  "MATL": {
    "TYPE": "<TYPE>",
    "NAME": "<NAME>",
    "PARAM": {},
    "properties": {
      "PARAM": {
        "items": {
          "properties": {
            "P_TYPE": 0,
            "STANDARD": "<STANDARD>",
            "DB": "<DB>",
            "ELAST": 0,
            "POISN": 0,
            "THERMAL": 0,
            "DEN": 0,
            "MASS": 0,
            "ELAST_M": 0,
            "POISN_M": 0,
            "THERMAL_M": 0,
            "SHEAR_M": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "TYPE": "STEEL",
      "NAME": "DB_Steel",
      "HE_SPEC": 0,
      "HE_COND": 0,
      "PLMT": 0,
      "P_NAME": "",
      "bMASS_DENS": false,
      "DAMP_RAT": 0.02,
      "PARAM": [
        {
          "P_TYPE": 1,
          "STANDARD": "EN05(S)",
          "CODE": "",
          "DB": "S450",
          "bELAST": false,
          "ELAST": 210000000
        }
      ]
    },
    "2": {
      "TYPE": "CONC",
      "NAME": "DB_Conc",
      "HE_SPEC": 0,
      "HE_COND": 0,
      "PLMT": 0,
      "P_NAME": "",
      "bMASS_DENS": false,
      "DAMP_RAT": 0.05,
      "PARAM": [
        {
          "P_TYPE": 1,
          "STANDARD": "EN04(RC)",
          "CODE": "",
          "DB": "C40/50",
          "bELAST": false,
          "ELAST": 35220000
        }
      ]
    },
    "3": {
      "TYPE": "SRC",
      "NAME": "DB_SRC",
      "HE_SPEC": 0,
      "HE_COND": 0,
      "PLMT": 0,
      "P_NAME": "",
      "bMASS_DENS": false,
      "DAMP_RAT": 0.05,
      "PARAM": [
        {
          "P_TYPE": 1,
          "STANDARD": "EN05(S)",
          "CODE": "",
          "DB": "S450",
          "bELAST": false,
          "ELAST": 210000000
        },
        {
          "P_TYPE": 1,
          "STANDARD": "EN04(RC)",
          "CODE": "",
          "DB": "C40/50",
          "bELAST": false,
          "ELAST": 35220000
        }
      ]
    },
    "4": {
      "TYPE": "USER",
      "NAME": "DB_User",
      "HE_SPEC": 0,
      "HE_COND": 0,
      "PLMT": 0,
      "P_NAME": "",
      "bMASS_DENS": false,
      "DAMP_RAT": 0,
      "PARAM": [
        {
          "P_TYPE": 1,
          "STANDARD": "BS04(S)",
          "CODE": "",
          "DB": "S460",
          "bELAST": false,
          "ELAST": 205000000
        }
      ]
    }
  }
}
```


---

### Material Properties — `/db/MATL-M1ᴴˢ⁾`

**方法**: POST, GET, PUT, DELETE | **参数**: 8 必填 + 15 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `MATL_NAME` | 文字（字符串） | **是** | Name |
| `MATL_TYPE` | string (enum) | **是** | Type of Design• Steel: STEEL• Concrete: CONC• SRC: SRC• User: USER |
| `PARAM` | array [object] | **是** | PARAMWhenMATL_TYPEis "SRC", enter both Concrete and Steel inputs. |
| `P_TYPE` | integer (enum) | **是** | Isotropic / Orthotropic• Standard: 0• Isotropic User Defined: 1• Orthotropic Use |
| `STANDARD` | 文字（字符串） | **是** | Standard |
| `DB` | 文字（字符串） | **是** | DB |
| `USER_DEFINED` | 对象（一组键值对） | **是** | USER_DEFINED |
| `MASS` | 数字 | **是** | Mass Density |
| `CODE` | 文字（字符串） | 否 | Code |
| `bELAST` | 数字 | 否 | Modulus of Elasticity |
| `POISN` | 数字 | 否 | Poisson's Ratio |
| `THERMAL` | 数字 | 否 | Thermal Coefficient |
| `DEN` | 数字 | 否 | Weight Density |
| `bMASS_DENS` | 是/否（布尔值） | 否 | Use Mass Density |
| `ELAST_M` | Array | 否 | Modulus of Elasticity |
| `THERMAL_M` | Array | 否 | Thermal Coefficient |
| `SHEAR_M` | Array | 否 | Shear Modulus |
| `POISN_M` | Array | 否 | Poisson's Ratio |
| ... | ... | ... | *还有 5 个可选参数* |

**最简 JSON**：
```json
{
  "MATL_NAME": "<MATL_NAME>",
  "MATL_TYPE": {},
  "PARAM": [],
  "P_TYPE": {},
  "STANDARD": "<STANDARD>",
  "DB": "<DB>",
  "USER_DEFINED": {},
  "MASS": 0
}
```


---

### Inelastic Material Properties for Fiber Model — `/db/IMFM`

**方法**: POST, GET, PUT, DELETE | **参数**: 0 必填 + 4 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `CONC_NAME` | 文字（字符串） | 否 | Inelastic Material of Concrete |
| `CONFINED_CONC_NAME` | 文字（字符串） | 否 | Confined Concrete for Columns |
| `REBAR_NAME` | 文字（字符串） | 否 | Inelastic Material of Rebar |
| `STEEL_NAME` | 文字（字符串） | 否 | Inelastic Material of Steel |

**官方示例**：
```json
{
  "Assign": {
    "7": {
      "STEEL_NAME": "Inealstic_Steel"
    },
    "8": {
      "CONC_NAME": "Inelastic_Conc",
      "CONFINED_CONC_NAME": "Inelastic_Conc",
      "REBAR_NAME": "Inealstic_Steel"
    }
  }
}
```


---

### Inelastic Material Link for Auto Generation — `/db/IMFM-M1ᴴˢ⁾`

**方法**: POST, GET, PUT, DELETE | **参数**: 3 必填 + 3 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `UN_CONC_NAME` | 文字（字符串） | **是** | Inelastic Material Property - Unconfined Concrete |
| `REBAR_NAME` | 文字（字符串） | **是** | Inelastic Material Property -Rebar |
| `STEEL_NAME` | 文字（字符串） | **是** | Inelastic Material Property -Steel |
| `CONCRETE` | 对象（一组键值对） | 否 | Material Type - Concrete |
| `CONF_CONC_NAME` | 文字（字符串） | 否 | Inelastic Material Property -Confined Concrete |
| `STEEL` | 对象（一组键值对） | 否 | Material Type - STEEL |

**最简 JSON**：
```json
{
  "UN_CONC_NAME": "<UN_CONC_NAME>",
  "REBAR_NAME": "<REBAR_NAME>",
  "STEEL_NAME": "<STEEL_NAME>"
}
```


---

### Time Dependent Material Properties - User Defined — `/db/TDMF`

**方法**: POST, GET, PUT, DELETE | **参数**: 8 必填 + 2 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Material Function Name |
| `FTYPE` | 文字（字符串） | **是** | Material Function Type• Creep: "CREEP"• Shrinkage Strain: "SHRINK"• Relaxation:  |
| `SCALE` | 数字 | **是** | Scale Factor |
| `CTYPE` | 文字（字符串） | **是** | Creep Type• Specific Creep: "SC"• Creep Function: "CF"• Creep Coefficient: "CC" |
| `RELAXATION` | 整数 | **是** | Relaxation Time• Hour: 0• Day: 1 |
| `vDAY` | Array[Object] | **是** | Function Data• Insert the data as an object |
| `DAY` | 数字 | **是** | Time |
| `VALUE` | 数字 | **是** | Value |
| `ELAST` | 数字 | 否 | Elast |
| `DESC` | 文字（字符串） | 否 | Description |

**最简 JSON**：
```json
{
  "TDMF": {
    "NAME": "<NAME>",
    "FTYPE": "<FTYPE>",
    "SCALE": 0,
    "CTYPE": "<CTYPE>",
    "RELAXATION": 0,
    "vDAY": [],
    "properties": {
      "vDAY": {
        "items": {
          "properties": {
            "DAY": 0,
            "VALUE": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "NAME": "F1",
      "FTYPE": "CREEP",
      "SCALE": 1,
      "CTYPE": "SC",
      "ELAST": 10,
      "DESC": "",
      "vDAY": [
        {
          "DAY": 0,
          "VALUE": 0
        },
        {
          "DAY": 1,
          "VALUE": 20
        }
      ]
    }
  }
}
```


---

### Time Dependent Material Properties - Creep/Shrinkage — `/db/TDMT`

**方法**: POST, GET, PUT, DELETE | **参数**: 43 必填 + 20 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Creep Function Name |
| `CODE` | 文字（字符串） | **是** | Code Name¹⁾ |
| `STR` | 数字 | **是** | Compression Strength |
| `HU` | 数字 | **是** | Relative Humidity |
| `AGE` | 数字 | **是** | Concrete Age |
| `UCS` | 数字 | **是** | Material Factored Ultimate Creep Strain (E-6) |
| `VOL` | 数字 | **是** | Volume-Surface Ratio• Range (2012): 100mm ~ 300mm• Range (2007): 25mm ~ 300mm |
| `RR` | 数字 | **是** | Reinforcement Ratio of Cross Section of Column Segment• When the "bRCE" is true |
| `MOD` | 数字 | **是** | Modulus of Elasticity of Steel• When the "bRCE" is true |
| `MSIZE` | 数字 | **是** | Notional Size of Member |
| `THIK` | 数字 | **是** | Hypothetical Thickness |
| `EPS_DRY` | 数字 | **是** | Drying Basic Shrinkage Strain³⁾ |
| `CEMCONTENT` | 数字 | **是** | Cement Content• Range: 260 kg/m3 ~ 500 kg/m3 |
| `WATERCONTENT` | 数字 | **是** | Water Content• Range: 130 kg/m3 ~ 230 kg/m3 |
| `BSC` | 数字 | **是** | Cement Type Coefficient |
| `CFACTA` | 数字 | **是** | Concrete Compressive Strength Factor a• Range: 0.05 ~ 9.25 |
| `CFACTB` | 数字 | **是** | Concrete Compressive Strength Factor b• Range: 0.67 ~ 0.98 |
| `SLUMP` | 数字 | **是** | Slump |
| `FAPERCENT` | 数字 | **是** | Fine Aggregate Percentage |
| `AIRCONTENT` | 数字 | **是** | Air Content |
| `CREEPCOEFF` | 数字 | **是** | Creep Coefficient• Range: 1.3 ~ 4.15 |
| `SHRINKSTRAIN` | 数字 | **是** | Shrinkage Strain• Range: 415 ~ 1070 (E-6) |
| `USS` | 数字 | **是** | Material Factored Ultimate Shrinkage Strain (E-6) |
| `CM` | 文字（字符串） | **是** | Calculation Method For E• JSCE: "JSCE"• AIJ: "AIJ" |
| `LAMBDA` | 数字 | **是** | Environmental Coefficient |
| `ALPHAFACT` | 数字 | **是** | Alpha-Factor according to Cement Type• 11 or 15 |
| `bAUTO` | 是/否（布尔值） | **是** | Autogenous Shrinkage Option |
| `GAMMAFACT` | 数字 | **是** | Gamma-Factor• When the "bAUTO" is true |
| `AFACT` | 数字 | **是** | a-Factor• When the "bAUTO" is true |
| `BFACT` | 数字 | **是** | b-Factor• When the "bAUTO" is true |
| `bGEN` | 是/否（布尔值） | **是** | General Shrinkage Option |
| `M` | 数字 | **是** | Module of an Exposed Surface |
| `W` | 数字 | **是** | Water Content |
| `MAXS` | 数字 | **是** | Maximum Aggregate Size |
| `A` | 数字 | **是** | Air Content |
| `PZ` | 数字 | **是** | Specific Content of the Cement Paste |
| `FLYASH` | 数字 | **是** | Amount of Added Fly Ash Alpha• Range : 0 ~ 30 |
| `FS` | 数字 | **是** | Relative Humidity Thickness• Only for NZ Bridge (SP/M/022)• Range: 0.20 ~ 0.72 |
| `DENSITY` | 数字 | **是** | Weight Density• Only for KDS-2016 |
| `IPFACT` | 数字 | **是** | Impact Factor by Cement Type and Mixture |
| `AGESOL` | 数字 | **是** | Age of Concrete at the Beginning of Solidification |
| `SSFNAME` | 文字（字符串） | **是** | Shrinkage Strain Function Name |
| `vCREEP_AGE` | Array[Object] | **是** | Creep Function• Insert the data as an object |
| `HTYPE` | 文字（字符串） | 否 | Type of Relative Humidity• Curing Underwater: "CU"• Relative Humidity: "RH" |
| `CTYPE` | 文字（字符串） | 否 | Type of Cement²⁾ |
| `VSR` | 文字（字符串） | 否 | Volume-Surface Ratio for Shrinkage Strain• ACI Code: "ACI"• PCA: "PCA" |
| `iEPS_DRY` | 整数 | 否 | Type of Drying Basic Shrinkage Strain³⁾ |
| `TYPE` | 文字（字符串） | 否 | Material Factored Ultimate Value Type• ACI Code: "CODE"• User: "USER" |
| `CMETHOD` | 文字（字符串） | 否 | Curing Method• Moist cured: "MOIST"• Steam cure: "STEAM" |
| `TYPEOFAFFR` | 整数 | 否 | Type of Aggregate<strong>• </strong>Only for CEB-FIP 2010◦ Basalt, dense limesto |
| `VSR1` | 文字（字符串） | 否 | Volume-Surface Ratio for Creep Strain• ACI Code: "ACI"• PCA: "PCA" |
| `LAF` | 文字（字符串） | 否 | Loading Aged Factor• moist cured ACI Code: "MOIST"• steam cured ACI Code: "STEAM |
| `US` | 数字 | 否 | Shrinkage |
| ... | ... | ... | *还有 10 个可选参数* |

**最简 JSON**：
```json
{
  "TDMT": {
    "NAME": "<NAME>",
    "CODE": "<CODE>",
    "STR": 0,
    "HU": 0,
    "AGE": 0,
    "UCS": 0,
    "VOL": 0,
    "RR": 0,
    "MOD": 0,
    "MSIZE": 0,
    "THIK": 0,
    "EPS_DRY": 0,
    "CEMCONTENT": 0,
    "WATERCONTENT": 0,
    "BSC": 0,
    "CFACTA": 0,
    "CFACTB": 0,
    "SLUMP": 0,
    "FAPERCENT": 0,
    "AIRCONTENT": 0,
    "CREEPCOEFF": 0,
    "SHRINKSTRAIN": 0,
    "USS": 0,
    "CM": "<CM>",
    "LAMBDA": 0,
    "ALPHAFACT": 0,
    "bAUTO": true,
    "GAMMAFACT": 0,
    "AFACT": 0,
    "BFACT": 0,
    "bGEN": true,
    "M": 0,
    "W": 0,
    "MAXS": 0,
    "A": 0,
    "PZ": 0,
    "FLYASH": 0,
    "FS": 0,
    "DENSITY": 0,
    "IPFACT": 0,
    "AGESOL": 0,
    "SSFNAME": "<SSFNAME>",
    "vCREEP_AGE": []
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "NAME": "CEB-FPI(2010)",
      "CODE": "CEB_FIP_2010",
      "STR": 50000,
      "HU": 70,
      "AGE": 3,
      "MSIZE": 1.2,
      "CTYPE": "NR",
      "TYPEOFAFFR": 0
    },
    "2": {
      "NAME": "CEB-FIP(1990)",
      "CODE": "CEB",
      "STR": 50000,
      "HU": 70,
      "AGE": 3,
      "MSIZE": 1.2,
      "CTYPE": "NR",
      "TYPEOFAFFR": 0
    },
    "3": {
      "NAME": "CEB-FIP(1978)",
      "CODE": "CEB_FIP_1978",
      "STR": 50000,
      "HU": 70,
      "AGE": 3,
      "MSIZE": 1.2,
      "CTYPE": "NR",
      "TYPEOFAFFR": 0
    }
  }
}
```


---

### Time Dependent Material Properties - Compressive Strength — `/db/TDME`

**方法**: POST, GET, PUT, DELETE | **参数**: 21 必填 + 2 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Material Name |
| `TYPE` | 文字（字符串） | **是** | Material Type• Code: "CODE"• User: "USER" |
| `CODENAME` | 文字（字符串） | **是** | Code Name¹⁾• When "TYPE" is "CODE" |
| `STRENGTH` | 数字 | **是** | Compression Strength• When "TYPE" is "CODE" |
| `A` | 数字 | **是** | Factor, a |
| `B` | 数字 | **是** | Factor, b |
| `D` | 数字 | **是** | Factor, d |
| `iCTYPE` | 整数 | **是** | Cement Type²⁾ |
| `TENS_STRN_FACTOR` | 数字 | **是** | Tensile Strength Factor |
| `iECTYPE` | 整数 | **是** | Elastic Cement Type• Normal Type: 0• Rapid Type: 1 |
| `CMETH` | 整数 | **是** | Curing Method• Natural Cure: 0• Steam Cure: 1 |
| `CTYPE` | 整数 | **是** | Concrete Type• Heavy Concrete: 0• Fine-Grained Concrete: 1 |
| `MAXS` | 数字 | **是** | Maximum Aggregate Size |
| `PZ` | 数字 | **是** | Specific Content of the Cement Paste |
| `nAGGRE` | 整数 | **是** | Aggregate Type• Basalt, dense limestone aggregates (1.2): 0• Quartzite aggregate |
| `DENSITY` | 数字 | **是** | Weight Density |
| `SCALE` | Array[Object] | **是** | Function Data• Insert the data as an object |
| `TIME` | 数字 | **是** | Time (day) |
| `COMP` | 数字 | **是** | Compression Strength |
| `TENS` | 数字 | **是** | Tensile Strength |
| `ELAST` | 数字 | **是** | Elastic Modulus |
| `bUSE` | 是/否（布尔值） | 否 | Use Concrete Data Option |
| `aDATA` | Array | 否 | FuncData |

**最简 JSON**：
```json
{
  "TDME": {
    "NAME": "<NAME>",
    "TYPE": "<TYPE>",
    "CODENAME": "<CODENAME>",
    "STRENGTH": 0,
    "A": 0,
    "B": 0,
    "D": 0,
    "iCTYPE": 0,
    "TENS_STRN_FACTOR": 0,
    "iECTYPE": 0,
    "CMETH": 0,
    "CTYPE": 0,
    "MAXS": 0,
    "PZ": 0,
    "nAGGRE": 0,
    "DENSITY": 0,
    "SCALE": [],
    "properties": {
      "aDATA": {
        "items": {
          "properties": {
            "TIME": 0,
            "COMP": 0,
            "TENS": 0,
            "ELAST": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "NAME": "ACI",
      "TYPE": "CODE",
      "CODENAME": "ACI",
      "STRENGTH": 30000,
      "A": 1,
      "B": 2
    }
  }
}
```


---

### Change Property — `/db/EDMP`

**方法**: POST, GET, PUT, DELETE | **参数**: 2 必填 + 0 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TYPE` | 文字（字符串） | **是** | Change Property Method• Notional Size of Member: "NSM"• Volume Surface Ratio: "V |
| `H_VS` | 数字 | **是** | Change Property Value• Notional Size of Member: h• Volume Surface Ratio: v/s |

**最简 JSON**：
```json
{
  "EDMP": {
    "TYPE": "<TYPE>",
    "H_VS": 0
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "10": {
      "TYPE": "NSM",
      "H_VS": 10
    }
  }
}
```


---

### Time Dependent Material Link — `/db/TMAT`

**方法**: POST, GET, PUT, DELETE | **参数**: 2 必填 + 0 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TDMT_NAME` | 文字（字符串） | **是** | Creep/Shrinkage Name |
| `TDME_NAME` | 文字（字符串） | **是** | Comp. Strength Name |

**最简 JSON**：
```json
{
  "TMAT": {
    "TDMT_NAME": "<TDMT_NAME>",
    "TDME_NAME": "<TDME_NAME>"
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "2": {
      "TDMT_NAME": "KDS2016",
      "TDME_NAME": "KDS2016"
    }
  }
}
```


---

### Plastic Material — `/db/EPMT`

**方法**: POST, GET, PUT, DELETE | **参数**: 24 必填 + 6 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Plastic Material Name |
| `MODEL_TYPE` | 文字（字符串） | **是** | Model Type• Tresca: "TR"• Von-Mises: "VM"• Mohr-Coulomb: "MC"• Drucker: "DP"• Ma |
| `TRESCA` | 对象（一组键值对） | **是** | Tresca Model |
| `INIT_YIELD_STRESS` | 数字 | **是** | Initial Uniaxial Yield Stress |
| `BACK_STRESS_COEF` | 数字 | **是** | Back Stress Coefficient• When Hardening Type is "MIX" |
| `HARDENING_COEF` | 数字 | **是** | Hardening Coefficient |
| `VMISES` | 对象（一组键值对） | **是** | Von Mises Model |
| `MOHRCL` | 对象（一组键值对） | **是** | Mohr-Coulomb Model |
| `INIT_COHESION` | 数字 | **是** | Initial Cohesion |
| `INIT_FRIC_ANGLE` | 数字 | **是** | Initial Friction Angle (deg) |
| `DRUCKER` | 对象（一组键值对） | **是** | Drucker-Prager Model |
| `MASONRY` | 对象（一组键值对） | **是** | Masonry Model |
| `BM` | 对象（一组键值对） | **是** | Brick Material |
| `BED_JOINT` | 对象（一组键值对） | **是** | Bed Joint Material |
| `HEAD_JOINT` | 对象（一组键值对） | **是** | Head Joint Material |
| `GEOM` | 对象（一组键值对） | **是** | Geometry |
| `CONCDMG` | 对象（一组键值对） | **是** | Concrete-Damage Model |
| `DILIATION_ANGLE` | 数字 | **是** | Diliation Angle |
| `ECCEN` | 数字 | **是** | Eccentricity |
| `FBO_FCO` | 数字 | **是** | fbo/fco |
| `K` | 数字 | **是** | K |
| `VISCOSITY_PARAM` | 数字 | **是** | Viscosity Parameter |
| `COMP_ITEMS` | Array[Object] | **是** | Compressive Behavior• Insert the data as an object |
| `TENSILE_ITEMS` | Array[Object] | **是** | Tensile Behavior• Insert the data as an object |
| `OPT_HARDENING` | 数字 | 否 | Hardening Option• Activated: 0• Inactivated: 1 |
| `HARDENING_TYPE` | 文字（字符串） | 否 | Hardening Type• Isotropic: "ISO"• Kinematic: "KIN"• Mixed: "MIX" |
| `MICROPL` | 对象（一组键值对） | 否 | Drucker-Prager |
| `PARAM_K` | Array | 否 | PARAM_K |
| `PARAM_C` | Array | 否 | PARAM_C |
| `MU` | 数字 | 否 | Mu |

**最简 JSON**：
```json
{
  "EPMT": {
    "NAME": "<NAME>",
    "MODEL_TYPE": "<MODEL_TYPE>",
    "TRESCA": {},
    "VMISES": {},
    "DRUCKER": {},
    "MOHRCL": {},
    "MASONRY": {
      "BM": {},
      "BED_JOINT": {},
      "HEAD_JOINT": {},
      "GEOM": {}
    },
    "CONCDMG": {
      "DILIATION_ANGLE": 0,
      "ECCEN": 0,
      "FBO_FCO": 0,
      "K": 0,
      "VISCOSITY_PARAM": 0,
      "COMP_ITEMS": [],
      "TENSILE_ITEMS": []
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "NAME": "Tresca_None",
      "MODEL_TYPE": "TR",
      "TRESCA": {
        "INIT_YIELD_STRESS": 30000,
        "OPT_HARDENING": 0
      }
    },
    "2": {
      "NAME": "Tresca_Isotropic",
      "MODEL_TYPE": "TR",
      "TRESCA": {
        "INIT_YIELD_STRESS": 30000,
        "OPT_HARDENING": 1,
        "HARDENING_TYPE": "ISO",
        "HARDENING_COEF": 20000
      }
    },
    "3": {
      "NAME": "Tresca_Kinematic",
      "MODEL_TYPE": "TR",
      "TRESCA": {
        "INIT_YIELD_STRESS": 30000,
        "OPT_HARDENING": 1,
        "HARDENING_TYPE": "KIN",
        "HARDENING_COEF": 20000
      }
    },
    "4": {
      "NAME": "Tresca_Mixed",
      "MODEL_TYPE": "TR",
      "TRESCA": {
        "INIT_YIELD_STRESS": 30000,
        "OPT_HARDENING": 1,
        "HARDENING_TYPE": "MIX",
        "BACK_STRESS_COEF": 0.8,
        "HARDENING_COEF": 20000
      }
    }
  }
}
```


---

### Plastic Material — `/db/EPMT-M1ᴴˢ⁾`

**方法**: POST, GET, PUT, DELETE | **参数**: 30 必填 + 2 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Name |
| `MODEL_TYPE` | integer (enum) | **是** | Model• Tresca: 0• Von Mises: 1• Mohr-Coulomb: 2• Drucker-Prager: 3• Masonry: 4•  |
| `TRESCA` | 对象（一组键值对） | **是** | Tresca parameters |
| `INIT_YIELD_STRESS` | 数字 | **是** | Initial Uniaxial Yield Stress |
| `HARDENING_TYPE` | integer (enum) | **是** | Isotropic / Kinematic / Mixed• Isotropic: 0 |
| `HARDENING_COEF` | 数字 | **是** | Hardening Coefficient |
| `VMISES` | 对象（一组键值对） | **是** | Von Mises parameters |
| `MOHRCL` | 对象（一组键值对） | **是** | Mohr-Coulomb parameters |
| `INIT_COHESION` | 数字 | **是** | Initial Cohesion |
| `INIT_FRIC_ANGLE` | 数字 | **是** | Initial Friction Angle |
| `DRUCKER` | 对象（一组键值对） | **是** | Drucker-Prager parameters |
| `MASONRY` | 对象（一组键值对） | **是** | Masonry parameters |
| `BM"¹⁾` | 对象（一组键值对） | **是** | Brick Material / Properties |
| `BED_JOINT"²⁾` | 对象（一组键值对） | **是** | Bed Joint / Properties |
| `HEAD_JOINT"³⁾` | 对象（一组键值对） | **是** | Head Joint / Properties |
| `GEOM"⁴⁾` | 对象（一组键值对） | **是** | Geometry / Properties |
| `MAT_COORD` | 对象（一组键值对） | **是** | Material Coordinate System |
| `COORD_TYPE` | integer (enum) | **是** | Material Coordinate System / Vertical : Horizontal• Global: 0• Element Local: 1• |
| `COORD_ANGLE` | 数字 | **是** | Angle from Global XWhen COORD_TYPE = 2 |
| `CONCDMG` | 对象（一组键值对） | **是** | Concrete Damage parameters |
| `DILIATION_ANGLE` | 数字 | **是** | Diliation Angle |
| `ECCEN` | 数字 | **是** | Eccentricity |
| `FBO_FCO` | 数字 | **是** | fbo/fco |
| `K` | 数字 | **是** | K |
| `VISCOSITY_PARAM` | 数字 | **是** | Viscosity Parameter |
| `COMP_ITEMS` | array [object] | **是** | Compressive Behavior / Strain-Yield Stress... |
| `INELASTIC_STRAIN` | 数字 | **是** | Inelastic Strain |
| `YIELD_STRESS` | 数字 | **是** | Yield Stress |
| `DAMAGE` | 数字 | **是** | Damage |
| `TENSILE_ITEMS` | array [object] | **是** | Tensile Behavior / Strain-Yield Stress... |
| `OPT_HARDENING` | 是/否（布尔值） | 否 | Hardening |
| `BACK_STRESS_COEF` | 数字 | 否 | Back Stress CoefficientWhen OPT_HARDENING = true, HARDENING_TYPE = 2 |

**最简 JSON**：
```json
{
  "NAME": "<NAME>",
  "MODEL_TYPE": {},
  "TRESCA": {},
  "INIT_YIELD_STRESS": 0,
  "HARDENING_TYPE": {},
  "HARDENING_COEF": 0,
  "VMISES": {},
  "MOHRCL": {},
  "INIT_COHESION": 0,
  "INIT_FRIC_ANGLE": 0,
  "DRUCKER": {},
  "MASONRY": {},
  "BM\"¹⁾": {},
  "BED_JOINT\"²⁾": {},
  "HEAD_JOINT\"³⁾": {},
  "GEOM\"⁴⁾": {},
  "MAT_COORD": {},
  "COORD_TYPE": {},
  "COORD_ANGLE": 0,
  "CONCDMG": {},
  "DILIATION_ANGLE": 0,
  "ECCEN": 0,
  "FBO_FCO": 0,
  "K": 0,
  "VISCOSITY_PARAM": 0,
  "COMP_ITEMS": [],
  "INELASTIC_STRAIN": 0,
  "YIELD_STRESS": 0,
  "DAMAGE": 0,
  "TENSILE_ITEMS": []
}
```


---

### Section Properties - Common — `/db/SECT`

**方法**: POST, GET, PUT, DELETE | **参数**: 4 必填 + 11 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `SECTTYPE` | 文字（字符串） | **是** | Section Data Type¹⁾ |
| `SECT_NAME` | 文字（字符串） | **是** | Section Name |
| `SECT_BEFORE` | 对象（一组键值对） | **是** | Section Data - Before |
| `SHAPE` | 文字（字符串） | **是** | Section Shape²⁾ |
| `OFFSET_PT` | 文字（字符串） | 否 | Offset Direction |
| `OFFSET_CENTER` | 整数 | 否 | Center Location• Centroid: 0• Center of Section: 1 |
| `USER_OFFSET_REF` | 整数 | 否 | User Type Offset Reference Position• Centroid: 0• Extreme Fiber(s): 1 |
| `HORZ_OFFSET_OPT` | 整数 | 否 | Horizontal Offset Option• to Extreme Fiber: 0• User: 1 |
| `USERDEF_OFFSET_YI` | 数字 | 否 | Horizontal Offset Value for I• for User Type |
| `USERDEF_OFFSET_YJ` | 数字 | 否 | Horizontal Offset Value for J• for User Type and Tapered Section |
| `VERT_OFFSET_OPT` | 整数 | 否 | Vertical Offset Option• to Extreme Fiber: 0• User: 1 |
| `USERDEF_OFFSET_ZI` | 数字 | 否 | Vertical Offset Value for I• for User Type |
| `USERDEF_OFFSET_ZJ` | 数字 | 否 | Vertical Offset Value for J• for User Type and Tapered Section |
| `USE_SHEAR_DEFORM` | 是/否（布尔值） | 否 | Consider Shear Deformation |
| ... | ... | ... | *还有 1 个可选参数* |

**最简 JSON**：
```json
{
  "SECT": {
    "SECTTYPE": "<SECTTYPE>",
    "SECT_NAME": "<SECT_NAME>",
    "SECT_BEFORE": {
      "SHAPE": "<SHAPE>"
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "6001": {
      "SECTTYPE": "DBUSER",
      "SECT_NAME": "LT_Const",
      "SECT_BEFORE": {
        "OFFSET_PT": "LT",
        "HORZ_OFFSET_OPT": 0,
        "VERT_OFFSET_OPT": 0,
        "USE_SHEAR_DEFORM": false,
        "USE_WARPING_EFFECT": false,
        "SHAPE": "SB",
        "DATATYPE": 2,
        "SECT_I": {
          "vSIZE": [
            1,
            1
          ]
        }
      }
    },
    "6002": {
      "SECTTYPE": "TAPERED",
      "SECT_NAME": "LT_Tapared",
      "SECT_BEFORE": {
        "OFFSET_PT": "LT",
        "USER_OFFSET_REF": 1,
        "HORZ_OFFSET_OPT": 1,
        "USERDEF_OFFSET_YI": 1.1,
        "USERDEF_OFFSET_YJ": 1.2,
        "VERT_OFFSET_OPT": 1,
        "USERDEF_OFFSET_ZI": 2.1,
        "USERDEF_OFFSET_ZJ": 2.2,
        "USE_SHEAR_DEFORM": true,
        "USE_WARPING_EFFECT": true,
        "SHAPE": "SB",
        "TYPE": 2,
        "SECT_I": {
          "vSIZE": [
            1,
            1
          ]
        },
        "SECT_J": {
          "vSIZE": [
            1,
            1
          ]
        },
        "Y_VAR": 1,
        "Z_VAR": 1
      }
    }
  }
}
```


---

### Thickness - Value — `/db/THIK`

**方法**: POST, GET, PUT, DELETE | **参数**: 4 必填 + 3 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Thickness Name |
| `TYPE` | 文字（字符串） | **是** | Thickness Type• Value: "VALUE"• Stiffened: "STIFFENED" |
| `T_IN` | 数字 | **是** | In-plane Thickness |
| `T_OUT` | 数字 | **是** | Out-of-plane Thickness• When "bINOUT" is True |
| `bINOUT` | 是/否（布尔值） | 否 | Plane• In-plane & Out-of-plane: false• In-plane / Out-of-plane: true |
| `OFFSET` | 整数 | 否 | Plate Offset Option• None: 0• Thickness Ratio: 1• Value: 2 |
| `O_VALUE` | 数字 | 否 | Local z Direction Offset Value• When "OFFSET" is 1 or 2 |

**最简 JSON**：
```json
{
  "THIK": {
    "NAME": "<NAME>",
    "TYPE": "<TYPE>",
    "T_IN": 0,
    "T_OUT": 0
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "NAME": "1",
      "TYPE": "VALUE",
      "bINOUT": false,
      "T_IN": 0.1,
      "T_OUT": 0,
      "O_VALUE": 0
    }
  }
}
```


---

### Tapered Group — `/db/TSGR`

**方法**: POST, GET, PUT, DELETE | **参数**: 6 必填 + 4 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Tapered Group Name |
| `ELEMLIST` | 整数数组 | **是** | Element No. |
| `ZVAR` | 文字（字符串） | **是** | Section Shape Variation• Linear: "LINEAR"• Polynomial: "POLY" |
| `ZEXP` | 数字 | **是** | Z axis - Exponent |
| `YVAR` | 文字（字符串） | **是** | Section Shape Variation• Linear: "LINEAR"• Polynomial: "POLY" |
| `YEXP` | 数字 | **是** | Y axis - Exponent |
| `ZFROM` | 文字（字符串） | 否 | Z axis - Symmetric Plane from i or j• "i" or "j" |
| `ZDIST` | 数字 | 否 | Z axis - Symmetric Plane Distance (m) |
| `YFROM` | 文字（字符串） | 否 | Y axis - Symmetric Plane from i or j• "i" or "j" |
| `YDIST` | 数字 | 否 | Y axis - Symmetric Plane Distance (m) |

**最简 JSON**：
```json
{
  "TSGR": {
    "NAME": "<NAME>",
    "ELEMLIST": 0,
    "ZVAR": "<ZVAR>",
    "ZEXP": 0,
    "YVAR": "<YVAR>",
    "YEXP": 0
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "NAME": "Linear",
      "ELEMLIST": [
        1,
        2,
        3
      ],
      "ZVAR": "LINEAR",
      "YVAR": "LINEAR"
    },
    "2": {
      "NAME": "ZPoly_YLinear",
      "ELEMLIST": [
        4,
        5,
        6
      ],
      "ZVAR": "POLY",
      "ZEXP": 2,
      "ZFROM": "i",
      "ZDIST": 1.2,
      "YVAR": "LINEAR"
    },
    "3": {
      "NAME": "Polynomial",
      "ELEMLIST": [
        7,
        8,
        9
      ],
      "ZVAR": "POLY",
      "ZEXP": 1.5,
      "ZFROM": "j",
      "ZDIST": 1.2,
      "YVAR": "POLY",
      "YEXP": 1.6,
      "YFROM": "j",
      "YDIST": 1.3
    }
  }
}
```


---

### Section Manager - Stiffness — `/db/SECF`

**方法**: POST, GET, PUT, DELETE | **参数**: 1 必填 + 20 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `ITEMS` | Array[Object] | **是** | Stiffness• Insert the data as an object |
| `ID` | 整数 | 否 | Serial Number |
| `GROUP_NAME` | 文字（字符串） | 否 | Boundary Group Name |
| `AREA_SF` | 数字 | 否 | Area - part I |
| `ASY_SF` | 数字 | 否 | Asy - part I |
| `ASZ_SF` | 数字 | 否 | Asz - part I |
| `IXX_SF` | 数字 | 否 | Ixx - part I |
| `IYY_SF` | 数字 | 否 | Iyy - part I |
| `IZZ_SF` | 数字 | 否 | Izz - part I |
| `WGT_SF` | 数字 | 否 | Weight - part I |
| `W_SF` | 数字 | 否 | W - part I |
| ... | ... | ... | *还有 10 个可选参数* |

**最简 JSON**：
```json
{
  "SECF": {
    "ITEMS": []
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "9001": {
      "ITEMS": [
        {
          "ID": 1,
          "GROUP_NAME": "Creep716",
          "AREA_SF": 2.607950983483919,
          "ASY_SF": 3.250759236531602,
          "ASZ_SF": 1.0918417525350592,
          "IXX_SF": 1.394622956596655,
          "IYY_SF": 1.5247905712919787,
          "IZZ_SF": 3.1433568982414926,
          "WGT_SF": 1,
          "W_SF": 1.288302203156793,
          "IPART": 2,
          "bDiffIJ": false
        },
        {
          "ID": 2,
          "GROUP_NAME": "Shrinkage716",
          "AREA_SF": 2.447026988940874,
          "ASY_SF": 3.025288463370856,
          "ASZ_SF": 1.08742280187333,
          "IXX_SF": 1.3551290279256454,
          "IYY_SF": 1.5023252980103026,
          "IZZ_SF": 2.9288493931376456,
          "WGT_SF": 1,
          "W_SF": 1.09614698234092,
          "IPART": 2,
          "bDiffIJ": false
        }
      ]
    }
  }
}
```


---

### Section Manager - Reinforcements — `/db/RPSC`

**方法**: POST, GET, PUT, DELETE | **参数**: 11 必填 + 24 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `OPT_MBAR_J` | 是/否（布尔值） | **是** | Same Rebar Data at i and j-end (Longitudinal) |
| `OPT_SBAR_J` | 是/否（布尔值） | **是** | Same Shear Rebar Data at i and j-end (Shear) |
| `OPT_CRACKED` | 是/否（布尔值） | **是** | Cracked Section |
| `SBAR_ITEMS` | Array[Object] | **是** | Shear Reinforcement Data• Insert the data as an object◦ Index 0: i-section◦ Inde |
| `MBAR_ITEMS` | Array[Object] | **是** | Longitudinal Reinforcement Data• Insert the data as an object◦ Index 0: i-sectio |
| `IJ` | 文字（字符串） | **是** | Section Positions - I / J• "I" or "J" |
| `NAME` | 文字（字符串） | **是** | Bar Name |
| `REF_Y` | 整数 | **是** | Reference Y• Centroid: 0• Left: 1 |
| `REF_Z` | 整数 | **是** | Reference Z• Top: 0• Bottom: 1 |
| `NUM` | 整数 | **是** | Number of Rebar |
| `PART` | 整数 | **是** | Part |
| `MBARS` | Array | 否 | LongitudinalReinforcementProperties |
| `OPT_DR` | 是/否（布尔值） | 否 | Diagonal Reinforcement (DR) |
| `DR_PITCH` | 数字 | 否 | [DR] Pitch |
| `DR_THETA` | 数字 | 否 | [DR] Angle |
| `DR_AW` | 数字 | 否 | [DR] Area |
| `OPT_SBW` | 是/否（布尔值） | 否 | Steel Bar for Web (SBW) |
| `SBW_PITCH` | 数字 | 否 | [SBW] Pitch |
| `SBW_ANGLE` | 数字 | 否 | [SBW] Angle |
| `SBW_AP` | 数字 | 否 | [SBW] Area |
| `SBW_PS` | 数字 | 否 | [SBW] Pre-force |
| ... | ... | ... | *还有 14 个可选参数* |

**最简 JSON**：
```json
{
  "RPSC": {
    "OPT_MBAR_J": true,
    "OPT_SBAR_J": true,
    "OPT_CRACKED": true,
    "SBAR_ITEMS": [],
    "properties": {
      "MBARS": {
        "items": {
          "properties": {
            "MBAR_ITEMS": {
              "items": {
                "properties": {
                  "IJ": "<IJ>",
                  "NAME": "<NAME>",
                  "REF_Y": 0,
                  "REF_Z": 0,
                  "NUM": 0,
                  "PART": 0
                }
              }
            }
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "401": {
      "OPT_MBAR_J": false,
      "OPT_SBAR_J": false,
      "OPT_CRACKED": false,
      "SBAR_ITEMS": [
        {
          "OPT_DR": false,
          "OPT_SBW": false,
          "OPT_TR": false,
          "OPT_SR": false,
          "OPT_LBAR_FLG": false
        }
      ],
      "MBARS": [
        {
          "MBAR_ITEMS": [
            {
              "IJ": "I",
              "NAME": "#18",
              "REF_Y": 1,
              "Y": 3.63,
              "REF_Z": 1,
              "Z": 2.148120340131863,
              "NUM": 1,
              "SPACING": 0,
              "PART": 0
            },
            {
              "IJ": "I",
              "NAME": "#18",
              "REF_Y": 0,
              "Y": 0,
              "REF_Z": 0,
              "Z": 0.1,
              "NUM": 2,
              "SPACING": 0.1,
              "PART": 0
            },
            {
              "IJ": "I",
              "NAME": "#11",
              "REF_Y": 1,
              "Y": 3.53,
              "REF_Z": 1,
              "Z": 0.04812034013186328,
              "NUM": 1,
              "SPACING": 0,
              "PART": 0
            },
            {
              "IJ": "I",
              "NAME": "#11",
              "REF_Y": 1,
              "Y": 3.63,
              "REF_Z": 1,
              "Z": 0.04812034013186328,
              "NUM": 1,
              "SPACING": 0,
              "PART": 0
            },
            {
              "IJ": "I",
              "NAME": "#11",
              "REF_Y": 1,
              "Y": 3.73,
              "REF_Z": 1,
              "Z": 0.04812034013186328,
              "NUM": 1,
              "SPACING": 0,
              "PART": 0
            },
            {
              "IJ": "I",
              "NAME": "#10",
              "REF_Y": 1,
              "Y": 1.4611,
              "REF_Z": 1,
              "Z": 2.131480340131863,
              "NUM": 1,
              "SPACING": 0,
              "PART": 0
            },
            {
              "IJ": "I",
              "NAME": "#10",
              "REF_Y": 1,
              "Y": 1.4492353743496362,
              "REF_Z": 1,
              "Z": 1.8353731826151332,
              "NUM": 1,
              "SPACING": 0,
              "PART": 0
            },
            {
              "IJ": "I",
              "NAME": "#10",
              "REF_Y": 1,
              "Y": 1.6839,
              "REF_Z": 1,
              "Z": 2.016350340131863,
              "NUM": 1,
              "SPACING": 0,
              "PART": 0
            },
            {
              "IJ": "I",
              "NAME": "#10",
              "REF_Y": 1,
              "Y": 5.7871,
              "REF_Z": 1,
              "Z": 2.166015640131863,
              "NUM": 1,
              "SPACING": 0,
              "PART": 0
            },
            {
              "IJ": "I",
              "NAME": "#10",
              "REF_Y": 1,
              "Y": 5.837429326148554,
              "REF_Z": 1,
              "Z": 2.078842690131863,
              "NUM": 1,
              "SPACING": 0,
              "PART": 0
            },
            {
              "IJ": "I",
              "NAME": "#10",
              "REF_Y": 1,
              "Y": 5.736770673851446,
              "REF_Z": 1,
              "Z": 2.078842690131863,
              "NUM": 1,
              "SPACING": 0,
              "PART": 0
            },
            {
              "IJ": "I",
              "NAME": "#10",
              "REF_Y": 1,
              "Y": 5.840814080204331,
              "REF_Z": 1,
              "Z": 1.7753208240021041,
              "NUM": 1,
              "SPACING": 0,
              "PART": 0
            },
            {
              "IJ": "I",
              "NAME": "#10",
              "REF_Y": 1,
              "Y": 5.802493302814122,
              "REF_Z": 1,
              "Z": 1.607298953906575,
              "NUM": 1,
              "SPACING": 0,
              "PART": 0
            },
            {
              "IJ": "I",
              "NAME": "#10",
              "REF_Y": 1,
              "Y": 5.643314689039411,
              "REF_Z": 1,
              "Z": 1.7222612860772002,
              "NUM": 1,
              "SPACING": 0,
              "PART": 0
            }
          ]
        },
        {
          "MBAR_ITEMS": [
            {
              "IJ": "J",
              "NAME": "#18",
              "REF_Y": 1,
              "Y": 3.63,
              "REF_Z": 1,
              "Z": 2.148120340131863,
              "NUM": 1,
              "SPACING": 0,
              "PART": 0
            },
            {
              "IJ": "J",
              "NAME": "#18",
              "REF_Y": 0,
              "Y": 0,
              "REF_Z": 0,
              "Z": 0.1,
              "NUM": 2,
              "SPACING": 0.1,
              "PART": 0
            },
            {
              "IJ": "J",
              "NAME": "#11",
              "REF_Y": 1,
              "Y": 3.53,
              "REF_Z": 1,
              "Z": 0.04812034013186328,
              "NUM": 1,
              "SPACING": 0,
              "PART": 0
            },
            {
              "IJ": "J",
              "NAME": "#11",
              "REF_Y": 1,
              "Y": 3.63,
              "REF_Z": 1,
              "Z": 0.04812034013186328,
              "NUM": 1,
              "SPACING": 0,
              "PART": 0
            },
            {
              "IJ": "J",
              "NAME": "#11",
              "REF_Y": 1,
              "Y": 3.73,
              "REF_Z": 1,
              "Z": 0.04812034013186328,
              "NUM": 1,
              "SPACING": 0,
              "PART": 0
            },
            {
              "IJ": "J",
              "NAME": "#10",
              "REF_Y": 1,
              "Y": 1.4611,
              "REF_Z": 1,
              "Z": 2.131480340131863,
              "NUM": 1,
              "SPACING": 0,
              "PART": 0
            },
            {
              "IJ": "J",
              "NAME": "#10",
              "REF_Y": 1,
              "Y": 1.4492353743496362,
              "REF_Z": 1,
              "Z": 1.8353731826151332,
              "NUM": 1,
              "SPACING": 0,
              "PART": 0
            },
            {
              "IJ": "J",
              "NAME": "#10",
              "REF_Y": 1,
              "Y": 1.6839,
              "REF_Z": 1,
              "Z": 2.016350340131863,
              "NUM": 1,
              "SPACING": 0,
              "PART": 0
            },
            {
              "IJ": "J",
              "NAME": "#10",
              "REF_Y": 1,
              "Y": 5.7871,
              "REF_Z": 1,
              "Z": 2.166015640131863,
              "NUM": 1,
              "SPACING": 0,
              "PART": 0
            },
            {
              "IJ": "J",
              "NAME": "#10",
              "REF_Y": 1,
              "Y": 5.837429326148554,
              "REF_Z": 1,
              "Z": 2.078842690131863,
              "NUM": 1,
              "SPACING": 0,
              "PART": 0
            },
            {
              "IJ": "J",
              "NAME": "#10",
              "REF_Y": 1,
              "Y": 5.736770673851446,
              "REF_Z": 1,
              "Z": 2.078842690131863,
              "NUM": 1,
              "SPACING": 0,
              "PART": 0
            },
            {
              "IJ": "J",
              "NAME": "#10",
              "REF_Y": 1,
              "Y": 5.840814080204331,
              "REF_Z": 1,
              "Z": 1.7753208240021041,
              "NUM": 1,
              "SPACING": 0,
              "PART": 0
            },
            {
              "IJ": "J",
              "NAME": "#10",
              "REF_Y": 1,
              "Y": 5.802493302814122,
              "REF_Z": 1,
              "Z": 1.607298953906575,
              "NUM": 1,
              "SPACING": 0,
              "PART": 0
            },
            {
              "IJ": "J",
              "NAME": "#10",
              "REF_Y": 1,
              "Y": 5.643314689039411,
              "REF_Z": 1,
              "Z": 1.7222612860772002,
              "NUM": 1,
              "SPACING": 0,
              "PART": 0
            }
          ]
        }
      ]
    }
  }
}
```


---

### Section Manager - Stress Points — `/db/STRPSSM`

**方法**: POST, GET, PUT, DELETE | **参数**: 6 必填 + 1 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `POINT_SIZE_1` | 整数 | **是** | Number of Stress Point for I |
| `POINT_SIZE_2` | 整数 | **是** | Number of Stress Point for J |
| `POINT1` | Array[Object] | **是** | Stress Point Coordinates for I• Insert the data as an object |
| `POINT2` | Array[Object] | **是** | Stress Point Coordinates for J• Insert the data as an object |
| `PY` | 数字 | **是** | Point Y |
| `PZ` | 数字 | **是** | Point Z |
| `OPT_SAME_J` | 是/否（布尔值） | 否 | Same Additional Stress Points Data at i and j-end |

**最简 JSON**：
```json
{
  "STRPSSM": {
    "POINT_SIZE_1": 0,
    "POINT_SIZE_2": 0,
    "POINT1": [],
    "POINT2": [],
    "properties": {
      "POINT1": {
        "items": {
          "properties": {
            "PY": 0,
            "PZ": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "STRPSSM": {
    "9003": {
      "OPT_SAME_J": true,
      "POINT_SIZE_1": 2,
      "POINT_SIZE_2": 2,
      "POINT1": [
        {
          "PY": 0.00583,
          "PZ": 0.00476
        },
        {
          "PY": -0.00506,
          "PZ": 0.00097
        }
      ],
      "POINT2": [
        {
          "PY": 0.007067356048348719,
          "PZ": 0.005572125828318985
        },
        {
          "PY": -0.0059233102292634635,
          "PZ": 0.0011354962297204655
        }
      ]
    }
  }
}
```


---

### Section Manager - Plate Stiffness Scale Factor — `/db/PSSF`

**方法**: POST, GET, PUT, DELETE | **参数**: 1 必填 + 10 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `ITEMS` | Array[Object] | **是** | Plate Stiffness Scale Factor• Insert the data as an object |
| `ID` | 整数 | 否 | Serial Number |
| `GROUP_NAME` | 文字（字符串） | 否 | Boundary Group Name |
| `AXIAL_X` | 数字 | 否 | Axial (Fxx) |
| `AXIAL_Y` | 数字 | 否 | Axial (Fyy) |
| `SHEAR` | 数字 | 否 | Shear (Fxy) |
| `OUT_BENDING_X` | 数字 | 否 | Bending (Mxx) |
| `OUT_BENDING_Y` | 数字 | 否 | Bending (Myy) |
| `OUT_TORSION` | 数字 | 否 | Bending (Mxy) |
| `OUT_SHEAR_X` | 数字 | 否 | Shear (Vxx) |
| `OUT_SHEAR_Y` | 数字 | 否 | Shear (Vyy) |

**最简 JSON**：
```json
{
  "PSSF": {
    "ITEMS": []
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "12": {
      "ITEMS": [
        {
          "ID": 1,
          "GROUP_NAME": "Service",
          "AXIAL_X": 0.6,
          "AXIAL_Y": 0.7,
          "SHEAR": 0.8,
          "OUT_BENDING_X": 0.9,
          "OUT_BENDING_Y": 1,
          "OUT_TORSION": 1.1,
          "OUT_SHEAR_X": 1.2,
          "OUT_SHEAR_Y": 1.3
        },
        {
          "ID": 2,
          "GROUP_NAME": "Ultimate",
          "AXIAL_X": 1.1,
          "AXIAL_Y": 1.2,
          "SHEAR": 1.3,
          "OUT_BENDING_X": 1.4,
          "OUT_BENDING_Y": 1.5,
          "OUT_TORSION": 1.6,
          "OUT_SHEAR_X": 1.7,
          "OUT_SHEAR_Y": 1.8
        }
      ]
    }
  }
}
```


---

### Section Manager - Section for Resultant Forces - Virtual Beam — `/db/VBEM`

**方法**: POST, GET, PUT, DELETE | **参数**: 2 必填 + 0 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `VSEC1` | 整数 | **是** | Virtual Section 1 |
| `VSEC2` | 整数 | **是** | Virtual Section 2 |

**最简 JSON**：
```json
{
  "VBEM": {
    "VSEC1": 0,
    "VSEC2": 0
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "VSEC1": 1,
      "VSEC2": 2
    }
  }
}
```


---

### Section Manager - Section for Resultant Forces - Virtual Section — `/db/VSEC`

**方法**: POST, GET, PUT, DELETE | **参数**: 10 必填 + 0 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Name |
| `CENT_CALC_TYPE` | 整数 | **是** | Centroid Calculation Type• 0 |
| `CEN_PT_X` | 数字 | **是** | Centroid X (Global) |
| `CEN_PT_Y` | 数字 | **是** | Centroid Y (Global) |
| `CEN_PT_Z` | 数字 | **是** | Centroid Z (Global) |
| `NORMAL_X` | 数字 | **是** | Direction Normal Vector (X) |
| `NORMAL_Y` | 数字 | **是** | Direction Normal Vector (Y) |
| `NORMAL_Z` | 数字 | **是** | Direction Normal Vector (Z) |
| `NODE_LIST` | 整数 | **是** | Node List |
| `ELEM_LIST` | 整数 | **是** | Element List |

**最简 JSON**：
```json
{
  "VSEC": {
    "NAME": "<NAME>",
    "CENT_CALC_TYPE": 0,
    "CEN_PT_X": 0,
    "CEN_PT_Y": 0,
    "CEN_PT_Z": 0,
    "NORMAL_X": 0,
    "NORMAL_Y": 0,
    "NORMAL_Z": 0,
    "NODE_LIST": 0,
    "ELEM_LIST": 0
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "NAME": "Girder_1_I",
      "CENT_CALC_TYPE": 0,
      "CEN_PT_X": 0,
      "CEN_PT_Y": 18.000000000000004,
      "CEN_PT_Z": 0.9343263371699391,
      "NORMAL_X": 1,
      "NORMAL_Y": 0,
      "NORMAL_Z": 0,
      "NODE_LIST": [
        20,
        29,
        26,
        23
      ],
      "ELEM_LIST": [
        18,
        16,
        14
      ]
    },
    "2": {
      "NAME": "Girder_2_J",
      "CENT_CALC_TYPE": 0,
      "CEN_PT_X": 1,
      "CEN_PT_Y": 18.000000000000004,
      "CEN_PT_Z": 0.9343263371699391,
      "NORMAL_X": 1,
      "NORMAL_Y": 0,
      "NORMAL_Z": 0,
      "NODE_LIST": [
        21,
        30,
        27,
        24
      ],
      "ELEM_LIST": [
        18,
        16,
        14
      ]
    }
  }
}
```


---

### Effective Width Scale Factor — `/db/EWSF`

**方法**: POST, GET, PUT, DELETE | **参数**: 5 必填 + 5 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `ITEMS` | Array[Object] | **是** | Effective Width Scale Factor• Insert the data as an object |
| `LYSCALE` | Real | **是** | ly Scale Factor for Sbz (I-End) |
| `ZTSCALE` | Real | **是** | z_top Scale Factor (I-End) |
| `ZBSCALE` | Real | **是** | z_bot Scale Factor (I-End) |
| `bJ` | 是/否（布尔值） | **是** | J-End Option |
| `ID` | 整数 | 否 | Serial Number |
| `GROUP_NAME` | 文字（字符串） | 否 | Boundary Group Name |
| `LYSCALE_J` | Real | 否 | ly Scale Factor for Sbz (J-End) |
| `ZTSCALE_J` | Real | 否 | z_top Scale Factor (J-End) |
| `ZBSCALE_J` | Real | 否 | z_bot Scale Factor (J-End) |

**最简 JSON**：
```json
{
  "EWSF": {
    "ITEMS": [],
    "properties": {
      "ITEMS": {
        "items": {
          "properties": {
            "LYSCALE": {},
            "ZTSCALE": {},
            "ZBSCALE": {},
            "bJ": true
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "10": {
      "ITEMS": [
        {
          "ID": 1,
          "GROUP_NAME": "Service",
          "LYSCALE": 0.5,
          "ZTSCALE": 0.6,
          "ZBSCALE": 0.7,
          "bJ": true,
          "LYSCALE_J": 0.8,
          "ZTSCALE_J": 0.9,
          "ZBSCALE_J": 1
        },
        {
          "ID": 2,
          "GROUP_NAME": "Ultimate",
          "LYSCALE": 1.1,
          "ZTSCALE": 1.2,
          "ZBSCALE": 1.3,
          "bJ": true,
          "LYSCALE_J": 1.4,
          "ZTSCALE_J": 1.5,
          "ZBSCALE_J": 1.6
        }
      ]
    }
  }
}
```


---

### Inelastic Hinge Control Data — `/db/IEHC`

**方法**: POST, GET, PUT, DELETE | **参数**: 17 必填 + 0 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `BEAM_LOC` | 整数 | **是** | Reference Location for Distributed Hinges• I-End: 0• Center: 1• J-End: 2 |
| `BeamDivNumNy` | 整数 | **是** | Number of Divisions(Beam-Column)• Ny (y-dir) |
| `BeamDivNumNz` | 整数 | **是** | Number of Divisions(Beam-Column)• Nz (z-dir) |
| `WallConsOut` | 是/否（布尔值） | **是** | Consider Out of Plane Nonlinearity of Plate Type |
| `WallDivNumZ` | 整数 | **是** | Number of divisions - z, Core |
| `WallDivNumY` | 整数 | **是** | Number of divisions - y, Core |
| `dR` | Real | **是** | Shear Spring Location |
| `WAreaSize` | 整数 | **是** | Fiber Wall Areas Core |
| `OPT_ConsiderRebarArea1D` | 是/否（布尔值） | **是** | Consider Reinforcement Area |
| `OPT_ConsiderRebarAreaWall` | 是/否（布尔值） | **是** | Wall, Consider Rebar Area |
| `FAreaSizeCore` | 整数 | **是** | Fiber Beam Areas Core• Auto Size: 0• Equal-Size: 1 |
| `FAreaSizeCover` | 整数 | **是** | Fiber Beam Areas Cover• Auto Size: 0• Equal-Size: 1 |
| `WAreaSizeCover` | 整数 | **是** | Fiber Wall Areas Cover |
| `BeamDivNumNyCover` | 整数 | **是** | Number of divisions(Beam-Column)• Ny (y-dir) |
| `BeamDivNumNzCover` | 整数 | **是** | Number of divisions(Beam-Column)• Nz (z-dir) |
| `WallDivNumZCover` | 整数 | **是** | Number of divisions - z, Cover |
| `WallDivNumYCover` | 整数 | **是** | Number of divisions - y, Cover |

**最简 JSON**：
```json
{
  "IEHC": {
    "BEAM_LOC": 0,
    "BeamDivNumNy": 0,
    "BeamDivNumNz": 0,
    "WallConsOut": true,
    "WallDivNumZ": 0,
    "WallDivNumY": 0,
    "dR": {},
    "WAreaSize": 0,
    "OPT_ConsiderRebarArea1D": true,
    "OPT_ConsiderRebarAreaWall": true,
    "FAreaSizeCore": 0,
    "FAreaSizeCover": 0,
    "WAreaSizeCover": 0,
    "BeamDivNumNyCover": 0,
    "BeamDivNumNzCover": 0,
    "WallDivNumZCover": 0,
    "WallDivNumYCover": 0
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "BEAM_LOC": 1,
      "BeamDivNumNy": 15,
      "BeamDivNumNz": 20,
      "WallConsOut": false,
      "WallDivNumZ": 8,
      "WallDivNumY": 1,
      "dR": 0.4,
      "WAreaSize": "AUTO",
      "OPT_ConsiderRebarArea1D": false,
      "OPT_ConsiderRebarAreaWall": false,
      "FAreaSizeCore": 1,
      "FAreaSizeCover": 1,
      "WAreaSizeCover": 1,
      "BeamDivNumNyCover": 20,
      "BeamDivNumNzCover": 15,
      "WallDivNumZCover": 8,
      "WallDivNumYCover": 1
    }
  }
}
```


---

### Assign Inelastic Hinge Properties — `/db/IEHG`

**方法**: POST, GET, PUT, DELETE | **参数**: 2 必填 + 0 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `PROP_NAME` | 文字（字符串） | **是** | Name of Inelastic Hinge Property |
| `FIBER_NAME` | 文字（字符串） | **是** | Name of Fiber Division |

**最简 JSON**：
```json
{
  "IEHG": {
    "PROP_NAME": "<PROP_NAME>",
    "FIBER_NAME": "<FIBER_NAME>"
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "2101": {
      "PROP_NAME": "Fiber_Auto",
      "FIBER_NAME": "B2102_Column12"
    }
  }
}
```


---

### Assign Inelastic Hinges - Beam — `/db/IEHG-BEAM-M1ᴴˢ⁾`

**方法**: POST, GET, PUT, DELETE | **参数**: 1 必填 + 0 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `INEL_PROP_NAME` | 文字（字符串） | **是** | Inelastic Hinge Property |

**最简 JSON**：
```json
{
  "INEL_PROP_NAME": "<INEL_PROP_NAME>"
}
```


---

### Assign Inelastic Hinges - Truss — `/db/IEHG-TRUSS-M1ᴴˢ⁾`

**方法**: POST, GET, PUT, DELETE | **参数**: 1 必填 + 0 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `INEL_PROP_NAME` | 文字（字符串） | **是** | Inelastic Hinge Property |

**最简 JSON**：
```json
{
  "INEL_PROP_NAME": "<INEL_PROP_NAME>"
}
```


---

### Assign Inelastic Hinges - General Link — `/db/IEHG-GL-M1ᴴˢ⁾`

**方法**: POST, GET, PUT, DELETE | **参数**: 1 必填 + 0 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `INEL_PROP_NAME` | 文字（字符串） | **是** | Inelastic Hinge Property |

**最简 JSON**：
```json
{
  "INEL_PROP_NAME": "<INEL_PROP_NAME>"
}
```


---

### Assign Inelastic Hinges - Point Spring Support — `/db/IEHG-PSS-M1ᴴˢ⁾`

**方法**: POST, GET, PUT, DELETE | **参数**: 1 必填 + 0 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `INEL_PROP_NAME` | 文字（字符串） | **是** | Inelastic Hinge Property |

**最简 JSON**：
```json
{
  "INEL_PROP_NAME": "<INEL_PROP_NAME>"
}
```


---

### Inelastic Material Properties — `/db/FIMP`

**方法**: POST, GET, PUT, DELETE | **参数**: 19 必填 + 2 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Material Name |
| `MATL_TYPE` | 文字（字符串） | **是** | Material Type• Concrete: "CONC"• Steel: "STEEL" |
| `HYS_MODEL` | 文字（字符串） | **是** | Hysteresis Model¹⁾ |
| `CONC` | 对象（一组键值对） | **是** | Concrete Hysteresis Model |
| `KENPAR` | 对象（一组键值对） | **是** | Kent & Park Model |
| `JPSTND` | 对象（一组键值对） | **是** | Japanese Concrete Standard Specification Model |
| `JP_H14` | 对象（一组键值对） | **是** | Japan Roadway Specification (H.14) Model |
| `NAGOYA` | 对象（一组键值对） | **是** | Nagoya Highway Corporation Model |
| `TRILIN` | 对象（一组键值对） | **是** | Asymmetrical Bilinear Steel Model |
| `CHGB02` | 对象（一组键值对） | **是** | China Concrete Code (GB50010-02) |
| `MANDER` | 对象（一组键值对） | **是** | Mander Model |
| `JP_H24` | 对象（一组键值对） | **是** | Japan Roadway Specification (H.24) Model |
| `CHGB10` | 对象（一组键值对） | **是** | China Concrete Code (GB50010-10) |
| `STEEL` | 对象（一组键值对） | **是** | Steel Hysteresis Model |
| `MENEGO` | 对象（一组键值对） | **是** | Menegotto-Pinto Model |
| `BILINE` | 对象（一组键值对） | **是** | Bilinear Model |
| `GENBIL` | 对象（一组键值对） | **是** | Asymmetrical Bilinear Steel Model |
| `PARKMD` | 对象（一组键值对） | **是** | Park Model |
| `JPROAD` | 对象（一组键值对） | **是** | Japan Roadway Specification Model |
| `ASSIGN_TYPE` | 文字（字符串） | 否 | AssignType |
| `ENRGDS` | 对象（一组键值对） | 否 | EnergyBasedModel |

**最简 JSON**：
```json
{
  "FIMP": {
    "NAME": "<NAME>",
    "MATL_TYPE": "<MATL_TYPE>",
    "HYS_MODEL": "<HYS_MODEL>",
    "CONC": {
      "KENPAR": {},
      "JPSTND": {},
      "JP_H14": {},
      "NAGOYA": {},
      "CHGB02": {},
      "MANDER": {},
      "JP_H24": {}
    },
    "STEEL": {
      "MENEGO": {},
      "BILINE": {},
      "GENBIL": {},
      "PARKMD": {},
      "JPROAD": {}
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "3": {
      "NAME": "Conc_Kent&Park",
      "MATL_TYPE": "CONC",
      "HYS_MODEL": "KPM",
      "CONC": {
        "KENPAR": {
          "FC": 30000,
          "EC0": 0.002,
          "K": 1,
          "ECU": 0.003,
          "PARTIAL_FACT": 1,
          "EC1_METHOD": 0,
          "EC1": 0.0025,
          "STRENGTH_AFTER": 1
        }
      }
    }
  }
}
```


---

### Fiber Division of Section — `/db/FIBR`

**方法**: POST, GET, PUT, DELETE | **参数**: 16 必填 + 5 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Fiber Division Name |
| `SECT_KEY` | 整数 | **是** | Assigned Section ID |
| `ASSIGN_TYPE` | 整数 | **是** | Assign Type |
| `FIMP_NAME` | Array[String, 6] | **是** | Inelastic Material Properties Name |
| `FIBR_BASE` | Array[Object] | **是** | Fiber Division• Insert the data as an object |
| `OPT_MONITORED_FIBER` | 是/否（布尔值） | **是** | Monitored Fiber Option |
| `FIBR_BASE_KEY` | 是/否（布尔值） | **是** | Base Key |
| `REBAR_NAME` | 文字（字符串） | **是** | Rebar Name |
| `AREA` | 数字 | **是** | Area |
| `CENTER_Y` | 数字 | **是** | Center Y |
| `CENTER_Z` | 数字 | **是** | Center Z |
| `FIBER_MATL_ID` | 数字 | **是** | Fiber Material ID |
| `AREA_CONSIDER_REBAR` | 数字 | **是** | Area Consider Rebar |
| `OPT_IS_REBAR` | 是/否（布尔值） | **是** | Rebar Options |
| `POINT_Y` | 数字数组 | **是** | Point Y |
| `POINT_Z` | 数字数组 | **是** | Point Z |
| `FIMP_COLOR` | Array[Object, 6] | 否 | Inelastic Material Properties Color |
| `MONITORED_FIBER` | 整数数组 | 否 | Monitored Fiber |
| `R` | 整数 | 否 | Red |
| `G` | 整数 | 否 | Green |
| `B` | 整数 | 否 | Blue |

**最简 JSON**：
```json
{
  "FIBR": {
    "NAME": "<NAME>",
    "SECT_KEY": 0,
    "ASSIGN_TYPE": 0,
    "FIMP_NAME": "<FIMP_NAME>",
    "FIBR_BASE": [],
    "OPT_MONITORED_FIBER": true,
    "properties": {
      "FIBR_BASE": {
        "items": {
          "properties": {
            "FIBR_BASE_KEY": true,
            "REBAR_NAME": "<REBAR_NAME>",
            "AREA": 0,
            "CENTER_Y": 0,
            "CENTER_Z": 0,
            "FIBER_MATL_ID": 0,
            "AREA_CONSIDER_REBAR": 0,
            "OPT_IS_REBAR": true,
            "POINT_Y": 0,
            "POINT_Z": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "NAME": "General",
      "SECT_KEY": 11001,
      "ASSIGN_TYPE": 0,
      "FIMP_NAME": [
        "Steel",
        "Cover Concrete",
        "Core Conc Column 1 2",
        "Core Conc Column 1 2",
        "Core Conc Column 1 2",
        "Core Conc Column 1 2"
      ],
      "FIMP_COLOR": [
        {
          "R": 121,
          "G": 198,
          "B": 220
        },
        {
          "R": 245,
          "G": 242,
          "B": 31
        },
        {
          "R": 214,
          "G": 126,
          "B": 176
        },
        {
          "R": 63,
          "G": 174,
          "B": 179
        },
        {
          "R": 40,
          "G": 130,
          "B": 89
        },
        {
          "R": 223,
          "G": 176,
          "B": 192
        }
      ],
      "FIBR_BASE": [
        {
          "FIBR_BASE_KEY": 752,
          "REBAR_NAME": "",
          "AREA": 0.00688072,
          "CENTER_Y": -1.05047e-16,
          "CENTER_Z": 1.06179,
          "FIBER_MATL_ID": 1,
          "AREA_CONSIDER_REBAR": 0,
          "OPT_IS_REBAR": false,
          "POINT_Y": [
            0.0527429,
            0.0527429,
            -0.0527429,
            -0.0527429,
            0
          ],
          "POINT_Z": [
            1.08596,
            1.029,
            1.029,
            1.08596,
            1.1025
          ]
        }
      ],
      "OPT_MONITORED_FIBER": true,
      "MONITORED_FIBER": [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0
      ]
    }
  }
}
```


---

### Group Damping — `/db/GRDP`

**方法**: POST, GET, PUT, DELETE | **参数**: 30 必填 + 7 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `STIFF_COEF_DEFAULT` | 数字 | **是** | Stiffness Proportional Value• Direct Specification: User Input• Calculate from M |
| `MASS_COEF_DEFAULT` | 数字 | **是** | Mass Proportional Value• Direct Specification: User Input• Calculate from Modal  |
| `OPT_CALC_WHEN_USED` | 是/否（布尔值） | **是** | Calculate Only When Used |
| `DIRECT_CALC_MODE_DEFAULT` | 整数 | **是** | Calculate from Modal Damping• Direct Specification: 0• Calculate from Modal Damp |
| `FREQ_PERIOD_MODE_DEFAULT` | 整数 | **是** | Coefficients Calculation• Frequency: 0• Period: 1 |
| `FREQ_MODE_1_DEFAULT` | 数字 | **是** | Frequency Mode 1 Value |
| `FREQ_MODE_2_DEFAULT` | 数字 | **是** | Frequency Mode 2 Value |
| `PERIOD_MODE_1_DEFAULT` | 数字 | **是** | Period Mode 1 Value |
| `PERIOD_MODE_2_DEFAULT` | 数字 | **是** | Period Mode 2 Value |
| `DAMPING_MODE_1_DEFAULT` | 数字 | **是** | Damping Ratio Mode 1 value |
| `DAMPING_MODE_2_DEFAULT` | 数字 | **是** | Damping Ratio Mode 2 value6 |
| `bExistElement` | 是/否（布尔值） | **是** | Element Mass & Stiffness Proportional |
| `bExistStrain` | 是/否（布尔值） | **是** | Strain Energy Proportional |
| `GROUP_DAMPING_ITEMS` | Array[Object] | **是** | Damping Coefficients for Specified Material Data/Group• Insert the data as an ob |
| `STRAIN_GROUP_ITEMS` | Array[Object] | **是** | Damping Ratio for Specified Elements and Boundaries• Insert the data as an objec |
| `ELEM_GROUP_PRIORITY` | 整数 | **是** | Priority between Material Data and Structure Group• Material Data: 0• Structure  |
| `ELEM_VALUE_PRIORITY` | 整数 | **是** | Priority between Structure Groups• Smallest Damping Ratio: 0• Largest Damping Ra |
| `STRAIN_GROUP_PRIORITY` | 整数 | **是** | Priority between Material Data and Structure Group• Material Data: 0• Structure  |
| `STRAIN_VALUE_PRIORITY` | 整数 | **是** | Priority between Structure Groups• Smallest Damping Ratio: 0• Largest Damping Ra |
| `GROUP_TYPE` | 文字（字符串） | **是** | Damping Ratio Type• Material: "MATERIAL"• Structure Group: "STRUCTURE"• Boundary |
| `GROUP_NAME` | 文字（字符串） | **是** | Damping Ratio Name• Material: ID• Structure Group: Name• Boundary: Name |
| `DAMPING_RATIO` | 数字 | **是** | Damping Ratio |
| `STIFF_COEF` | 数字 | **是** | Stiffness Proportional |
| `MASS_COEF` | Real | **是** | Mass Proportional |
| `FREQ_MODE_1` | 数字 | **是** | Frequency - Mode 1 |
| `FREQ_MODE_2` | 数字 | **是** | Frequency - Mode 2 |
| `PERIOD_MODE_1` | 数字 | **是** | Period - Mode 1 |
| `PERIOD_MODE_2` | 数字 | **是** | Period - Mode 2 |
| `DAMPING_RATIO_MODE_1` | 数字 | **是** | Damping Ratio - Mode 1 |
| `DAMPING_RATIO_MODE_2` | 数字 | **是** | Damping Ratio - Mode 2 |
| `OPT_MASS_PROP_DEFAULT` | 是/否（布尔值） | 否 | Unspecified Nodes, Elements and Boundaries• Mass Proportional Option |
| `OPT_STIFF_PROP_DEFAULT` | 是/否（布尔值） | 否 | Unspecified Nodes, Elements and Boundaries• Stiffness Proportional |
| `OPT_STIFF_PROP` | 是/否（布尔值） | 否 | Stiffness Proportional Options |
| `OPT_MASS_PROP` | 是/否（布尔值） | 否 | Mass Proportional Options |
| `DIRECT_CALC_MODE` | 整数 | 否 | Direct Specification / Calculate from Modal Damping Mode Index |
| `FREQ_PERIOD_MODE` | 整数 | 否 | Frequency / Period Mode Index |
| `DAMPING_RATIO_MODE` | 整数 | 否 | Using Material Data / Direct Define Mode Index |

**最简 JSON**：
```json
{
  "GRDP": {
    "STIFF_COEF_DEFAULT": 0,
    "MASS_COEF_DEFAULT": 0,
    "OPT_CALC_WHEN_USED": true,
    "DIRECT_CALC_MODE_DEFAULT": 0,
    "FREQ_PERIOD_MODE_DEFAULT": 0,
    "FREQ_MODE_1_DEFAULT": 0,
    "FREQ_MODE_2_DEFAULT": 0,
    "PERIOD_MODE_1_DEFAULT": 0,
    "PERIOD_MODE_2_DEFAULT": 0,
    "DAMPING_MODE_1_DEFAULT": 0,
    "DAMPING_MODE_2_DEFAULT": 0,
    "bExistElement": true,
    "bExistStrain": true,
    "GROUP_DAMPING_ITEMS": [],
    "STRAIN_GROUP_ITEMS": [],
    "ELEM_GROUP_PRIORITY": 0,
    "ELEM_VALUE_PRIORITY": 0,
    "STRAIN_GROUP_PRIORITY": 0,
    "STRAIN_VALUE_PRIORITY": 0,
    "properties": {
      "GROUP_DAMPING_ITEMS": {
        "items": {
          "properties": {
            "GROUP_TYPE": "<GROUP_TYPE>",
            "GROUP_NAME": "<GROUP_NAME>",
            "STIFF_COEF": 0,
            "MASS_COEF": {},
            "FREQ_MODE_1": 0,
            "FREQ_MODE_2": 0,
            "PERIOD_MODE_1": 0,
            "PERIOD_MODE_2": 0,
            "DAMPING_RATIO_MODE_1": 0,
            "DAMPING_RATIO_MODE_2": 0
          }
        }
      },
      "STRAIN_GROUP_ITEMS": {
        "items": {
          "properties": {
            "DAMPING_RATIO": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "STIFF_COEF_DEFAULT": 0.0848826377636192,
      "MASS_COEF_DEFAULT": 0.04188790133333333,
      "OPT_CALC_WHEN_USED": true,
      "OPT_MASS_PROP_DEFAULT": true,
      "OPT_STIFF_PROP_DEFAULT": true,
      "DIRECT_CALC_MODE_DEFAULT": 1,
      "FREQ_PERIOD_MODE_DEFAULT": 0,
      "FREQ_MODE_1_DEFAULT": 0.1,
      "FREQ_MODE_2_DEFAULT": 0.2,
      "PERIOD_MODE_1_DEFAULT": 0,
      "PERIOD_MODE_2_DEFAULT": 0,
      "DAMPING_MODE_1_DEFAULT": 0.06,
      "DAMPING_MODE_2_DEFAULT": 0.07,
      "bExistElement": true,
      "bExistStrain": true,
      "GROUP_DAMPING_ITEMS": [
        {
          "GROUP_TYPE": "MATERIAL",
          "GROUP_NAME": "1",
          "STIFF_COEF": 0.005787452574792216,
          "OPT_STIFF_PROP": true,
          "MASS_COEF": 0.06854383854545451,
          "OPT_MASS_PROP": true,
          "DIRECT_CALC_MODE": 1,
          "FREQ_PERIOD_MODE": 0,
          "FREQ_MODE_1": 0.5,
          "FREQ_MODE_2": 0.6,
          "PERIOD_MODE_1": 0,
          "PERIOD_MODE_2": 0,
          "DAMPING_RATIO_MODE": 0,
          "DAMPING_RATIO_MODE_1": 0.02,
          "DAMPING_RATIO_MODE_2": 0.02
        },
        {
          "GROUP_TYPE": "STRUCTURE",
          "GROUP_NAME": "VBGirder",
          "STIFF_COEF": 0.00106103297204524,
          "OPT_STIFF_PROP": true,
          "MASS_COEF": 3.3510321066666675,
          "OPT_MASS_PROP": true,
          "DIRECT_CALC_MODE": 1,
          "FREQ_PERIOD_MODE": 1,
          "FREQ_MODE_1": 0.5,
          "FREQ_MODE_2": 0.6,
          "PERIOD_MODE_1": 0.1,
          "PERIOD_MODE_2": 0.2,
          "DAMPING_RATIO_MODE": 1,
          "DAMPING_RATIO_MODE_1": 0.06,
          "DAMPING_RATIO_MODE_2": 0.07
        },
        {
          "GROUP_TYPE": "BOUNDARY",
          "GROUP_NAME": "Service",
          "STIFF_COEF": 0.00106103297204524,
          "OPT_STIFF_PROP": true,
          "MASS_COEF": 3.3510321066666675,
          "OPT_MASS_PROP": true,
          "DIRECT_CALC_MODE": 1,
          "FREQ_PERIOD_MODE": 1,
          "FREQ_MODE_1": 0.5,
          "FREQ_MODE_2": 0.6,
          "PERIOD_MODE_1": 0.1,
          "PERIOD_MODE_2": 0.2,
          "DAMPING_RATIO_MODE": 1,
          "DAMPING_RATIO_MODE_1": 0.06,
          "DAMPING_RATIO_MODE_2": 0.07
        }
      ],
      "STRAIN_GROUP_ITEMS": [
        {
          "GROUP_TYPE": "MATERIAL",
          "GROUP_NAME": "1",
          "DAMPING_RATIO": 0.02
        },
        {
          "GROUP_TYPE": "STRUCTURE",
          "GROUP_NAME": "VBGirder",
          "DAMPING_RATIO": 0.05
        },
        {
          "GROUP_TYPE": "BOUNDARY",
          "GROUP_NAME": "Service",
          "DAMPING_RATIO": 0.05
        }
      ],
      "ELEM_GROUP_PRIORITY": 0,
      "ELEM_VALUE_PRIORITY": 0,
      "STRAIN_GROUP_PRIORITY": 0,
      "STRAIN_VALUE_PRIORITY": 0
    }
  }
}
```


---

### Element Stiffness Scale Factor — `/db/ESSF`

**方法**: POST, GET, PUT, DELETE | **参数**: 1 必填 + 10 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `ID` | Array[Object] | **是** | Serial Number |
| `ITEMS` | Array | 否 | Items |
| `AREA_SF` | 数字 | 否 | Area• Cross-sectional area |
| `ASY_SF` | 数字 | 否 | Asy• Effective Shear Area resisting shear forces in the element local y-axis |
| `ASZ_SF` | 数字 | 否 | Asz• Effective shear Area resisting shear forces in the element local z-axis |
| `IXX_SF` | 数字 | 否 | Ixx• Torsional Resistance about the element local a-axis |
| `IYY_SF` | 数字 | 否 | Iyy• Area Moment of Inertia about the element local y-axis |
| `IZZ_SF` | 数字 | 否 | Izz• Area Moment of Inertia about the element local z-axis |
| `WGT_SF` | 数字 | 否 | Weight• Cross-sectional area used for calculating self-weight |
| `GROUP_NAME` | 文字（字符串） | 否 | Boundary Group |
| `iPart` | 文字（字符串） | 否 | Part• For sections defined as Composite Type, Scale Factors can be defined for " |

**最简 JSON**：
```json
{
  "Argument": {
    "properties": {
      "ITEMS": {
        "items": {
          "properties": {
            "ID": []
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "ITEMS": [
        {
          "ID": 1,
          "AREA_SF": 0.5,
          "ASY_SF": 0.6,
          "ASZ_SF": 0.7,
          "IXX_SF": 0.8,
          "IYY_SF": 0.8,
          "IZZ_SF": 0.9,
          "WGT_SF": 0.95,
          "GROUP_NAME": "",
          "iPart": "Before"
        }
      ]
    }
  }
}
```


---

### Constraint Support — `/db/CONS`

**方法**: POST, GET, PUT, DELETE | **参数**: 2 必填 + 2 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `ITEMS` | Array[Object] | **是** | Constraint Supports• Insert the data as an object |
| `CONSTRAINT` | 文字（字符串） | **是** | Constraint• [DX, DY, DZ, RX, RY, RZ, RW]◦ Constraint: 1◦ Unconstraint: 0◦ RW: Wa |
| `ID` | 整数 | 否 | Serial Number |
| `GROUP_NAME` | 文字（字符串） | 否 | Boundary Group Name |

**最简 JSON**：
```json
{
  "CONS": {
    "ITEMS": [],
    "properties": {
      "ITEMS": {
        "items": {
          "properties": {
            "CONSTRAINT": "<CONSTRAINT>"
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "ITEMS": [
        {
          "ID": 1,
          "GROUP_NAME": "Service",
          "CONSTRAINT": "1111000"
        }
      ]
    }
  }
}
```


---

### Point Spring — `/db/NSPR`

**方法**: POST, GET, PUT, DELETE | **参数**: 6 必填 + 9 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `ITEMS` | Array[Object] | **是** | Point Spring• Insert the data as an object |
| `TYPE` | 文字（字符串） | **是** | Spring Type• Linear: "LINEAR"• Compression-Only: "COMP"• Tension-Only: "TENS"• M |
| `SDR` | Array[Number,6] | **是** | Spring Stiffness• [SDx, SDy, SDz, SRx, SRy, SRz] |
| `STIFF` | 数字 | **是** | Stiffness |
| `DIR` | 整数 | **是** | Direction• Dx (+): 0• Dx (-): 1• Dy (+): 2• Dy (-): 3• Dz (+): 4• Dz (-): 5• Vec |
| `FUNCTION` | 整数 | **是** | Defined Forces-Deformation Function ID Number |
| `ID` | 整数 | 否 | Serial Number |
| `GROUP_NAME` | 文字（字符串） | 否 | Boundary Group Name |
| `FormType` | 整数 | 否 | Create Function Type• by Point Spring Function: 0• by Surface Spring Function: 1 |
| `F_S` | Array[Boolean,6] | 否 | Fixed Option• [SDx, SDy, SDz, SRx, SRy, SRz] |
| `DAMPING` | 是/否（布尔值） | 否 | Damping Constant |
| `Cr` | Array[Number,6] | 否 | Damping• [Cx, Cy, Cz, CRx, CRy, CRz] |
| `DV` | Array[Number,3) | 否 | Normal Vector• When "DIR" is 6 |
| `EFFAREA` | 数字 | 否 | Width of Frame |
| `DK` | Array[Number,3) | 否 | Modulus of Subgrade Reaction• [Kx, Ky, Kz] |

**最简 JSON**：
```json
{
  "NSPR": {
    "ITEMS": [],
    "properties": {
      "ITEMS": {
        "items": {
          "properties": {
            "TYPE": "<TYPE>",
            "SDR": 0,
            "STIFF": 0,
            "DIR": 0,
            "FUNCTION": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "2": {
      "ITEMS": [
        {
          "ID": 1,
          "TYPE": "LINEAR",
          "F_S": [
            false,
            false,
            false,
            false,
            false,
            false
          ],
          "SDR": [
            33000,
            34000,
            35000,
            33000000,
            34000000,
            35000000
          ],
          "DAMPING": true,
          "Cr": [
            1,
            2,
            3,
            4,
            5,
            6
          ],
          "GROUP_NAME": "Service"
        }
      ]
    },
    "3": {
      "ITEMS": [
        {
          "ID": 1,
          "TYPE": "LINEAR",
          "F_S": [
            true,
            true,
            true,
            true,
            true,
            true
          ],
          "SDR": [
            33000,
            34000,
            35000,
            33000000,
            34000000,
            35000000
          ],
          "DAMPING": true,
          "Cr": [
            1,
            2,
            3,
            4,
            5,
            6
          ],
          "GROUP_NAME": "Service"
        }
      ]
    }
  }
}
```


---

### Define General Spring Type — `/db/GSTP`

**方法**: POST, GET, PUT, DELETE | **参数**: 1 必填 + 6 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | General Spring Name |
| `SPRING` | Array[Number, 21] | 否 | Stiffness Matrix¹⁾ |
| `MASS` | Array[Number, 21] | 否 | Mass Matrix¹⁾ |
| `DAMPING` | Array[Number, 21] | 否 | Damping Matrix¹⁾ |
| `OPT_STIFFNESS` | 是/否（布尔值） | 否 | Stiffness Matrix Option• True |
| `OPT_MASS` | 是/否（布尔值） | 否 | Mass Matrix Option |
| `OPT_DAMPING` | 是/否（布尔值） | 否 | Damping Matrix Option |

**最简 JSON**：
```json
{
  "GSTP": {
    "NAME": "<NAME>"
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "3": {
      "NAME": "GS_Damping",
      "SPRING": [
        1,
        7,
        12,
        16,
        19,
        21,
        2,
        3,
        4,
        5,
        6,
        8,
        9,
        10,
        11,
        13,
        14,
        15,
        17,
        18,
        20
      ],
      "MASS": [
        1,
        7,
        12,
        16,
        19,
        21,
        2,
        3,
        4,
        5,
        6,
        8,
        9,
        10,
        11,
        13,
        14,
        15,
        17,
        18,
        20
      ],
      "DAMPING": [
        1,
        7,
        12,
        16,
        19,
        21,
        2,
        3,
        4,
        5,
        6,
        8,
        9,
        10,
        11,
        13,
        14,
        15,
        17,
        18,
        20
      ],
      "OPT_STIFFNESS": true,
      "OPT_MASS": true,
      "OPT_DAMPING": true
    }
  }
}
```


---

### Assign General Spring Supports — `/db/GSPR`

**方法**: POST, GET, PUT, DELETE | **参数**: 2 必填 + 2 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `ITEMS` | Array[Object] | **是** | General Spring• Insert the data as an object |
| `TYPE_NAME` | 文字（字符串） | **是** | Defined General Spring Name |
| `ID` | 整数 | 否 | Serial Number |
| `GROUP_NAME` | 文字（字符串） | 否 | Boundary Group Name |

**最简 JSON**：
```json
{
  "GSPR": {
    "ITEMS": [],
    "properties": {
      "ITEMS": {
        "items": {
          "properties": {
            "TYPE_NAME": "<TYPE_NAME>"
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "14": {
      "ITEMS": [
        {
          "ID": 1,
          "GROUP_NAME": "Service",
          "TYPE_NAME": "GS_Stiff"
        }
      ]
    }
  }
}
```


---

### Surface Spring — `/db/SSPS`

**方法**: POST, GET, PUT, DELETE | **参数**: 4 必填 + 4 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `ITEMS` | Array[Object] | **是** | Surface Spring• Insert the data as an object |
| `ELEM_TYPE` | 文字（字符串） | **是** | Element Type• Frame: "FRAME"• Planar(Face): "PLANAR(FACE)"• Planar(Edge): "PLANA |
| `MODULUS` | 数字 | **是** | Modulus of Subgrade Reaction (Ks) |
| `WIDTH` | 数字 | **是** | Width• Only for Frame Type |
| `ID` | 整数 | 否 | Serial Number |
| `GROUP_NAME` | 文字（字符串） | 否 | Boundary Group Name |
| `EDGE_FACE` | 整数 | 否 | Frame (Local Axis)• Local x: 2• Local y: 0• Local z: 1Planar & Solid (Edge Face) |
| `SPRING_TYPE` | 整数 | 否 | Spring Type• Linear: 0• Comp. -only: 1• Tens. -only: 2 |

**最简 JSON**：
```json
{
  "SSPS": {
    "ITEMS": [],
    "properties": {
      "ITEMS": {
        "items": {
          "properties": {
            "ELEM_TYPE": "<ELEM_TYPE>",
            "MODULUS": 0,
            "WIDTH": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "ITEMS": [
        {
          "ID": 1,
          "GROUP_NAME": "Service",
          "ELEM_TYPE": "FRAME",
          "EDGE_FACE": 1,
          "WIDTH": 1.2,
          "SPRING_TYPE": 0,
          "MODULUS": 500
        }
      ]
    }
  }
}
```


---

### Elastic Link — `/db/ELNK`

**方法**: POST, GET, PUT, DELETE | **参数**: 5 必填 + 7 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NODE` | Array[Integer,2] | **是** | Assigned Node Number• [i Node, j Node] |
| `LINK` | 文字（字符串） | **是** | Elastic Link type• Rail Track Interaction: "RAIL INTERACT" |
| `SDR` | Array[Number, 6] | **是** | Stiffness• [SDx, 0, 0, 0, 0, 0] |
| `MLFC` | 整数 | **是** | Defined Force-Deformation Function ID Number |
| `RLFC` | 整数 | **是** | Defined Rail-Track Interaction Function ID Number |
| `ANGLE` | 数字 | 否 | Beta Angle |
| `R_S` | Array[Boolean, 6] | 否 | Stiffness Rigid• [SDx, SDy, SDz, SRx, SRy, SRz] |
| `bSHEAR` | 是/否（布尔值） | 否 | Shear Spring Location• Direction: Dy, Dz, Ry, Rz only |
| `DR` | Array[Number, 2] | 否 | Distance Ratio from End I• [SDy, SDz] |
| `BNGR_NAME` | 文字（字符串） | 否 | Boundary Group Name |
| `DIR` | 整数 | 否 | Direction• Dy: 1• Dz: 2 |
| `DRENDI` | 数字 | 否 | Distance Ratio from End I |

**最简 JSON**：
```json
{
  "ELNK": {
    "NODE": 0,
    "LINK": "<LINK>",
    "SDR": 0,
    "MLFC": 0,
    "RLFC": 0
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "NODE": [
        1,
        2
      ],
      "LINK": "GEN",
      "ANGLE": 0,
      "R_S": [
        false,
        false,
        false,
        false,
        false,
        false
      ],
      "SDR": [
        1100,
        1200,
        1300,
        1100000,
        1200000,
        1300000
      ],
      "bSHEAR": true,
      "DR": [
        0.5,
        0.5
      ],
      "BNGR_NAME": "Service"
    },
    "2": {
      "NODE": [
        2,
        3
      ],
      "LINK": "GEN",
      "ANGLE": 0,
      "R_S": [
        true,
        true,
        true,
        true,
        true,
        true
      ],
      "SDR": [
        1100,
        1200,
        1300,
        1100000,
        1200000,
        1300000
      ],
      "bSHEAR": true,
      "DR": [
        0.5,
        0.5
      ],
      "BNGR_NAME": "Service"
    }
  }
}
```


---

### Rigid Link — `/db/RIGD`

**方法**: POST, GET, PUT, DELETE | **参数**: 3 必填 + 2 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `ITEMS` | Array[Object] | **是** | Rigid Link• Insert the data as an object |
| `DOF` | 整数 | **是** | Degree of Freedom• Rigid: 1, Free: 0◦ 6th decimal place: DX◦ 5th decimal place:  |
| `S_NODE` | 整数数组 | **是** | Slave Nodes ID Number |
| `ID` | 整数 | 否 | Serial Number |
| `GROUP_NAME` | 文字（字符串） | 否 | Boundary Group Name |

**最简 JSON**：
```json
{
  "RIGD": {
    "ITEMS": [],
    "properties": {
      "ITEMS": {
        "items": {
          "properties": {
            "DOF": 0,
            "S_NODE": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "ITEMS": [
        {
          "ID": 1,
          "GROUP_NAME": "Service",
          "DOF": 110001,
          "S_NODE": [
            2,
            3,
            4,
            5
          ]
        }
      ]
    }
  }
}
```


---

### General Link Properties — `/db/NLLP`

**方法**: POST, GET, PUT, DELETE | **参数**: 0 必填 + 28 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `PROPERTY_NAME` | 文字（字符串） | 否 | General Link Property Name |
| `APPLICATION_TYPE` | 文字（字符串） | 否 | Application Type¹⁾ |
| `APPLICATION_TYPE_D` | 文字（字符串） | 否 | Property/Devices Type¹⁾ |
| `DESC` | 文字（字符串） | 否 | Description |
| `TOTAL_WEIGHT` | 数字 | 否 | Self-Weight (Total) |
| `L_WEIGHT_RATIO` | 数字 | 否 | Lumped Weight Ratio |
| `OPT_USE_MASS` | 是/否（布尔值） | 否 | Use Mass Option |
| `TOTAL_MASS` | 数字 | 否 | Mass (Total) |
| `L_MASS_RATIO` | 数字 | 否 | Lumped Mass Ratio |
| `OPT_SHEAR_SPR_LOC` | 是/否（布尔值） | 否 | Shear Spring Location Option |
| ... | ... | ... | *还有 18 个可选参数* |

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "PROPERTY_NAME": "GL01",
      "APPLICATION_TYPE": "ELEMENT",
      "APPLICATION_TYPE_D": "SPG",
      "DESC": "Elem_Spring",
      "TOTAL_WEIGHT": 100,
      "L_WEIGHT_RATIO": 0.5,
      "OPT_USE_MASS": true,
      "TOTAL_MASS": 10,
      "L_MASS_RATIO": 0.5,
      "OPT_SHEAR_SPR_LOC": true,
      "COUPLED_INPUT_METHOD": 1,
      "DIST_RATIO_DY": 0.5,
      "DIST_RATIO_DZ": 0.5,
      "SEIS_TYPE": 0,
      "SEIS_PROP": "",
      "LDP_EFF_STIFF_COUPLED_ITEMS": [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15
      ],
      "LDP_EFF_DAMPING_COUPLED_ITEMS": [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0
      ],
      "ITEMS": [
        {
          "LINEAR_PROP": true,
          "EFF_STIFF": 1100,
          "EFF_DAMPING": 0,
          "NONLINEAR_PROP": false
        },
        {
          "LINEAR_PROP": true,
          "EFF_STIFF": 1200,
          "EFF_DAMPING": 0,
          "NONLINEAR_PROP": false
        },
        {
          "LINEAR_PROP": true,
          "EFF_STIFF": 1300,
          "EFF_DAMPING": 0,
          "NONLINEAR_PROP": false
        },
        {
          "LINEAR_PROP": true,
          "EFF_STIFF": 110000,
          "EFF_DAMPING": 0,
          "NONLINEAR_PROP": false
        },
        {
          "LINEAR_PROP": true,
          "EFF_STIFF": 120000,
          "EFF_DAMPING": 0,
          "NONLINEAR_PROP": false
        },
        {
          "LINEAR_PROP": true,
          "EFF_STIFF": 130000,
          "EFF_DAMPING": 0,
          "NONLINEAR_PROP": false
        }
      ]
    },
    "2": {
      "PROPERTY_NAME": "GL02",
      "APPLICATION_TYPE": "ELEMENT",
      "APPLICATION_TYPE_D": "DSP",
      "DESC": "Elem_LinearDashpot",
      "TOTAL_WEIGHT": 100,
      "L_WEIGHT_RATIO": 0.5,
      "OPT_USE_MASS": true,
      "TOTAL_MASS": 10,
      "L_MASS_RATIO": 0.5,
      "OPT_SHEAR_SPR_LOC": true,
      "COUPLED_INPUT_METHOD": 1,
      "DIST_RATIO_DY": 0.5,
      "DIST_RATIO_DZ": 0.5,
      "SEIS_TYPE": 0,
      "SEIS_PROP": "",
      "LDP_EFF_STIFF_COUPLED_ITEMS": [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0
      ],
      "LDP_EFF_DAMPING_COUPLED_ITEMS": [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15
      ],
      "ITEMS": [
        {
          "LINEAR_PROP": true,
          "EFF_STIFF": 0,
          "EFF_DAMPING": 110,
          "NONLINEAR_PROP": false
        },
        {
          "LINEAR_PROP": true,
          "EFF_STIFF": 0,
          "EFF_DAMPING": 120,
          "NONLINEAR_PROP": false
        },
        {
          "LINEAR_PROP": true,
          "EFF_STIFF": 0,
          "EFF_DAMPING": 130,
          "NONLINEAR_PROP": false
        },
        {
          "LINEAR_PROP": true,
          "EFF_STIFF": 0,
          "EFF_DAMPING": 1100,
          "NONLINEAR_PROP": false
        },
        {
          "LINEAR_PROP": true,
          "EFF_STIFF": 0,
          "EFF_DAMPING": 1200,
          "NONLINEAR_PROP": false
        },
        {
          "LINEAR_PROP": true,
          "EFF_STIFF": 0,
          "EFF_DAMPING": 1300,
          "NONLINEAR_PROP": false
        }
      ]
    },
    "3": {
      "PROPERTY_NAME": "GL03",
      "APPLICATION_TYPE": "ELEMENT",
      "APPLICATION_TYPE_D": "SLD",
      "DESC": "Elem_Spring&LinearDashPot",
      "TOTAL_WEIGHT": 100,
      "L_WEIGHT_RATIO": 0.5,
      "OPT_USE_MASS": true,
      "TOTAL_MASS": 10,
      "L_MASS_RATIO": 0.5,
      "OPT_SHEAR_SPR_LOC": true,
      "COUPLED_INPUT_METHOD": 1,
      "DIST_RATIO_DY": 0.5,
      "DIST_RATIO_DZ": 0.5,
      "SEIS_TYPE": 0,
      "SEIS_PROP": "",
      "LDP_EFF_STIFF_COUPLED_ITEMS": [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15
      ],
      "LDP_EFF_DAMPING_COUPLED_ITEMS": [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15
      ],
      "ITEMS": [
        {
          "LINEAR_PROP": true,
          "EFF_STIFF": 1100,
          "EFF_DAMPING": 110,
          "NONLINEAR_PROP": false
        },
        {
          "LINEAR_PROP": true,
          "EFF_STIFF": 1200,
          "EFF_DAMPING": 120,
          "NONLINEAR_PROP": false
        },
        {
          "LINEAR_PROP": true,
          "EFF_STIFF": 1300,
          "EFF_DAMPING": 130,
          "NONLINEAR_PROP": false
        },
        {
          "LINEAR_PROP": true,
          "EFF_STIFF": 110000,
          "EFF_DAMPING": 1100,
          "NONLINEAR_PROP": false
        },
        {
          "LINEAR_PROP": true,
          "EFF_STIFF": 120000,
          "EFF_DAMPING": 1200,
          "NONLINEAR_PROP": false
        },
        {
          "LINEAR_PROP": true,
          "EFF_STIFF": 130000,
          "EFF_DAMPING": 1300,
          "NONLINEAR_PROP": false
        }
      ]
    }
  }
}
```


---

### General Link — `/db/NLNK`

**方法**: POST, GET, PUT, DELETE | **参数**: 8 必填 + 4 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NODE1` | 整数 | **是** | Node 1 ID Number |
| `NODE2` | 整数 | **是** | Node 2 ID Number |
| `PROP_NAME` | 文字（字符串） | **是** | General Link Property Name |
| `REF_SYSTEM` | 整数 | **是** | Reference Coordinate System• Element: 0• Global: 1 |
| `INPUT_METHOD` | 整数 | **是** | Input Method• Vector: 2 |
| `ANGLE_VALUES` | Array[Object] | **是** | Angle• Insert the data as an object |
| `POINT_VALUES` | Array[Object, 2] | **是** | Points• Insert the data as an object• [V1, V2] |
| `VALUE` | Array[Number,3] | **是** | Point Values• [X, Y, Z] |
| `IEHP_NAME` | 文字（字符串） | 否 | Inelastic Hinge Property Name |
| `BETA_ANGLE` | 数字 | 否 | Beta Angle |
| `VECTOR_VALUES` | Array | 否 | Vector(V1X~Z,V2X~Z) |
| `GROUP_NAME` | 文字（字符串） | 否 | Boundary Group Name |

**最简 JSON**：
```json
{
  "NLNK": {
    "NODE1": 0,
    "NODE2": 0,
    "PROP_NAME": "<PROP_NAME>",
    "REF_SYSTEM": 0,
    "INPUT_METHOD": 0,
    "ANGLE_VALUES": [],
    "POINT_VALUES": [],
    "properties": {
      "ANGLE_VALUES": {
        "items": {
          "properties": {
            "VALUE": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "NODE1": 10,
      "NODE2": 11,
      "PROP_NAME": "GL01",
      "IEHP_NAME": "Inelastic_Link",
      "REF_SYSTEM": 0,
      "BETA_ANGLE": 30,
      "GROUP_NAME": "Service"
    }
  }
}
```


---

### General Link — `/db/NLNK-M1ᴴˢ⁾`

**方法**: POST, GET, PUT, DELETE | **参数**: 10 必填 + 1 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `PROP_NAME` | 文字（字符串） | **是** | General Link Property Name |
| `NODE1` | 整数 | **是** | Node Number 1 |
| `NODE2` | 整数 | **是** | Node Number 1 |
| `REF_SYSTEM` | integer (enum) | **是** | Reference Coordinate System• Element: 0• Global: 1 |
| `BETA_ANGLE` | 数字 | **是** | Beta Angle |
| `INPUT_METHOD` | integer (enum) | **是** | Input Method• Angle: 0• 3 Points: 1• Vector: 2 |
| `ANGLE_VALUES` | array [object] | **是** | Angle Value |
| `VALUE` | Array | **是** | VALUE[V1, V2] |
| `POINT_VALUES` | array [object] | **是** | Points Value |
| `VECTOR_VALUES` | array [object] | **是** | Vector Value |
| `GROUP_NAME` | 文字（字符串） | 否 | Boundary Group Name |

**最简 JSON**：
```json
{
  "PROP_NAME": "<PROP_NAME>",
  "NODE1": 0,
  "NODE2": 0,
  "REF_SYSTEM": {},
  "BETA_ANGLE": 0,
  "INPUT_METHOD": {},
  "ANGLE_VALUES": [],
  "VALUE": [],
  "POINT_VALUES": [],
  "VECTOR_VALUES": []
}
```


---

### Change General Link Property — `/db/CGLP`

**方法**: POST, GET, PUT, DELETE | **参数**: 2 必填 + 1 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `GLINK_KEY` | 整数 | **是** | General Link ID Number |
| `CHANGE_PROPERTY_NAME` | 文字（字符串） | **是** | Change Property Name |
| `GROUP_NAME` | 文字（字符串） | 否 | Boundary Group Name |

**最简 JSON**：
```json
{
  "CGLP": {
    "GLINK_KEY": 0,
    "CHANGE_PROPERTY_NAME": "<CHANGE_PROPERTY_NAME>"
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "GLINK_KEY": 1,
      "CHANGE_PROPERTY_NAME": "GL09",
      "GROUP_NAME": "Service"
    },
    "2": {
      "GLINK_KEY": 2,
      "CHANGE_PROPERTY_NAME": "GL09",
      "GROUP_NAME": "Service"
    }
  }
}
```


---

### Beam End Release — `/db/FRLS`

**方法**: POST, GET, PUT, DELETE | **参数**: 3 必填 + 5 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `ITEMS` | Array[Object] | **是** | Beam End Release• Insert the data as an object |
| `FLAG_I` | 文字（字符串） | **是** | Release i-Node |
| `FLAG_J` | 文字（字符串） | **是** | Release j-Node |
| `ID` | 整数 | 否 | Serial Number |
| `GROUP_NAME` | 文字（字符串） | 否 | Load Group Name |
| `bVALUE` | 是/否（布尔值） | 否 | Input Method• Relative: false• Value: true |
| `VALUE_I` | 数字 | 否 | Partial Fixity for i-Node• [Fx, Fy, Fz, Mx, My, Mz, Mb] |
| `VALUE_J` | 数字 | 否 | Partial Fixity for j-Node• [Fx, Fy, Fz, Mx, My, Mz, Mb] |

**最简 JSON**：
```json
{
  "FRLS": {
    "ITEMS": [],
    "properties": {
      "ITEMS": {
        "items": {
          "properties": {
            "FLAG_I": "<FLAG_I>",
            "FLAG_J": "<FLAG_J>"
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "9": {
      "ITEMS": [
        {
          "ID": 1,
          "GROUP_NAME": "Service",
          "bVALUE": true,
          "FLAG_I": "1111111",
          "VALUE_I": [
            0.1,
            0.2,
            0.3,
            0.4,
            0.5,
            0.6,
            0.7
          ],
          "FLAG_J": "1111111",
          "VALUE_J": [
            0.1,
            0.2,
            0.3,
            0.4,
            0.5,
            0.6,
            0.7
          ]
        }
      ]
    },
    "10": {
      "ITEMS": [
        {
          "ID": 1,
          "GROUP_NAME": "Service",
          "bVALUE": false,
          "FLAG_I": "1111111",
          "VALUE_I": [
            0.1,
            0.2,
            0.3,
            0.4,
            0.5,
            0.6,
            0.7
          ],
          "FLAG_J": "1111111",
          "VALUE_J": [
            0.1,
            0.2,
            0.3,
            0.4,
            0.5,
            0.6,
            0.7
          ]
        }
      ]
    }
  }
}
```


---

### Beam End Offsets — `/db/OFFS`

**方法**: POST, GET, PUT, DELETE | **参数**: 2 必填 + 8 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `ITEMS` | Array[Object] | **是** | Beam End Offsets• Insert the data as an object |
| `TYPE` | 文字（字符串） | **是** | Reference Coordinate System• Global : "GLOBAL"• Element : "ELEMENT" |
| `ID` | 整数 | 否 | Serial Number |
| `GROUP_NAME` | 文字（字符串） | 否 | Load Group Name |
| `RGDXi` | 数字 | 否 | Vector of the End Offset Distance at N1 end in GCS X-Direction |
| `RGDYi` | 数字 | 否 | End Offset Distance in the Element’s Local (+) X-Y Plane at N1 end |
| `RGDZi` | 数字 | 否 | End Offset Distance in the Element’s Local (+) X-Z Plane at N1 end |
| `RGDXj` | 数字 | 否 | Vector of the End Offset Distance at N2 end in GCS X-Direction |
| `RGDYj` | 数字 | 否 | End Offset Distance in the Element’s Local (+) X-Y Plane at N2 end |
| `RGDZj` | 数字 | 否 | End Offset Distance in the Element’s Local (+) X-Z Plane at N2 end |

**最简 JSON**：
```json
{
  "OFFS": {
    "ITEMS": [],
    "properties": {
      "ITEMS": {
        "items": {
          "properties": {
            "TYPE": "<TYPE>"
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "8": {
      "ITEMS": [
        {
          "ID": 1,
          "GROUP_NAME": "Service",
          "TYPE": "GLOBAL",
          "RGDXi": 0.11,
          "RGDYi": 0.12,
          "RGDZi": 0.13,
          "RGDXj": 0.21,
          "RGDYj": 0.22,
          "RGDZj": 0.23
        }
      ]
    }
  }
}
```


---

### Plate End Release — `/db/PRLS`

**方法**: POST, GET, PUT, DELETE | **参数**: 5 必填 + 2 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `ITEMS` | Array[Object] | **是** | Plate End Release• Insert the data as an object |
| `N1` | Array[Integer, 5] | **是** | Position - N1• Release: 1• Connect: 0• [Fx, Fy, Fz, Mx, My] |
| `N2` | Array[Integer, 5] | **是** | Position - N2• Release: 1• Connect: 0• [Fx, Fy, Fz, Mx, My] |
| `N3` | Array[Integer, 5] | **是** | Position - N3• Release: 1• Connect: 0• [Fx, Fy, Fz, Mx, My] |
| `N4` | Array[Integer, 5] | **是** | Position - N4• Release: 1• Connect: 0• [Fx, Fy, Fz, Mx, My] |
| `ID` | 整数 | 否 | Serial Number |
| `GROUP_NAME` | 文字（字符串） | 否 | Load Group Name |

**最简 JSON**：
```json
{
  "PRLS": {
    "ITEMS": [],
    "properties": {
      "ITEMS": {
        "items": {
          "properties": {
            "N1": 0,
            "N2": 0,
            "N3": 0,
            "N4": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "21": {
      "ITEMS": [
        {
          "ID": 1,
          "GROUP_NAME": "Service",
          "N1": [
            1,
            0,
            1,
            0,
            1
          ],
          "N2": [
            0,
            1,
            0,
            1,
            0
          ],
          "N3": [
            1,
            1,
            1,
            1,
            1
          ],
          "N4": [
            0,
            0,
            1,
            0,
            0
          ]
        }
      ]
    }
  }
}
```


---

### Force-Deformation Function — `/db/MLFC`

**方法**: POST, GET, PUT, DELETE | **参数**: 4 必填 + 3 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Function Name |
| `ITEMS` | Array[Object] | **是** | Function Data• Insert the data as an object |
| `X` | 数字 | **是** | X-Axis• Force: Displacement• Moment: Radian |
| `Y` | 数字 | **是** | Y-Axis |
| `TYPE` | 文字（字符串） | 否 | Type of Function• Force: "FORCE"• Moment: "MOMENT" |
| `SYMM` | 是/否（布尔值） | 否 | Symmetric Boolean• Symmetric: true• Unsymmetric: false |
| `FUNC_ID` | 整数 | 否 | Function ID |

**最简 JSON**：
```json
{
  "MLFC": {
    "NAME": "<NAME>",
    "ITEMS": [],
    "properties": {
      "ITEMS": {
        "items": {
          "properties": {
            "X": 0,
            "Y": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "NAME": "Force_Deform",
      "TYPE": "FORCE",
      "SYMM": false,
      "FUNC_ID": 0,
      "ITEMS": [
        {
          "X": -0.2,
          "Y": -1200
        },
        {
          "X": -0.1,
          "Y": -1000
        },
        {
          "X": 0,
          "Y": 0
        },
        {
          "X": 0.1,
          "Y": 1000
        },
        {
          "X": 0.2,
          "Y": 1200
        }
      ]
    }
  }
}
```


---

### Seismic Device - Viscous Damper/Oil Damper — `/db/SDVI`

**方法**: POST, GET, PUT, DELETE | **参数**: 23 必填 + 2 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `COMMON` | 对象（一组键值对） | **是** | Common Data |
| `NAME` | 文字（字符串） | **是** | Name |
| `INPUT_METHOD` | 整数 | **是** | Input Method• User Input: 0• Import Reference Database: 1 |
| `COMPANY` | 文字（字符串） | **是** | Company |
| `PRODUCT_NAME` | 文字（字符串） | **是** | Product Name |
| `TYPE_NUMBER` | 文字（字符串） | **是** | Type Number |
| `DAMPER_TYPE` | 整数 | **是** | Damper Type• Single Dashpot Model: 0• Kelvin (Voigt) Model: 1• Maxwell Model: 2 |
| `DASHPOT_TYPE` | 整数 | **是** | Dashpot Type• Linear Elastic Type: 0• Elastic Bilinear Type: 1• Exponential Func |
| `INPUT_TYPE` | 整数 | **是** | Input Type• Damping Reductio Ratio (α1): 0• Damping (C1): 1 |
| `INPUT_TYPE_EXFN` | 整数 | **是** | Input Type (Exponential Function Type) |
| `ITEM` | Array[Object,6] | **是** | Property Data• Insert the data as an object◦ Index 0: Dx◦ Index 1: Dy◦ Index 2:  |
| `OPT_DOF` | 是/否（布尔值） | **是** | Degree of Freedom |
| `CE` | 数字 | **是** | Initial Damping Coefficient |
| `P1` | 数字 | **是** | Relief Damping Force |
| `C1` | 数字 | **是** | Second Damping Coefficient |
| `ALPHA1` | 数字 | **是** | Damping Reduction Factor |
| `K0` | 数字 | **是** | TODO: K0 |
| `EXFN_PY` | 数字 | **是** | Damping Force |
| `EXFN_VY` | 数字 | **是** | Reference Velocity |
| `EXFN_DE` | 数字 | **是** | Damping Exponent |
| `EXFN_DC` | 数字 | **是** | Damping Coefficient |
| `OPT_EXFN_CE` | 是/否（布尔值） | **是** | TODO: OPT_EXEN_CE |
| `EXFN_CE` | 数字 | **是** | Initial Damping Coefficient |
| `DESC` | 文字（字符串） | 否 | Description |
| `DEVICE_TYPE` | 文字（字符串） | 否 | Device Type |

**最简 JSON**：
```json
{
  "SDVI": {
    "COMMON": {
      "NAME": "<NAME>",
      "INPUT_METHOD": 0,
      "COMPANY": "<COMPANY>",
      "PRODUCT_NAME": "<PRODUCT_NAME>",
      "TYPE_NUMBER": "<TYPE_NUMBER>"
    },
    "DAMPER_TYPE": 0,
    "DASHPOT_TYPE": 0,
    "INPUT_TYPE": 0,
    "INPUT_TYPE_EXFN": 0,
    "ITEM": [],
    "properties": {
      "ITEM": {
        "items": {
          "properties": {
            "OPT_DOF": true,
            "CE": 0,
            "P1": 0,
            "C1": 0,
            "ALPHA1": 0,
            "K0": 0,
            "EXFN_PY": 0,
            "EXFN_VY": 0,
            "EXFN_DE": 0,
            "EXFN_DC": 0,
            "OPT_EXFN_CE": true,
            "EXFN_CE": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "COMMON": {
        "NAME": "VisDamper01",
        "DESC": "",
        "INPUT_METHOD": 0,
        "COMPANY": "",
        "PRODUCT_NAME": "",
        "TYPE_NUMBER": ""
      },
      "DEVICE_TYPE": "",
      "DAMPER_TYPE": 0,
      "DASHPOT_TYPE": 0,
      "INPUT_TYPE": 0,
      "INPUT_TYPE_EXFN": 0,
      "ITEM": [
        {
          "OPT_DOF": true,
          "CE": 13000,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        }
      ]
    },
    "2": {
      "COMMON": {
        "NAME": "VisDamper02",
        "DESC": "",
        "INPUT_METHOD": 0,
        "COMPANY": "",
        "PRODUCT_NAME": "",
        "TYPE_NUMBER": ""
      },
      "DEVICE_TYPE": "",
      "DAMPER_TYPE": 0,
      "DASHPOT_TYPE": 1,
      "INPUT_TYPE": 0,
      "INPUT_TYPE_EXFN": 0,
      "ITEM": [
        {
          "OPT_DOF": true,
          "CE": 1200,
          "P1": 100,
          "C1": 600,
          "ALPHA1": 0.5,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        }
      ]
    },
    "3": {
      "COMMON": {
        "NAME": "VisDamper03",
        "DESC": "",
        "INPUT_METHOD": 0,
        "COMPANY": "",
        "PRODUCT_NAME": "",
        "TYPE_NUMBER": ""
      },
      "DEVICE_TYPE": "",
      "DAMPER_TYPE": 0,
      "DASHPOT_TYPE": 1,
      "INPUT_TYPE": 1,
      "INPUT_TYPE_EXFN": 0,
      "ITEM": [
        {
          "OPT_DOF": true,
          "CE": 1200,
          "P1": 100,
          "C1": 2.1,
          "ALPHA1": 0.00175,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        }
      ]
    },
    "4": {
      "COMMON": {
        "NAME": "VisDamper04",
        "DESC": "",
        "INPUT_METHOD": 0,
        "COMPANY": "",
        "PRODUCT_NAME": "",
        "TYPE_NUMBER": ""
      },
      "DEVICE_TYPE": "",
      "DAMPER_TYPE": 0,
      "DASHPOT_TYPE": 2,
      "INPUT_TYPE": 1,
      "INPUT_TYPE_EXFN": 0,
      "ITEM": [
        {
          "OPT_DOF": true,
          "CE": 1200,
          "P1": 100,
          "C1": 2.1,
          "ALPHA1": 0.00175,
          "K0": 0,
          "EXFN_PY": 1200,
          "EXFN_VY": 1.2,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1136.13,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1136.13
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        }
      ]
    },
    "5": {
      "COMMON": {
        "NAME": "VisDamper05",
        "DESC": "",
        "INPUT_METHOD": 0,
        "COMPANY": "",
        "PRODUCT_NAME": "",
        "TYPE_NUMBER": ""
      },
      "DEVICE_TYPE": "",
      "DAMPER_TYPE": 0,
      "DASHPOT_TYPE": 2,
      "INPUT_TYPE": 1,
      "INPUT_TYPE_EXFN": 1,
      "ITEM": [
        {
          "OPT_DOF": true,
          "CE": 1200,
          "P1": 100,
          "C1": 2.1,
          "ALPHA1": 0.00175,
          "K0": 0,
          "EXFN_PY": 1136.13,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1136.13,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1136.13
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        }
      ]
    },
    "6": {
      "COMMON": {
        "NAME": "VisDamper06",
        "DESC": "",
        "INPUT_METHOD": 0,
        "COMPANY": "",
        "PRODUCT_NAME": "",
        "TYPE_NUMBER": ""
      },
      "DEVICE_TYPE": "",
      "DAMPER_TYPE": 1,
      "DASHPOT_TYPE": 0,
      "INPUT_TYPE": 1,
      "INPUT_TYPE_EXFN": 1,
      "ITEM": [
        {
          "OPT_DOF": true,
          "CE": 1200,
          "P1": 100,
          "C1": 2.1,
          "ALPHA1": 0.00175,
          "K0": 2000,
          "EXFN_PY": 1136.13,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1136.13,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1136.13
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        }
      ]
    },
    "7": {
      "COMMON": {
        "NAME": "VisDamper07",
        "DESC": "",
        "INPUT_METHOD": 0,
        "COMPANY": "",
        "PRODUCT_NAME": "",
        "TYPE_NUMBER": ""
      },
      "DEVICE_TYPE": "",
      "DAMPER_TYPE": 1,
      "DASHPOT_TYPE": 1,
      "INPUT_TYPE": 0,
      "INPUT_TYPE_EXFN": 1,
      "ITEM": [
        {
          "OPT_DOF": true,
          "CE": 1200,
          "P1": 100,
          "C1": 960,
          "ALPHA1": 0.8,
          "K0": 2000,
          "EXFN_PY": 1136.13,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1136.13,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1136.13
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        }
      ]
    },
    "8": {
      "COMMON": {
        "NAME": "VisDamper08",
        "DESC": "",
        "INPUT_METHOD": 0,
        "COMPANY": "",
        "PRODUCT_NAME": "",
        "TYPE_NUMBER": ""
      },
      "DEVICE_TYPE": "",
      "DAMPER_TYPE": 1,
      "DASHPOT_TYPE": 1,
      "INPUT_TYPE": 1,
      "INPUT_TYPE_EXFN": 1,
      "ITEM": [
        {
          "OPT_DOF": true,
          "CE": 1200,
          "P1": 100,
          "C1": 2.1,
          "ALPHA1": 0.00175,
          "K0": 2000,
          "EXFN_PY": 1136.13,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1136.13,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1136.13
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        }
      ]
    },
    "9": {
      "COMMON": {
        "NAME": "VisDamper09",
        "DESC": "",
        "INPUT_METHOD": 0,
        "COMPANY": "",
        "PRODUCT_NAME": "",
        "TYPE_NUMBER": ""
      },
      "DEVICE_TYPE": "",
      "DAMPER_TYPE": 2,
      "DASHPOT_TYPE": 0,
      "INPUT_TYPE": 1,
      "INPUT_TYPE_EXFN": 1,
      "ITEM": [
        {
          "OPT_DOF": true,
          "CE": 1200,
          "P1": 100,
          "C1": 2.1,
          "ALPHA1": 0.00175,
          "K0": 2000,
          "EXFN_PY": 1136.13,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1136.13,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1136.13
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        }
      ]
    },
    "10": {
      "COMMON": {
        "NAME": "VisDamper10",
        "DESC": "",
        "INPUT_METHOD": 0,
        "COMPANY": "",
        "PRODUCT_NAME": "",
        "TYPE_NUMBER": ""
      },
      "DEVICE_TYPE": "",
      "DAMPER_TYPE": 2,
      "DASHPOT_TYPE": 1,
      "INPUT_TYPE": 0,
      "INPUT_TYPE_EXFN": 1,
      "ITEM": [
        {
          "OPT_DOF": true,
          "CE": 1200,
          "P1": 100,
          "C1": 960,
          "ALPHA1": 0.8,
          "K0": 2000,
          "EXFN_PY": 1136.13,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1136.13,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1136.13
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        }
      ]
    },
    "11": {
      "COMMON": {
        "NAME": "VisDamper11",
        "DESC": "",
        "INPUT_METHOD": 0,
        "COMPANY": "",
        "PRODUCT_NAME": "",
        "TYPE_NUMBER": ""
      },
      "DEVICE_TYPE": "",
      "DAMPER_TYPE": 2,
      "DASHPOT_TYPE": 1,
      "INPUT_TYPE": 1,
      "INPUT_TYPE_EXFN": 1,
      "ITEM": [
        {
          "OPT_DOF": true,
          "CE": 1200,
          "P1": 100,
          "C1": 2.1,
          "ALPHA1": 0.00175,
          "K0": 2000,
          "EXFN_PY": 1136.13,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1136.13,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1136.13
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        },
        {
          "OPT_DOF": false,
          "CE": 0,
          "P1": 0,
          "C1": 0,
          "ALPHA1": 0,
          "K0": 0,
          "EXFN_PY": 1,
          "EXFN_VY": 1,
          "EXFN_DE": 0.3,
          "EXFN_DC": 1,
          "OPT_EXFN_CE": false,
          "EXFN_CE": 1
        }
      ]
    }
  }
}
```


---

### Seismic Device - Viscoelastic Damper — `/db/SDVE`

**方法**: POST, GET, PUT, DELETE | **参数**: 22 必填 + 1 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `COMMON` | 对象（一组键值对） | **是** | Common Data |
| `NAME` | 文字（字符串） | **是** | Name |
| `INPUT_METHOD` | 整数 | **是** | Input Method• User Input: 0• Import Reference Database: 1 |
| `COMPANY` | 文字（字符串） | **是** | Company |
| `PRODUCT_NAME` | 文字（字符串） | **是** | Product Name |
| `TYPE_NUMBER` | 文字（字符串） | **是** | Type Number |
| `MATERIAL_TYPE` | 文字（字符串） | **是** | Material Type• SUMITOMO GR100: "GR100"• SUMITOMO GR300: "GR300"• SUMITOMO SR05:  |
| `SHEAR_AREA` | 数字 | **是** | Shear Area |
| `THICKNESS` | 数字 | **是** | Thickness |
| `MULTIPL` | 数字 | **是** | Multiplier |
| `DIR` | 文字（字符串） | **是** | Direction |
| `FREQ` | 数字 | **是** | Freq. |
| `STIFF_FACTOR` | 数字 | **是** | Stiffness Factor |
| `DAMP_FACTOR` | 数字 | **是** | Damping Factor |
| `REF_T` | 数字 | **是** | Reference T |
| `LIMIT_DEF` | 数字 | **是** | Limit Deform |
| `EFF_STIFF` | 数字 | **是** | Effective Stiffness |
| `EQUI_DAMP` | 数字 | **是** | Equi-Damping |
| `OPT_MOUNT_STIFF` | 是/否（布尔值） | **是** | Use Mount Stiffness |
| `MOUNT_STIFF` | 数字 | **是** | Mount Stiffness |
| `OPT_KINETIC_FRIC` | 是/否（布尔值） | **是** | Use Kinetic Fric |
| `KINETIC_FRIC` | 数字 | **是** | Kinetic Fric |
| `DESC` | 文字（字符串） | 否 | Description |

**最简 JSON**：
```json
{
  "SDVE": {
    "COMMON": {
      "NAME": "<NAME>",
      "INPUT_METHOD": 0,
      "COMPANY": "<COMPANY>",
      "PRODUCT_NAME": "<PRODUCT_NAME>",
      "TYPE_NUMBER": "<TYPE_NUMBER>"
    },
    "MATERIAL_TYPE": "<MATERIAL_TYPE>",
    "SHEAR_AREA": 0,
    "THICKNESS": 0,
    "MULTIPL": 0,
    "DIR": "<DIR>",
    "FREQ": 0,
    "STIFF_FACTOR": 0,
    "DAMP_FACTOR": 0,
    "REF_T": 0,
    "LIMIT_DEF": 0,
    "EFF_STIFF": 0,
    "EQUI_DAMP": 0,
    "OPT_MOUNT_STIFF": true,
    "MOUNT_STIFF": 0,
    "OPT_KINETIC_FRIC": true,
    "KINETIC_FRIC": 0
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "COMMON": {
        "NAME": "Viscoelastic01",
        "DESC": "",
        "INPUT_METHOD": 0,
        "PRODUCT_NAME": "",
        "TYPE_NUMBER": ""
      },
      "MATERIAL_TYPE": "GR100",
      "SHEAR_AREA": 0.2,
      "THICKNESS": 0.02,
      "MULTIPL": 1,
      "DIR": "Dx",
      "FREQ": 0,
      "STIFF_FACTOR": 1,
      "DAMP_FACTOR": 1,
      "REF_T": 20,
      "LIMIT_DEF": 0.3,
      "EFF_STIFF": 0,
      "EQUI_DAMP": 0,
      "OPT_MOUNT_STIFF": true,
      "MOUNT_STIFF": 1200,
      "OPT_KINETIC_FRIC": false,
      "KINETIC_FRIC": 0
    },
    "2": {
      "COMMON": {
        "NAME": "Viscoelastic02",
        "DESC": "",
        "INPUT_METHOD": 0,
        "PRODUCT_NAME": "",
        "TYPE_NUMBER": ""
      },
      "MATERIAL_TYPE": "GR300",
      "SHEAR_AREA": 0.2,
      "THICKNESS": 0.02,
      "MULTIPL": 1,
      "DIR": "Dy",
      "FREQ": 0,
      "STIFF_FACTOR": 1,
      "DAMP_FACTOR": 1,
      "REF_T": 20,
      "LIMIT_DEF": 0.03,
      "EFF_STIFF": 0,
      "EQUI_DAMP": 0,
      "OPT_MOUNT_STIFF": true,
      "MOUNT_STIFF": 12000,
      "OPT_KINETIC_FRIC": false,
      "KINETIC_FRIC": 0
    },
    "3": {
      "COMMON": {
        "NAME": "Viscoelastic03",
        "DESC": "",
        "INPUT_METHOD": 0,
        "PRODUCT_NAME": "",
        "TYPE_NUMBER": ""
      },
      "MATERIAL_TYPE": "SR05",
      "SHEAR_AREA": 0.2,
      "THICKNESS": 0.02,
      "MULTIPL": 1,
      "DIR": "Dy",
      "FREQ": 0,
      "STIFF_FACTOR": 1,
      "DAMP_FACTOR": 1,
      "REF_T": 20,
      "LIMIT_DEF": 0.03,
      "EFF_STIFF": 0,
      "EQUI_DAMP": 0,
      "OPT_MOUNT_STIFF": true,
      "MOUNT_STIFF": 12000,
      "OPT_KINETIC_FRIC": false,
      "KINETIC_FRIC": 0
    },
    "4": {
      "COMMON": {
        "NAME": "Viscoelastic05",
        "DESC": "",
        "INPUT_METHOD": 0,
        "PRODUCT_NAME": "",
        "TYPE_NUMBER": ""
      },
      "MATERIAL_TYPE": "GR400",
      "SHEAR_AREA": 0.2,
      "THICKNESS": 0.02,
      "MULTIPL": 1,
      "DIR": "Dy",
      "FREQ": 1,
      "STIFF_FACTOR": 1,
      "DAMP_FACTOR": 1,
      "REF_T": 20,
      "LIMIT_DEF": 0.03,
      "EFF_STIFF": 0,
      "EQUI_DAMP": 0,
      "OPT_MOUNT_STIFF": true,
      "MOUNT_STIFF": 12000,
      "OPT_KINETIC_FRIC": false,
      "KINETIC_FRIC": 0
    },
    "5": {
      "COMMON": {
        "NAME": "Viscoelastic06",
        "DESC": "",
        "INPUT_METHOD": 0,
        "PRODUCT_NAME": "",
        "TYPE_NUMBER": ""
      },
      "MATERIAL_TYPE": "CST",
      "SHEAR_AREA": 0.2,
      "THICKNESS": 0.02,
      "MULTIPL": 1,
      "DIR": "Dy",
      "FREQ": 1,
      "STIFF_FACTOR": 1,
      "DAMP_FACTOR": 1,
      "REF_T": 20,
      "LIMIT_DEF": 0.03,
      "EFF_STIFF": 0,
      "EQUI_DAMP": 0,
      "OPT_MOUNT_STIFF": true,
      "MOUNT_STIFF": 12000,
      "OPT_KINETIC_FRIC": false,
      "KINETIC_FRIC": 0
    },
    "6": {
      "COMMON": {
        "NAME": "Viscoelastic07",
        "DESC": "",
        "INPUT_METHOD": 0,
        "PRODUCT_NAME": "",
        "TYPE_NUMBER": ""
      },
      "MATERIAL_TYPE": "TRC",
      "SHEAR_AREA": 0.2,
      "THICKNESS": 0.02,
      "MULTIPL": 1,
      "DIR": "Dy",
      "FREQ": 1,
      "STIFF_FACTOR": 1,
      "DAMP_FACTOR": 1,
      "REF_T": 20,
      "LIMIT_DEF": 0.03,
      "EFF_STIFF": 0,
      "EQUI_DAMP": 0,
      "OPT_MOUNT_STIFF": true,
      "MOUNT_STIFF": 12000,
      "OPT_KINETIC_FRIC": false,
      "KINETIC_FRIC": 0
    }
  }
}
```


---

### Seismic Device - Steel Damper — `/db/SDST`

**方法**: POST, GET, PUT, DELETE | **参数**: 21 必填 + 2 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `COMMON` | 对象（一组键值对） | **是** | Common Data |
| `NAME` | 文字（字符串） | **是** | Name |
| `INPUT_METHOD` | 整数 | **是** | Input Method• User Input: 0• Import Reference Database: 1 |
| `COMPANY` | 文字（字符串） | **是** | Company |
| `PRODUCT_NAME` | 文字（字符串） | **是** | Product Name |
| `TYPE_NUMBER` | 文字（字符串） | **是** | Type Number |
| `DIR` | 文字（字符串） | **是** | Direction |
| `SDST_HYS_MODEL` | 文字（字符串） | **是** | Hysteresis Properties• Degrading Bilinear Model: "BL2"• Low Yielding Strength St |
| `K0` | 数字 | **是** | Initial Stiffness (K0) |
| `P1` | 数字 | **是** | Yield Strength (P1) |
| `KB` | 数字 | **是** | Mounting Parts Stiffness (Kb) |
| `BL2` | 对象（一组键值对） | **是** | Degrading Bilinear Model |
| `BETA` | 数字 | **是** | Exponent in Unloading Stiffness Calculation (β) |
| `LY2` | 对象（一组键值对） | **是** | Low Yielding Strength Steel Model (LY2) |
| `ALPHA2` | 数字 | **是** | Alpha2 Stiffness Factor |
| `THETA` | 数字 | **是** | Theta Strength Factor |
| `LY3` | 对象（一组键值对） | **是** | Low Yielding Strength Steel Model (LY3) |
| `GAMMA` | 数字 | **是** | Isotropic Factor (γ) |
| `IK2` | 对象（一组键值对） | **是** | Steel Isotropic-Kinematic Hardening Mode |
| `MATERIAL_TYPE` | 文字（字符串） | **是** | Material Type• SUMITOMO GR100: "GR100"• SUMITOMO GR300: "GR300"• SUMITOMO SR05:  |
| `MULTIPL` | 数字 | **是** | Multiplier |
| `DESC` | 文字（字符串） | 否 | Description |
| `ALPHA1` | 数字 | 否 | Alpha1_StiffnessFactor |

**最简 JSON**：
```json
{
  "SDST": {
    "COMMON": {
      "NAME": "<NAME>",
      "INPUT_METHOD": 0,
      "COMPANY": "<COMPANY>",
      "PRODUCT_NAME": "<PRODUCT_NAME>",
      "TYPE_NUMBER": "<TYPE_NUMBER>"
    },
    "DIR": "<DIR>",
    "SDST_HYS_MODEL": "<SDST_HYS_MODEL>",
    "K0": 0,
    "P1": 0,
    "KB": 0,
    "BL2": {
      "BETA": 0
    },
    "LY2": {},
    "LY3": {},
    "IK2": {}
  },
  "MATERIAL_TYPE": "<MATERIAL_TYPE>",
  "MULTIPL": 0
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "COMMON": {
        "NAME": "SteelDamper01",
        "DESC": "",
        "INPUT_METHOD": 0,
        "PRODUCT_NAME": "",
        "TYPE_NUMBER": ""
      },
      "DIR": "Dx",
      "SDST_HYS_MODEL": "BL2",
      "K0": 1000,
      "P1": 100,
      "ALPHA1": 0.2,
      "KB": 2000,
      "BL2": {
        "BETA": 0
      }
    },
    "2": {
      "COMMON": {
        "NAME": "SteelDamper02",
        "DESC": "",
        "INPUT_METHOD": 0,
        "PRODUCT_NAME": "",
        "TYPE_NUMBER": ""
      },
      "DIR": "Dx",
      "SDST_HYS_MODEL": "LY2",
      "K0": 1000,
      "P1": 100,
      "ALPHA1": 0.8,
      "KB": 2000,
      "LY2": {
        "ALPHA2": 0.7,
        "THETA": 1.5
      }
    },
    "3": {
      "COMMON": {
        "NAME": "SteelDamper03",
        "DESC": "",
        "INPUT_METHOD": 0,
        "PRODUCT_NAME": "",
        "TYPE_NUMBER": ""
      },
      "DIR": "Dx",
      "SDST_HYS_MODEL": "LY3",
      "K0": 1000,
      "P1": 100,
      "ALPHA1": 0.8,
      "KB": 2000,
      "LY3": {
        "ALPHA2": 0.7,
        "THETA": 1.5,
        "GAMMA": 0.5
      }
    },
    "4": {
      "COMMON": {
        "NAME": "SteelDamper04",
        "DESC": "",
        "INPUT_METHOD": 0,
        "PRODUCT_NAME": "",
        "TYPE_NUMBER": ""
      },
      "DIR": "Dx",
      "SDST_HYS_MODEL": "IK2",
      "K0": 1000,
      "P1": 100,
      "ALPHA1": 0.8,
      "KB": 2000,
      "IK2": {
        "GAMMA": 0.5
      }
    }
  }
}
```


---

### Seismic Device - Hysteretic Isolator(MSS) — `/db/SDHY`

**方法**: POST, GET, PUT, DELETE | **参数**: 17 必填 + 1 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `COMMON` | 对象（一组键值对） | **是** | Common Data |
| `NAME` | 文字（字符串） | **是** | Name |
| `INPUT_METHOD` | 整数 | **是** | Input Method• User Input: 0• Import Reference Database: 1 |
| `COMPANY` | 文字（字符串） | **是** | Company |
| `PRODUCT_NAME` | 文字（字符串） | **是** | Product Name |
| `TYPE_NUMBER` | 文字（字符串） | **是** | Type Number |
| `SDHY_HYS_MODEL` | 文字（字符串） | **是** | Hysteresis Properties |
| `MSS` | 整数 | **是** | Number of Shear Springs |
| `K0` | 数字 | **是** | K0 Initial Stiffness |
| `P1` | 数字 | **是** | P1 Yield Strength |
| `P2` | 数字 | **是** | P2 Yield Strength |
| `ALPHA1` | 数字 | **是** | Alpha1 Stiffness Factor |
| `ALPHA2` | 数字 | **是** | Alpha2 Stiffness Factor |
| `BETA` | 数字 | **是** | Beta Exponent in Unloading Stiffness Calculation |
| `Phi` | 数字 | **是** | Phi |
| `LAMBDA` | 数字 | **是** | Lambda |
| `MULTIPL` | 数字 | **是** | Multiplier |
| `DESC` | 文字（字符串） | 否 | Description |

**最简 JSON**：
```json
{
  "SDHY": {
    "COMMON": {
      "NAME": "<NAME>",
      "INPUT_METHOD": 0,
      "COMPANY": "<COMPANY>",
      "PRODUCT_NAME": "<PRODUCT_NAME>",
      "TYPE_NUMBER": "<TYPE_NUMBER>"
    },
    "SDHY_HYS_MODEL": "<SDHY_HYS_MODEL>",
    "MSS": 0,
    "K0": 0,
    "P1": 0,
    "P2": 0,
    "ALPHA1": 0,
    "ALPHA2": 0,
    "BETA": 0,
    "Phi": 0,
    "LAMBDA": 0
  },
  "MULTIPL": 0
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "COMMON": {
        "NAME": "HystereticIsolater01",
        "DESC": "",
        "INPUT_METHOD": 0,
        "PRODUCT_NAME": "",
        "TYPE_NUMBER": ""
      },
      "SDHY_HYS_MODEL": "DegradingBiLinear",
      "MSS": 8,
      "K0": 1000,
      "P1": 100,
      "P2": 0,
      "ALPHA1": 1,
      "ALPHA2": 0,
      "BETA": 0.5,
      "Phi": 0,
      "LAMBDA": 8
    },
    "2": {
      "COMMON": {
        "NAME": "HystereticIsolater02",
        "DESC": "",
        "INPUT_METHOD": 0,
        "PRODUCT_NAME": "",
        "TYPE_NUMBER": ""
      },
      "SDHY_HYS_MODEL": "NORMALTRILINEAR",
      "MSS": 8,
      "K0": 1200,
      "P1": 100,
      "P2": 200,
      "ALPHA1": 0.7,
      "ALPHA2": 0.6,
      "BETA": 0,
      "Phi": 0,
      "LAMBDA": 8
    }
  }
}
```


---

### Seismic Device - Isolator(MSS) — `/db/SDIS`

**方法**: POST, GET, PUT, DELETE | **参数**: 30 必填 + 2 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `COMMON` | 对象（一组键值对） | **是** | Common Data |
| `NAME` | 文字（字符串） | **是** | Name |
| `INPUT_METHOD` | 整数 | **是** | Input Method• User Input: 0• Import Reference Database: 1 |
| `COMPANY` | 文字（字符串） | **是** | Company |
| `PRODUCT_NAME` | 文字（字符串） | **是** | Product Name |
| `TYPE_NUMBER` | 文字（字符串） | **是** | Type Number |
| `SDIS_DEV_TYPE` | 文字（字符串） | **是** | Device Type |
| `TAU_K` | 数字 | **是** | Adjustment Parameters (τk) |
| `TAU_Q` | 数字 | **是** | Adjustment Parameters (τq) |
| `KV` | 数字 | **是** | Vertical Stiffness (Kv) |
| `LRB` | 对象（一组键值对） | **是** | LRB Data |
| `SDIS_HYS_MODEL` | 文字（字符串） | **是** | Hysteresis Properties |
| `KE` | 数字 | **是** | Initial Stiffness |
| `AR` | 数字 | **是** | Rubber Cross Section Area |
| `TR` | 数字 | **是** | Total Thickness of Rubber Laminas |
| `K0` | 数字 | **是** | Initial Stiffness |
| `K2` | 数字 | **是** | 2nd Stiffness |
| `QD` | 整数 | **是** | Index |
| `DX` | 整数 | **是** | Vertical Direction Properties |
| `NRB` | 对象（一组键值对） | **是** | NRB Data |
| `KH` | 数字 | **是** | Horizontal Stiffness |
| `SB` | 对象（一组键值对） | **是** | SB Data |
| `AS` | 数字 | **是** | Area of the Sliding Head |
| `Pi_VALUE` | 数字 | **是** | Pi |
| `MU0` | 数字 | **是** | Frictional Factor |
| `Number of Shear Springs` | 整数 | **是** | Multi-Shear Spring |
| `OPT_CONS_NONL` | 是/否（布尔值） | **是** | Use Consider Vertical Direction Nonlinearity |
| `BETA` | 数字 | **是** | Tensile Stiffness Reduction Factor Beta |
| `ALPHA` | 数字 | **是** | Tensile Stiffness Reduction Ratio Alpha |
| `SIGMA_V` | 数字 | **是** | Tensile Limit Strength |
| `DESC` | 文字（字符串） | 否 | Description |
| `MSS` | 整数 | 否 | NumberofShearSprings |

**最简 JSON**：
```json
{
  "SDIS": {
    "COMMON": {
      "NAME": "<NAME>",
      "INPUT_METHOD": 0,
      "COMPANY": "<COMPANY>",
      "PRODUCT_NAME": "<PRODUCT_NAME>",
      "TYPE_NUMBER": "<TYPE_NUMBER>"
    },
    "SDIS_DEV_TYPE": "<SDIS_DEV_TYPE>",
    "TAU_K": 0,
    "TAU_Q": 0,
    "KV": 0,
    "LRB": {
      "SDIS_HYS_MODEL": "<SDIS_HYS_MODEL>",
      "KE": 0,
      "K2": 0
    },
    "NRB": {
      "KH": 0
    },
    "SB": {
      "AS": 0,
      "Pi_VALUE": 0,
      "MU0": 0
    },
    "properties": {
      "LRB": {
        "properties": {
          "DX": {
            "properties": {
              "OPT_CONS_NONL": true,
              "BETA": 0,
              "ALPHA": 0,
              "SIGMA_V": 0
            }
          }
        }
      }
    }
  },
  "Number of Shear Springs": 0
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "COMMON": {
        "NAME": "Isolator01",
        "DESC": "",
        "INPUT_METHOD": 0,
        "PRODUCT_NAME": "",
        "TYPE_NUMBER": ""
      },
      "SDIS_DEV_TYPE": "LRB",
      "MSS": 8,
      "TAU_K": 1,
      "TAU_Q": 1,
      "KV": 1,
      "LRB": {
        "SDIS_HYS_MODEL": "MB",
        "KE": 0,
        "AR": 1e-06,
        "TR": 0.001,
        "K0": 1,
        "K2": 1,
        "QD": 0.001
      }
    },
    "2": {
      "COMMON": {
        "NAME": "Isolator02",
        "DESC": "",
        "INPUT_METHOD": 0,
        "PRODUCT_NAME": "",
        "TYPE_NUMBER": ""
      },
      "SDIS_DEV_TYPE": "LRB",
      "MSS": 8,
      "TAU_K": 1,
      "TAU_Q": 1,
      "KV": 1,
      "LRB": {
        "SDIS_HYS_MODEL": "Mod.HD",
        "KE": 1200,
        "AR": 1e-06,
        "TR": 0.001,
        "K0": 1,
        "K2": 1,
        "QD": 0.001
      }
    },
    "3": {
      "COMMON": {
        "NAME": "Isolator03",
        "DESC": "",
        "INPUT_METHOD": 0,
        "PRODUCT_NAME": "",
        "TYPE_NUMBER": ""
      },
      "SDIS_DEV_TYPE": "NRB",
      "MSS": 8,
      "TAU_K": 1,
      "KV": 1,
      "NRB": {
        "AR": 1e-06,
        "TR": 0.001,
        "KH": 1
      }
    },
    "4": {
      "COMMON": {
        "NAME": "Isolator04",
        "DESC": "",
        "INPUT_METHOD": 0,
        "PRODUCT_NAME": "",
        "TYPE_NUMBER": ""
      },
      "SDIS_DEV_TYPE": "SLD",
      "MSS": 8,
      "TAU_K": 1,
      "TAU_Q": 1,
      "KV": 1,
      "SB": {
        "AS": 1e-06,
        "K0": 1,
        "QD": 2,
        "Pi_VALUE": 0,
        "MU0": 0.01
      }
    }
  }
}
```


---

### Linear Constraints — `/db/MCON`

**方法**: POST, GET, PUT, DELETE | **参数**: 4 必填 + 2 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `ITEMS` | Array[Object] | **是** | Linear Constraints• Insert the data as an object |
| `SLAVE_TYPE` | 文字（字符串） | **是** | DOF of Constraint Node• 6th decimal place: DX• 5th decimal place: DY• 4th decima |
| `TYPE` | 文字（字符串） | **是** | Constraint Type• Explicit: "EX"• Weighted Displacement: "WD" |
| `SLAVES` | Array[Object] | **是** | Independent Nodes• Insert the data as an object |
| `ID` | 整数 | 否 | Serial Number |
| `GROUP_NAME` | 文字（字符串） | 否 | Load Group Name |

**最简 JSON**：
```json
{
  "MCON": {
    "ITEMS": [],
    "properties": {
      "ITEMS": {
        "items": {
          "properties": {
            "SLAVE_TYPE": "<SLAVE_TYPE>",
            "TYPE": "<TYPE>",
            "SLAVES": []
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "21": {
      "ITEMS": [
        {
          "ID": 1,
          "GROUP_NAME": "Service",
          "SLAVE_TYPE": "100000",
          "TYPE": "EX",
          "SLAVES": [
            {
              "NODE_KEY": 22,
              "COEFF": 0.5,
              "DOF": 0
            },
            {
              "NODE_KEY": 23,
              "COEFF": 0.5,
              "DOF": 1
            },
            {
              "NODE_KEY": 32,
              "COEFF": 0.5,
              "DOF": 2
            },
            {
              "NODE_KEY": 33,
              "COEFF": 0.5,
              "DOF": 3
            },
            {
              "NODE_KEY": 34,
              "COEFF": 0.5,
              "DOF": 4
            },
            {
              "NODE_KEY": 35,
              "COEFF": 0.5,
              "DOF": 5
            }
          ]
        }
      ]
    }
  }
}
```


---

### Panel Zone Effects — `/db/PZEF`

**方法**: POST, GET, PUT | **参数**: 3 必填 + 0 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `OPT_OFFSET` | 是/否（布尔值） | **是** | Calculation Option• Auto Calculate Panel Zone Offset Distances: true• Do not Cal |
| `OFFS_FACTOR` | 数字 | **是** | Offset Factor |
| `OUTPUT_POSITION` | 整数 | **是** | Output Position• Panel Zone: 1• Offset Position: 2 |

**最简 JSON**：
```json
{
  "PZEF": {
    "OPT_OFFSET": true,
    "OFFS_FACTOR": 0,
    "OUTPUT_POSITION": 0
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "OPT_OFFSET": true,
      "OFFS_FACTOR": 1.0,
      "OUTPUT_POSITION": 1
    }
  }
}
```


---

### Define Constraints Label Direction — `/db/CLDR`

**方法**: POST, GET, PUT | **参数**: 1 必填 + 0 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `DIR` | 整数 | **是** | Constraint Label Direction• Local x (+): 0• Local x (-): 1• Local y (+): 2• Loca |

**最简 JSON**：
```json
{
  "CLDR": {
    "DIR": 0
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "53": {
      "DIR": 0
    },
    "55": {
      "DIR": 1
    },
    "57": {
      "DIR": 2
    },
    "59": {
      "DIR": 3
    },
    "61": {
      "DIR": 4
    },
    "63": {
      "DIR": 5
    }
  }
}
```


---

### Diaphragm Disconnect — `/db/DRLS`

**方法**: POST, GET, PUT, DELETE | **参数**: 1 必填 + 1 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `Assign` | 对象（一组键值对） | **是** | Assign Object• Defines unit assignment by index.• Keys: Node Number• Value: Dumm |
| `DUMMY` | 整数 | 否 | dummy |

**最简 JSON**：
```json
{
  "Assign": {}
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {},
    "2": {},
    "5": {}
  }
}
```


---

### Static Load Cases — `/db/STLD`

**方法**: POST, GET, PUT, DELETE | **参数**: 2 必填 + 2 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Load Case Name |
| `TYPE` | 文字（字符串） | **是** | Load Type¹⁾ |
| `NO` | 整数 | 否 | Ordering Index in GUI |
| `DESC` | 文字（字符串） | 否 | Description |

**最简 JSON**：
```json
{
  "STLD": {
    "NAME": "<NAME>",
    "TYPE": "<TYPE>"
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "NAME": "DL",
      "TYPE": "D",
      "DESC": "DeadLoads"
    }
  }
}
```


---

### Self-Weight — `/db/BODF`

**方法**: POST, GET, PUT, DELETE | **参数**: 2 必填 + 1 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `LCNAME` | 文字（字符串） | **是** | Load Case Name |
| `FV` | Array[Number, 3] | **是** | Self-Weight Factor• [X, Y, Z] |
| `GROUP_NAME` | 文字（字符串） | 否 | Load Group Name |

**最简 JSON**：
```json
{
  "BODF": {
    "LCNAME": "<LCNAME>",
    "FV": 0
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "2": {
      "LCNAME": "D",
      "GROUP_NAME": "",
      "FV": [
        0,
        0,
        -1
      ]
    }
  }
}
```


---

### Nodal Loads — `/db/CNLD`

**方法**: POST, GET, PUT, DELETE | **参数**: 2 必填 + 8 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `ITEMS` | Array[Object] | **是** | Nodal Load• Insert the data as an object |
| `LCNAME` | 文字（字符串） | **是** | Load Case Name |
| `ID` | 整数 | 否 | Serial Number |
| `GROUP_NAME` | 文字（字符串） | 否 | Load Group Name |
| `FX` | 数字 | 否 | Nodal Load - FX |
| `FY` | 数字 | 否 | Nodal Load - FY |
| `FZ` | 数字 | 否 | Nodal Load - FZ |
| `MX` | 数字 | 否 | Nodal Load - MX |
| `MY` | 数字 | 否 | Nodal Load - MY |
| `MZ` | 数字 | 否 | Nodal Load - MZ |

**最简 JSON**：
```json
{
  "CNLD": {
    "ITEMS": [],
    "properties": {
      "ITEMS": {
        "items": {
          "properties": {
            "LCNAME": "<LCNAME>"
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "8": {
      "ITEMS": [
        {
          "ID": 1,
          "LCNAME": "D",
          "GROUP_NAME": "",
          "FX": 10,
          "FY": 20,
          "FZ": 30,
          "MX": -40,
          "MY": -50,
          "MZ": -60
        }
      ]
    }
  }
}
```


---

### Beam Loads — `/db/BMLD`

**方法**: POST, GET, PUT, DELETE | **参数**: 6 必填 + 14 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `ITEMS` | Array[Object] | **是** | Beam Loads• Insert the data as an object |
| `LCNAME` | 文字（字符串） | **是** | Load Case Name |
| `CMD` | 文字（字符串） | **是** | Load Classification• Element Beam Loads: "BEAM"• Line Beam Loads: "LINE"• Typica |
| `TYPE` | 文字（字符串） | **是** | Load Type• Concentrated Forces: "CONLOAD"• Concentrated Moments / Torsions: "CON |
| `DIRECTION` | 文字（字符串） | **是** | Direction• Local x: "LX"• Local y: "LY"• Local z: "LZ"• Global X: "GX"• Global Y |
| `ECCEN_DIR` | 文字（字符串） | **是** | Eccentricity Direction• Local y: "LY"• Local z: "LZ"• Global X: "GX"• Global Y:  |
| `ID` | 整数 | 否 | Serial Number |
| `GROUP_NAME` | 文字（字符串） | 否 | Load Group Name |
| `USE_PROJECTION` | 是/否（布尔值） | 否 | Projection |
| `D` | Array[Number,4] | 否 | Distance• [x1, x2, x3, x4] |
| `P` | Array[Number,4] | 否 | Load• [v1, v2, v3, v4] |
| `USE_ECCEN` | 是/否（布尔值） | 否 | Eccentricity |
| `ECCEN_TYPE` | 整数 | 否 | Eccentricity Type• Centroid: 0• Offset: 1 |
| `I_END` | 数字 | 否 | Distance I-End |
| `USE_J_END` | 是/否（布尔值） | 否 | J-End Option |
| `J_END` | 数字 | 否 | Distance J-End |
| ... | ... | ... | *还有 4 个可选参数* |

**最简 JSON**：
```json
{
  "BMLD": {
    "ITEMS": [],
    "properties": {
      "ITEMS": {
        "items": {
          "properties": {
            "LCNAME": "<LCNAME>",
            "CMD": "<CMD>",
            "TYPE": "<TYPE>",
            "DIRECTION": "<DIRECTION>",
            "ECCEN_DIR": "<ECCEN_DIR>"
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "115": {
      "ITEMS": [
        {
          "ID": 1,
          "LCNAME": "L",
          "GROUP_NAME": "",
          "CMD": "BEAM",
          "TYPE": "UNILOAD",
          "DIRECTION": "GZ",
          "USE_PROJECTION": false,
          "USE_ECCEN": false,
          "D": [
            0,
            1,
            0,
            0
          ],
          "P": [
            -50,
            -50,
            0,
            0
          ]
        }
      ]
    }
  }
}
```


---

### Specified Displacements of Support — `/db/SDSP`

**方法**: POST, GET, PUT, DELETE | **参数**: 2 必填 + 3 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `ITEMS` | Array[Object] | **是** | Specified Displacement of Support• Insert the data as an object |
| `LCNAME` | 文字（字符串） | **是** | Load Case Name |
| `ID` | 整数 | 否 | Serial Number |
| `GROUP_NAME` | 文字（字符串） | 否 | Load Group Name |
| `VALUES` | Array[Object, 6] | 否 | Displacements (Local Direction)• [Dx, Dy, Dz, Rx, Ry, Rz] |

**最简 JSON**：
```json
{
  "SDSP": {
    "ITEMS": [],
    "properties": {
      "ITEMS": {
        "items": {
          "properties": {
            "LCNAME": "<LCNAME>"
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "10": {
      "ITEMS": [
        {
          "ID": 1,
          "LCNAME": "LL",
          "GROUP_NAME": "",
          "VALUES": [
            {
              "OPT_FLAG": true,
              "DISPLACEMENT": 1.5
            },
            {
              "OPT_FLAG": true,
              "DISPLACEMENT": 1.5
            },
            {
              "OPT_FLAG": true,
              "DISPLACEMENT": 1.5
            },
            {
              "OPT_FLAG": true,
              "DISPLACEMENT": 1.5
            },
            {
              "OPT_FLAG": true,
              "DISPLACEMENT": 0.5
            },
            {
              "OPT_FLAG": true,
              "DISPLACEMENT": 0.5
            }
          ]
        }
      ]
    }
  }
}
```


---

### Nodal Masses — `/db/NMAS`

**方法**: POST, GET, PUT, DELETE | **参数**: 1 必填 + 5 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `mX` | 数字 | **是** | Translational Lumped Mass in GCS X-direction |
| `mY` | 数字 | 否 | Translational Lumped Mass in GCS Y-direction |
| `mZ` | 数字 | 否 | Translational Lumped Mass in GCS Z-direction |
| `rmX` | 数字 | 否 | Rotational Mass Moment of Inertia about GCS X-axis |
| `rmY` | 数字 | 否 | Rotational Mass Moment of Inertia about GCS Y-axis |
| `rmZ` | 数字 | 否 | Rotational Mass Moment of Inertia about GCS Z-axis |

**最简 JSON**：
```json
{
  "NMAS": {
    "mX": 0
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "mX": 1,
      "mY": 2,
      "mZ": 3,
      "rmX": 4,
      "rmY": 5,
      "rmZ": 6
    }
  }
}
```


---

### Loads to Masses — `/db/LTOM`

**方法**: POST, GET, PUT, DELETE | **参数**: 4 必填 + 5 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `DIR` | 文字（字符串） | **是** | Mass Direction• X: "X"• Y: "Y"• Z: "Z"• X, Y: "XY"• Y, Z: "YZ"• X, Z: "XZ"• X, Y |
| `vLC` | Array[Object] | **是** | Load Case List• Insert the data as an object |
| `LCNAME` | 文字（字符串） | **是** | Load Case Name |
| `FACTOR` | 数字 | **是** | Scale Factor |
| `bNODAL` | 是/否（布尔值） | 否 | Nodal Load |
| `bBEAM` | 是/否（布尔值） | 否 | Beam Load |
| `bFLOOR` | 是/否（布尔值） | 否 | Floor Load |
| `bPRES` | 是/否（布尔值） | 否 | Pressure (Hydrostatic) |
| `GRAV` | 数字 | 否 | Gravity Acceleration |

**最简 JSON**：
```json
{
  "LTOM": {
    "DIR": "<DIR>",
    "vLC": [],
    "properties": {
      "vLC": {
        "items": {
          "properties": {
            "LCNAME": "<LCNAME>",
            "FACTOR": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "DIR": "XYZ",
      "bNODAL": true,
      "bBEAM": true,
      "bFLOOR": true,
      "bPRES": true,
      "GRAV": 9.806,
      "vLC": [
        {
          "LCNAME": "D",
          "FACTOR": 1.0
        },
        {
          "LCNAME": "L",
          "FACTOR": 0.5
        }
      ]
    }
  }
}
```


---

## Nodal Body Force — `/db/NBOF`

**HTTP 方法**: POST, GET, PUT, DELETE | **参数总数**: 10（2 必填 + 8 可选）

### 1. 这是什么？（工程含义）

**Nodal Body Force** — 这是模型数据库的创建和查询操作，属于 Static Loads 类别。

Load Case Name

> 简单说：这个接口用来**Nodal Body Force**。

### 2. JSON 结构（逐层解释）

下面按照从外到内的顺序解释每一层的 JSON 结构：

```json
{
  "NBOF": {
    "LCNAME": "<LCNAME>",
    "OPT_USE_GROUP (可选)": "False",
    "GROUP_NAME (可选)": "<GROUP_NAME>",
    "KEY_NODE_ITEMS (可选)": 0,
    "OPT_NODAL_MASS (可选)": "False",
    "OPT_LOAD_TO_MASS (可选)": "False",
    "OPT_STRUCT_MASS (可选)": "False",
    "Y (可选)": "0",
    "Z (可选)": "0",
    "X": 0
  }
}
```

**第 1 层：`NBOF`** — 10 个参数在这一层

- `"LCNAME"`: 文字（字符串） — Load Case Name
- `"OPT_USE_GROUP"`: 是/否（布尔值） — Structure Group Option
- `"GROUP_NAME"`: 文字（字符串） — Structure Group Name
- `"KEY_NODE_ITEMS"`: 整数数组 — Node No. List
- `"OPT_NODAL_MASS"`: 是/否（布尔值） — Nodal Mass
- `"OPT_LOAD_TO_MASS"`: 是/否（布尔值） — Load to Mass
- `"OPT_STRUCT_MASS"`: 是/否（布尔值） — Structure Mass
- `"X"`: 数字 — X-dir. Force Factor
- ... *还有 2 个参数*


### 3. 必填 vs 可选参数

**必填参数**（不填会报错）：

| 参数名 | 类型 | JSON 路径 | 说明 |
|--------|------|-----------|------|
| `LCNAME` | 文字（字符串） | `NBOF.LCNAME` | Load Case Name |
| `X` | 数字 | `NBOF.X` | X-dir. Force Factor |

**可选参数**（填不填都行）：

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `OPT_USE_GROUP` | 是/否（布尔值） | `False` | Structure Group Option |
| `GROUP_NAME` | 文字（字符串） | `无` | Structure Group Name |
| `KEY_NODE_ITEMS` | 整数数组 | `无` | Node No. List |
| `OPT_NODAL_MASS` | 是/否（布尔值） | `False` | Nodal Mass |
| `OPT_LOAD_TO_MASS` | 是/否（布尔值） | `False` | Load to Mass |
| `OPT_STRUCT_MASS` | 是/否（布尔值） | `False` | Structure Mass |
| `Y` | 数字 | `0` | Y-dir. Force Factor |
| `Z` | 数字 | `0` | Z-dir. Force Factor |


### 4. 可选参数放在哪里？

可选参数必须放在正确的 JSON 层级中。以下是每个可选参数的具体位置：

- `OPT_USE_GROUP` 的路径：**"NBOF" → "OPT_USE_GROUP"**
  意思是：在 JSON 中依次打开 NBOF, OPT_USE_GROUP，最后填入 `OPT_USE_GROUP` 的值
- `GROUP_NAME` 的路径：**"NBOF" → "GROUP_NAME"**
  意思是：在 JSON 中依次打开 NBOF, GROUP_NAME，最后填入 `GROUP_NAME` 的值
- `KEY_NODE_ITEMS` 的路径：**"NBOF" → "KEY_NODE_ITEMS"**
  意思是：在 JSON 中依次打开 NBOF, KEY_NODE_ITEMS，最后填入 `KEY_NODE_ITEMS` 的值
- `OPT_NODAL_MASS` 的路径：**"NBOF" → "OPT_NODAL_MASS"**
  意思是：在 JSON 中依次打开 NBOF, OPT_NODAL_MASS，最后填入 `OPT_NODAL_MASS` 的值
- `OPT_LOAD_TO_MASS` 的路径：**"NBOF" → "OPT_LOAD_TO_MASS"**
  意思是：在 JSON 中依次打开 NBOF, OPT_LOAD_TO_MASS，最后填入 `OPT_LOAD_TO_MASS` 的值
- `OPT_STRUCT_MASS` 的路径：**"NBOF" → "OPT_STRUCT_MASS"**
  意思是：在 JSON 中依次打开 NBOF, OPT_STRUCT_MASS，最后填入 `OPT_STRUCT_MASS` 的值
- `Y` 的路径：**"NBOF" → "Y"**
  意思是：在 JSON 中依次打开 NBOF, Y，最后填入 `Y` 的值
- `Z` 的路径：**"NBOF" → "Z"**
  意思是：在 JSON 中依次打开 NBOF, Z，最后填入 `Z` 的值

**理解 JSON 路径**：想象你在文件夹里找文件——`A.B.C` 就像 `A文件夹/B文件夹/C文件`。


### 5. 参数之间的关系

以下参数之间存在关联关系：

这个接口的参数之间没有复杂的依赖关系。每个参数可以独立填写。

**一般规律**：`TYPE` 类参数决定结构类型，然后 `PARAM` 类参数的格式由 `TYPE` 决定。


### 6. 最小可运行代码

以下是能跑起来的最简代码：

```python
import requests
import urllib3
urllib3.disable_warnings()  # 关闭 SSL 警告

# MIDAS 服务地址（根据你的产品修改端口）
BASE = "https://127.0.0.1:1102"

url = f"{BASE}/db/NBOF"

# JSON 数据 — 这是你要发给 MIDAS 的内容
data = {
#     "NBOF": {
#         "LCNAME": "<LCNAME>",
#         "X": 0
#     }
# }

# 发送请求
r = requests.post(url, json=data, verify=False)

# 检查结果
if r.status_code == 200:
    print("成功！")
    print(r.json())
else:
    print(f"失败，错误码：{r.status_code}")
```

**运行前确认**：MIDAS Civil 已经打开，并且加载了一个项目。


### 7. 工程意义

参数化建模的核心。一旦掌握，你可以用几十行代码代替几小时的点鼠标操作。参数变化时，重新生成模型只需要几秒钟。

### 8. 常见错误

使用这个接口时最容易犯的错误：

1. **忘记填必填参数**：LCNAME、X 是必填的，漏掉任何一个都会报错。
3. **数组格式错误**：KEY_NODE_ITEMS 需要数组类型，要写成 `[1, 2, 3]` 而不是 `1, 2, 3`。
4. **URL 写错**：确认路径是 `/db/NBOF`——多一个斜杠或少一个都会导致 404 错误。


### 9. Python 批量生成案例

如果你需要创建多个类似的调用（例如创建 100 个节点），可以用列表+循环来生成：

```python
import requests
import urllib3
urllib3.disable_warnings()

BASE = "https://127.0.0.1:1102"

# 定义基础数据模板
def make_data(**kwargs):
    """根据参数生成 Nodal Body Force 的 JSON 数据。"""
    data = {"NBOF": {"LCNAME": "<LCNAME>", "X": 0}}
    # 在这里修改需要变化的值
    for key, value in kwargs.items():
        # 根据 json_path 更新对应位置的值
        pass  # 具体逻辑见下面的 for 循环例子
    return data

# 批量调用
results = []
for i in range(1, 11):  # 生成 10 个
    data = make_data()    # 在这里修改参数
    r = requests.post(f"{BASE}/db/NBOF", json=data, verify=False)
    results.append(r.json())
    print(f'第 {i} 个完成')
```


### 10. for 循环优化案例

对于批量操作，直接写 for 循环每次发一个请求效率不够高。以下是优化技巧：

**技巧 1：利用 Assign 结构一次发送多个对象**

很多 DB 接口支持在一次请求中发送多个对象，通过 `Assign` 下的编号 `"1"`, `"2"`, ... 区分。

```python
# ❌ 慢：循环 100 次，每次发一个节点
for i in range(100):
    data = {"Assign": {"1": {"X": i, "Y": 0, "Z": 0}}}
    requests.post(url, json=data, verify=False)

# ✅ 快：一次发 100 个节点
nodes = {}
for i in range(100):
    nodes[str(i+1)] = {"X": i, "Y": 0, "Z": 0}
data = {"Assign": nodes}
requests.post(url, json=data, verify=False)
```

**技巧 2：使用列表推导式预生成数据**（在 Nodal Body Force 中适用）

```python
# 列表推导式 — 一行代码生成所有节点的坐标
nodes = {str(i+1): {"X": i*5.0, "Y": 0, "Z": 0} for i in range(100)}
data = {"Assign": nodes}
requests.post(url, json=data, verify=False)
```

**通用优化原则**：

1. 能一次发多个就不要循环发单个
2. 用 `requests.Session()` 代替 `requests.post()` 做批量请求
3. 先生成所有数据，再统一发送，不要在循环里逐个生成+发送



---

### Define Pressure Load Type — `/db/PSLT`

**方法**: POST, GET, PUT, DELETE | **参数**: 7 必填 + 3 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Pressure Load Type Name |
| `DESC` | 文字（字符串） | **是** | Description |
| `ELEM_TYPE` | 文字（字符串） | **是** | Element Type• "Plate/Plane Stress (Face)"• "Plate/Plane Stress (Edge)"• "Solid ( |
| `PRESSURE_LOAD_ITEMS` | Array[Object] | **是** | Pressure Load• Insert the data as an object |
| `CMD` | 文字（字符串） | **是** | Load Case Name |
| `LOADTYPE` | 文字（字符串） | **是** | Load Type• "Uniform"• "Linear" |
| `LOAD_P1` | 数字 | **是** | Load: P1¹⁾ |
| `LOAD_P2` | 数字 | 否 | Load: P2¹⁾ |
| `LOAD_P3` | 数字 | 否 | Load: P3¹⁾ |
| `LOAD_P4` | 数字 | 否 | Load: P4¹⁾ |

**最简 JSON**：
```json
{
  "PSLT": {
    "NAME": "<NAME>",
    "DESC": "<DESC>",
    "ELEM_TYPE": "<ELEM_TYPE>",
    "PRESSURE_LOAD_ITEMS": [],
    "properties": {
      "PRESSURE_LOAD_ITEMS": {
        "items": {
          "properties": {
            "LOADTYPE": "<LOADTYPE>",
            "LOAD_P1": 0
          }
        }
      }
    }
  },
  "CMD": "<CMD>"
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "NAME": "Element_Type1",
      "DESC": "Plate/PlaneStress(Face)",
      "ELEM_TYPE": "Plate/PlaneStress(Face)",
      "PRESSURE_LOAD_ITEMS": [
        {
          "LOADCASENAME": "DC",
          "LOADTYPE": "Uniform",
          "LOAD_P1": -20
        },
        {
          "LOADCASENAME": "DW",
          "LOADTYPE": "Linear",
          "LOAD_P1": -1,
          "LOAD_P2": -2,
          "LOAD_P3": -3,
          "LOAD_P4": 4
        },
        {
          "LOADCASENAME": "SIDL",
          "LOADTYPE": "Uniform",
          "LOAD_P1": -15
        },
        {
          "LOADCASENAME": "LL",
          "LOADTYPE": "Linear",
          "LOAD_P1": -4,
          "LOAD_P2": -5,
          "LOAD_P3": -4,
          "LOAD_P4": -5
        },
        {
          "LOADCASENAME": "EV",
          "LOADTYPE": "Uniform",
          "LOAD_P1": 20
        },
        {
          "LOADCASENAME": "EH",
          "LOADTYPE": "Linear",
          "LOAD_P1": 10,
          "LOAD_P2": 10,
          "LOAD_P3": 11,
          "LOAD_P4": 12
        },
        {
          "LOADCASENAME": "BR",
          "LOADTYPE": "Uniform",
          "LOAD_P1": 6
        },
        {
          "LOADCASENAME": "CR",
          "LOADTYPE": "Linear",
          "LOAD_P1": 7,
          "LOAD_P2": 8,
          "LOAD_P3": 9,
          "LOAD_P4": 10
        }
      ]
    }
  }
}
```


---

### Assign Pressure Loads — `/db/PRES`

**方法**: POST, GET, PUT, DELETE | **参数**: 6 必填 + 7 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `ITEMS` | Array[Object] | **是** | Pressure Loads• Insert the data as an object |
| `LCNAME` | 文字（字符串） | **是** | Load Case Name |
| `FACE_EDGE_TYPE` | 文字（字符串） | **是** | Pressure Type• Pressure Face: "FACE"• Pressure Edge: "EDGE"• Solid: "PRES" |
| `EDGE_FACE` | 整数 | **是** | Element Type: Solid• Face #1: 1• Face #2: 2• Face #3: 3• Face #4: 4• Face #5: 5• |
| `FORCES` | Array[Number, 5] | **是** | Uniform Load• [PU, 0, 0, 0, 0]Linear Load• [0, P1, P2, P3, P4] |
| `EDGE_LOADS` | Array[Number, 3] | **是** | Uniform Load• [EPU, 0, 0]Linear Load• [0, EP1, EP2] |
| `ID` | 整数 | 否 | Serial Number |
| `GROUP_NAME` | 文字（字符串） | 否 | Load Group Name |
| `CMD` | 文字（字符串） | 否 | Command Type• Pressure Loads: "PRES" |
| `ELEM_TYPE` | 文字（字符串） | 否 | Element Type• Plate/Plane Stress: "PLATE"• Solid: "SOLID"• Plane Strain: "PLANE" |
| `DIRECTION` | 文字（字符串） | 否 | Direction¹⁾• Normal: "NORMAL"• Local x: "LX"• Local y: "LY"• Local z: "LZ"• Glob |
| `VECTORS` | Array[Number, 3] | 否 | Vector• if "DIRECTION" is "VECTOR"• [X, Y, Z] |
| `OPT_PROJECTION` | 是/否（布尔值） | 否 | Projection Option• GX, GY, GZ only |

**最简 JSON**：
```json
{
  "PRES": {
    "ITEMS": [],
    "properties": {
      "ITEMS": {
        "items": {
          "properties": {
            "LCNAME": "<LCNAME>",
            "FACE_EDGE_TYPE": "<FACE_EDGE_TYPE>",
            "EDGE_FACE": 0,
            "FORCES": 0,
            "EDGE_LOADS": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "116": {
      "ITEMS": [
        {
          "ID": 1,
          "LCNAME": "Element_Type1",
          "GROUP_NAME": "",
          "CMD": "PRES",
          "ELEM_TYPE": "PLATE",
          "FACE_EDGE_TYPE": "FACE",
          "DIRECTION": "LZ",
          "FORCES": [
            -10,
            0,
            0,
            0,
            0
          ]
        }
      ]
    }
  }
}
```


---

### Define Plane Load Type — `/db/PNLD`

**方法**: POST, GET, PUT, DELETE | **参数**: 7 必填 + 8 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Load Type Name |
| `LTYPE` | 文字（字符串） | **是** | Load Type• Point: "POINT"• Line: "LINE"• Area: "AREA" |
| `POINTLOAD` | Array[Object] | **是** | Point Loads• Insert the data as an object |
| `LINELOAD` | 对象（一组键值对） | **是** | Line Loads |
| `AREALOAD` | 对象（一组键值对） | **是** | Area Loads |
| `COPY_X` | 数字数组 | **是** | Copy in X-Direction |
| `COPY_Y` | 数字数组 | **是** | Copy in Y-Direction |
| `DESC` | 文字（字符串） | 否 | Description |
| `bUNIFORM` | 是/否（布尔值） | 否 | Load Type• Uniform: true• Trapezoidal: false |
| `X` | Array[Number, 4] | 否 | Coordinates of X1, X2, X3, X4• [X1, X2, X3, X4] |
| `Y` | Array[Number, 4] | 否 | Coordinates of Y1, Y2, Y3, Y4• [Y1, Y2, Y3, Y4] |
| `F` | Array[Number, 2] | 否 | Force• Uniform: [F1]• Trapezoidal: [F1, F2] |
| `b3PNT` | 是/否（布尔值） | 否 | Points• 3 points: true• 4 points: false |
| `LOAD` | Array[Number, 4] | 否 | Load• Uniform: [F1]• Trapezoidal: [F1, F2, F3, F4] |
| `SEQ` | 整数 | 否 | Sequence Number (Unique) |

**最简 JSON**：
```json
{
  "PNLD": {
    "NAME": "<NAME>",
    "LTYPE": "<LTYPE>",
    "POINTLOAD": [],
    "LINELOAD": {},
    "AREALOAD": {},
    "COPY_X": 0,
    "COPY_Y": 0
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "NAME": "Point_examples",
      "DESC": "API_example",
      "LTYPE": "POINT",
      "POINTLOAD": [
        {
          "X": 0,
          "Y": 0,
          "F": -10
        },
        {
          "X": 1,
          "Y": -1,
          "F": 10.5
        }
      ],
      "COPY_X": [
        5,
        5,
        5
      ],
      "COPY_Y": [
        4.5
      ],
      "SEQ": 1
    }
  }
}
```


---

### Assign Plane Loads — `/db/PNLA`

**方法**: POST, GET, PUT, DELETE | **参数**: 11 必填 + 5 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `LCNAME` | 文字（字符串） | **是** | Load Case Name |
| `LOAD_GROUP` | 文字（字符串） | **是** | Load Group Name |
| `PNLD_KEY` | 整数 | **是** | Defined Plane Load Key |
| `ELEM_TYPE` | 文字（字符串） | **是** | Element Type• Plate element: "PLATE"• Solid element: "SOLID" |
| `POINT_ORIGIN` | Array[Number, 3] | **是** | First Point (Origin)• [x, y, z] |
| `AXIS_X` | Array[Number, 3] | **是** | Second Point (on x Axis)• [x, y, z] |
| `AXIS_Y` | Array[Number, 3] | **是** | Third Point (on x-y Plane)• [x, y, z] |
| `TOL` | 数字 | **是** | Tolerance |
| `SELECT_TYPE` | 文字（字符串） | **是** | Element Selection Type• Elements on the loading plane: "ON_PLANE"• Group: "IN_GR |
| `LOAD_DIR` | 文字（字符串） | **是** | Load Direction• Normal (Loading Plane): "NORMAL_PLANE"• Normal (Element): "NORMA |
| `PROJECT_TYPE` | 文字（字符串） | **是** | Projection Type• No: "NO"• Load Direction: "LOAD_DIR"• Loading Plane: "LOAD_PLAN |
| `ELEM_GROUP` | 文字（字符串） | 否 | Element Group Name |
| `FACE_NO` | 整数 | 否 | Solid Face No. (1~6)• Face #1: 1• Face #2: 2• Face #3: 3• Face #4: 4• Face #5: 5 |
| `bDEFINE_NODE` | 是/否（布尔值） | 否 | Node Defining Loading Area |
| `CONNECT_NODE` | Array[Integer, 15] | 否 | Loading Boundary Connecting Node |
| `DESC` | 文字（字符串） | 否 | Description |

**最简 JSON**：
```json
{
  "PNLA": {
    "LCNAME": "<LCNAME>",
    "LOAD_GROUP": "<LOAD_GROUP>",
    "PNLD_KEY": 0,
    "ELEM_TYPE": "<ELEM_TYPE>",
    "POINT_ORIGIN": 0,
    "AXIS_X": 0,
    "AXIS_Y": 0,
    "TOL": 0,
    "SELECT_TYPE": "<SELECT_TYPE>",
    "LOAD_DIR": "<LOAD_DIR>",
    "PROJECT_TYPE": "<PROJECT_TYPE>"
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "LCNAME": "AssignPlaneExample",
      "PNLD_KEY": 1,
      "ELEM_TYPE": "PLATE",
      "POINT_ORIGIN": [
        18,
        2,
        0
      ],
      "AXIS_X": [
        19,
        2,
        0
      ],
      "AXIS_Y": [
        19,
        3,
        0
      ],
      "TOL": 0.0009144,
      "SELECT_TYPE": "ON_PLANE",
      "LOAD_DIR": "GLOBAL_Z",
      "PROJECT_TYPE": "LOAD_DIR",
      "DESC": "Elements"
    }
  }
}
```


---

### Define Floor Load Type — `/db/FBLD`

**方法**: POST, GET, PUT, DELETE | **参数**: 4 必填 + 2 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Floor Load Type Name |
| `ITEM` | Array[Object] | **是** | Floor Loads• Insert the data as an object |
| `LCNAME` | 文字（字符串） | **是** | Load Case Name |
| `FLOOR_LOAD` | 数字 | **是** | Floor Load |
| `DESC` | 文字（字符串） | 否 | Description |
| `OPT_SUB_BEAM_WEIGHT` | 是/否（布尔值） | 否 | Consider Sub Beam Weight |

**最简 JSON**：
```json
{
  "FBLD": {
    "NAME": "<NAME>",
    "ITEM": [],
    "properties": {
      "ITEM": {
        "items": {
          "properties": {
            "LCNAME": "<LCNAME>",
            "FLOOR_LOAD": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "NAME": "Floor_example",
      "DESC": "",
      "ITEM": [
        {
          "LCNAME": "DC",
          "FLOOR_LOAD": 10,
          "OPT_SUB_BEAM_WEIGHT": true
        },
        {
          "LCNAME": "DW",
          "FLOOR_LOAD": 20,
          "OPT_SUB_BEAM_WEIGHT": true
        }
      ]
    }
  }
}
```


---

### Assign Floor Loads — `/db/FBLA`

**方法**: POST, GET, PUT, DELETE | **参数**: 3 必填 + 11 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `FLOOR_LOAD_TYPE_NAME` | 文字（字符串） | **是** | Floor Load Type Name |
| `FLOOR_DIST_TYPE` | 整数 | **是** | Distribution Type• One Way: 1• Two Way: 2• Polygon-Centroid: 3• Polygon-Length:  |
| `NODES` | 整数数组 | **是** | Nodes defining Loading Area |
| `LOAD_ANGLE` | 数字 | 否 | Load Angle(A1) |
| `SUB_BEAM_NUM` | 整数 | 否 | No. of Sub Beams |
| `SUB_BEAM_ANGLE` | 数字 | 否 | Sub-Beam Angle (A2) |
| `UNIT_SELF_WEIGHT` | 数字 | 否 | UnitSelfWeight |
| `DIR` | 文字（字符串） | 否 | Load Direction• Local x: "LX"• Local y: "LY"• Local z: "LZ"• Global X: "GX"• Glo |
| `OPT_PROJECTION` | 是/否（布尔值） | 否 | Projection Boolean |
| `DESC` | 文字（字符串） | 否 | Description |
| `OPT_EXCLUDE_INNER_ELEM_AREA` | 是/否（布尔值） | 否 | Exclude Inner Element of Area |
| `OPT_ALLOW_POLYGON_TYPE_UNIT_AREA` | 是/否（布尔值） | 否 | Allow Polygon Type Unit Angle |
| `GROUP_NAME` | 文字（字符串） | 否 | Load Group Name |
| ... | ... | ... | *还有 1 个可选参数* |

**最简 JSON**：
```json
{
  "FBLA": {
    "FLOOR_LOAD_TYPE_NAME": "<FLOOR_LOAD_TYPE_NAME>",
    "FLOOR_DIST_TYPE": 0,
    "NODES": 0
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "FLOOR_LOAD_TYPE_NAME": "Floor_example",
      "FLOOR_DIST_TYPE": 1,
      "LOAD_ANGLE": 0,
      "SUB_BEAM_NUM": 2,
      "SUB_BEAM_ANGLE": 90,
      "UNIT_SELF_WEIGHT": 10,
      "DIR": "GZ",
      "OPT_PROJECTION": false,
      "DESC": "",
      "OPT_EXCLUDE_INNER_ELEM_AREA": true,
      "GROUP_NAME": "LoadGroup2",
      "NODES": [
        508,
        509,
        511,
        510
      ]
    }
  }
}
```


---

### Finishing Material Loads — `/db/FMLD`

**方法**: POST, GET, PUT, DELETE | **参数**: 4 必填 + 6 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `ITEMS` | Array[Object] | **是** | Finishing Material Loads• Insert the data as an object |
| `LCNAME` | 文字（字符串） | **是** | Load Case Name |
| `COVERING_RANGE` | Array[String, 4] | **是** | Covering Range• Full: "FULL"• Half: "HALF"• [+x dir. face, -y dir. face, -x dir. |
| `SCALE_FACTOR` | 数字 | **是** | Scale Factor |
| `ID` | 整数 | 否 | Serial Number |
| `GROUP_NAME` | 文字（字符串） | 否 | Load Group Name |
| `COVERING_TYPE` | 文字（字符串） | 否 | Covering Type• Envelop: "ENVELOP"• Fill: "FILL"• Surround: "SURROUND" |
| `THICKNESS` | 数字 | 否 | Covering Thickness (d) |
| `DENSITY` | 数字 | 否 | Filling Property (Density) |
| `DIR` | 文字（字符串） | 否 | Direction• Global X: "GX"• Global Y: "GY"• Global Z: "GZ" |

**最简 JSON**：
```json
{
  "FMLD": {
    "ITEMS": [],
    "properties": {
      "ITEMS": {
        "items": {
          "properties": {
            "LCNAME": "<LCNAME>",
            "COVERING_RANGE": "<COVERING_RANGE>",
            "SCALE_FACTOR": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "448": {
      "ITEMS": [
        {
          "ID": 1,
          "LCNAME": "FMLD_examples",
          "GROUP_NAME": "LoadGroups",
          "COVERING_TYPE": "ENVELOP",
          "COVERING_RANGE": [
            "HALF",
            "HALF",
            "FULL",
            "FULL"
          ],
          "THICKNESS": 0.2,
          "DENSITY": 24.5,
          "DIR": "GZ",
          "SCALE_FACTOR": -1
        },
        {
          "ID": 2,
          "LCNAME": "FMLD_examples",
          "GROUP_NAME": "LoadGroups",
          "COVERING_TYPE": "FILL",
          "COVERING_RANGE": [
            "HALF",
            "HALF",
            "FULL",
            "FULL"
          ],
          "THICKNESS": 0.2,
          "DENSITY": 24.5,
          "DIR": "GZ",
          "SCALE_FACTOR": -1
        },
        {
          "ID": 3,
          "LCNAME": "FMLD_examples",
          "GROUP_NAME": "LoadGroups",
          "COVERING_TYPE": "SURROUND",
          "COVERING_RANGE": [
            "HALF",
            "HALF",
            "FULL",
            "FULL"
          ],
          "THICKNESS": 0.2,
          "DENSITY": 24.5,
          "DIR": "GZ",
          "SCALE_FACTOR": -1
        }
      ]
    }
  }
}
```


---

### Parameter of Soil Properties — `/db/POSP`

**方法**: POST, GET, PUT, DELETE | **参数**: 11 必填 + 2 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Parameters of Soil Properties Name |
| `GROUND_LEVEL` | 数字 | **是** | Level of ground surface |
| `BEDROCK_LEVEL` | 数字 | **是** | Level of Bedrock |
| `FOOTING_LEVEL` | 数字 | **是** | Level of footing bottom |
| `ITEMS` | Arrary[Object] | **是** | Soil Characteristic• Insert the data as an object |
| `HEIGHT` | 数字 | **是** | Soil layer thickness |
| `ANGLE_OR_N` | 数字 | **是** | Internal friction angle of soil or N Value |
| `DENSITY` | 数字 | **是** | Unit volume weight of soil |
| `VS` | 数字 | **是** | Shear Wave Velocity |
| `KH` | 数字 | **是** | Coeff.of Horizontal Ground Reaction |
| `DISP` | 数字 | **是** | Relative Displacement |
| `DESC` | 文字（字符串） | 否 | Description |
| `OPT_USE_N` | 数字 | 否 | Use N Value• True : Use N Value of soil• False : Internal friction angle of soil |

**最简 JSON**：
```json
{
  "Argument": {
    "NAME": "<NAME>",
    "GROUND_LEVEL": 0,
    "BEDROCK_LEVEL": 0,
    "FOOTING_LEVEL": 0,
    "ITEMS": {},
    "properties": {
      "ITEMS": {
        "items": {
          "properties": {
            "HEIGHT": 0,
            "ANGLE_OR_N": 0,
            "DENSITY": 0,
            "VS": 0,
            "KH": 0,
            "DISP": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "NAME": "Soil-1",
      "DESC": "",
      "OPT_USE_N": false,
      "GROUND_LEVEL": 6,
      "BEDROCK_LEVEL": -21,
      "FOOTING_LEVEL": -17.5,
      "ITEMS": [
        {
          "HEIGHT": 7,
          "ANGLE_OR_N": 30,
          "DENSITY": 17,
          "VS": 160,
          "KH": 11449,
          "DISP": 0.001
        },
        {
          "HEIGHT": 1,
          "ANGLE_OR_N": 30,
          "DENSITY": 17,
          "VS": 160,
          "KH": 11449,
          "DISP": 0.001
        },
        {
          "HEIGHT": 1,
          "ANGLE_OR_N": 30,
          "DENSITY": 17,
          "VS": 160,
          "KH": 11449,
          "DISP": 0.001
        },
        {
          "HEIGHT": 1,
          "ANGLE_OR_N": 30,
          "DENSITY": 17,
          "VS": 160,
          "KH": 15913,
          "DISP": 0.001
        },
        {
          "HEIGHT": 1,
          "ANGLE_OR_N": 30,
          "DENSITY": 17,
          "VS": 160,
          "KH": 15913,
          "DISP": 0.001
        },
        {
          "HEIGHT": 1,
          "ANGLE_OR_N": 30,
          "DENSITY": 17,
          "VS": 160,
          "KH": 15913,
          "DISP": 0.001
        },
        {
          "HEIGHT": 1,
          "ANGLE_OR_N": 30,
          "DENSITY": 17,
          "VS": 160,
          "KH": 15913,
          "DISP": 0.001
        },
        {
          "HEIGHT": 1,
          "ANGLE_OR_N": 30,
          "DENSITY": 17,
          "VS": 187,
          "KH": 20511,
          "DISP": 0.001
        },
        {
          "HEIGHT": 1,
          "ANGLE_OR_N": 30,
          "DENSITY": 18,
          "VS": 193,
          "KH": 21533,
          "DISP": 0.001
        },
        {
          "HEIGHT": 1,
          "ANGLE_OR_N": 30,
          "DENSITY": 18,
          "VS": 210,
          "KH": 25565,
          "DISP": 0.001
        },
        {
          "HEIGHT": 1,
          "ANGLE_OR_N": 30,
          "DENSITY": 18,
          "VS": 215,
          "KH": 26986,
          "DISP": 0.001
        },
        {
          "HEIGHT": 1,
          "ANGLE_OR_N": 30,
          "DENSITY": 18,
          "VS": 221,
          "KH": 28690,
          "DISP": 0.001
        },
        {
          "HEIGHT": 1,
          "ANGLE_OR_N": 30,
          "DENSITY": 18,
          "VS": 224,
          "KH": 45496,
          "DISP": 0.001
        },
        {
          "HEIGHT": 1,
          "ANGLE_OR_N": 30,
          "DENSITY": 18,
          "VS": 228,
          "KH": 47246,
          "DISP": 0.001
        },
        {
          "HEIGHT": 1,
          "ANGLE_OR_N": 30,
          "DENSITY": 18,
          "VS": 215,
          "KH": 41559,
          "DISP": 0.001
        },
        {
          "HEIGHT": 1,
          "ANGLE_OR_N": 30,
          "DENSITY": 18,
          "VS": 181,
          "KH": 30014,
          "DISP": 0.001
        },
        {
          "HEIGHT": 1,
          "ANGLE_OR_N": 30,
          "DENSITY": 18,
          "VS": 171,
          "KH": 27391,
          "DISP": 0.001
        },
        {
          "HEIGHT": 1,
          "ANGLE_OR_N": 30,
          "DENSITY": 18,
          "VS": 167,
          "KH": 26342,
          "DISP": 0.001
        },
        {
          "HEIGHT": 1,
          "ANGLE_OR_N": 30,
          "DENSITY": 18,
          "VS": 169,
          "KH": 26867,
          "DISP": 0.001
        },
        {
          "HEIGHT": 1,
          "ANGLE_OR_N": 30,
          "DENSITY": 18,
          "VS": 479,
          "KH": 213426,
          "DISP": 0.001
        },
        {
          "HEIGHT": 1,
          "ANGLE_OR_N": 30,
          "DENSITY": 24,
          "VS": 736,
          "KH": 476345,
          "DISP": 0.001
        }
      ]
    }
  }
}
```


---

### Static Earth Pressure — `/db/EPST`

**方法**: POST, GET, PUT, DELETE | **参数**: 9 必填 + 10 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `LOADCASE` | 文字（字符串） | **是** | Prameters of Soil Properties Name |
| `ANGLE` | 数字 | **是** | Static Earth Pressure Angle |
| `SF` | 数字 | **是** | Scale Factor |
| `SURCHARGE_LOAD` | 数字 | **是** | Surcharge Load |
| `WATER_LEVEL` | 数字 | **是** | Water Level |
| `SOIL_PROP` | 文字（字符串） | **是** | Parameters of Soil Properties |
| `SEL_TYPE` | 文字（字符串） | **是** | Selection Type• GRUP: Use Area Group from Loading Area Plane• ELEMENT: Use selec |
| `ELEM_TYPE` | 文字（字符串） | **是** | Element Type• FRAME: Apply loads to frame nodes• PLANAR: Apply loads to planar e |
| `EP_TYPE":` | 数字 | **是** | Static Earth Pressure Type• At_Rest• Active |
| `DIR` | Stringr | 否 | Load Direction• XY: Apply load in horizontal direction• NORMAL: Apply load norma |
| `IN_PT` | 数字数组 | 否 | Inner Point |
| `EP_TYPE` | 文字（字符串） | 否 |  Static Earth Pressure Type |
| `NODE_LIST` | 整数数组 | 否 | Node List |
| `ELEM_LIST` | 整数数组 | 否 | Element List |
| `LOADING_AREA_GROUP` | 整数 | 否 | Loading Area Group Name |
| `PRES_PROFILE_ITEMS` | Array(Object) | 否 | Pressure Profile Items |
| `Level of each pressure profile point` | "LEVEL" | 否 | (1) |
| `Soil pressure at each level` | "SOIL_PRES" | 否 | (2) |
| `Additional pressure at each level` | "ADD_PRES" | 否 | (3) |

**最简 JSON**：
```json
{
  "Argument": {
    "LOADCASE": "<LOADCASE>",
    "ANGLE": 0,
    "SF": 0,
    "SURCHARGE_LOAD": 0,
    "WATER_LEVEL": 0,
    "SOIL_PROP": "<SOIL_PROP>",
    "SEL_TYPE": "<SEL_TYPE>",
    "ELEM_TYPE": "<ELEM_TYPE>"
  },
  "EP_TYPE\":": 0
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "LOADCASE": "HsX(+)",
      "DIR": "XY",
      "ANGLE": 0,
      "IN_PT": [
        5000,
        0,
        0
      ],
      "SF": 1,
      "EP_TYPE": "AT_REST",
      "SURCHARGE_LOAD": 16,
      "WATER_LEVEL": -4.7,
      "SOIL_PROP": "Soil-1",
      "SEL_TYPE": "GRUP",
      "ELEM_TYPE": "FRAME",
      "LOADING_AREA_GROUP": 1,
      "PRES_PROFILE_ITEMS": [
        {
          "LEVEL": 6,
          "SOIL_PRES": 8,
          "ADD_PRES": 0
        },
        {
          "LEVEL": -1,
          "SOIL_PRES": 67.5,
          "ADD_PRES": 0
        },
        {
          "LEVEL": -2,
          "SOIL_PRES": 76.00000000000001,
          "ADD_PRES": 0
        },
        {
          "LEVEL": -3,
          "SOIL_PRES": 84.50000000000001,
          "ADD_PRES": 0
        },
        {
          "LEVEL": -4,
          "SOIL_PRES": 93.00000000000003,
          "ADD_PRES": 0
        },
        {
          "LEVEL": -4.700000000000001,
          "SOIL_PRES": 98.95000000000003,
          "ADD_PRES": 0
        },
        {
          "LEVEL": -5,
          "SOIL_PRES": 102.97099750000002,
          "ADD_PRES": 0
        },
        {
          "LEVEL": -6,
          "SOIL_PRES": 116.37432250000005,
          "ADD_PRES": 0
        },
        {
          "LEVEL": -7,
          "SOIL_PRES": 129.77764750000003,
          "ADD_PRES": 0
        },
        {
          "LEVEL": -8,
          "SOIL_PRES": 143.18097250000005,
          "ADD_PRES": 0
        },
        {
          "LEVEL": -9,
          "SOIL_PRES": 157.08429750000005,
          "ADD_PRES": 0
        },
        {
          "LEVEL": -10,
          "SOIL_PRES": 170.98762250000007,
          "ADD_PRES": 0
        },
        {
          "LEVEL": -11,
          "SOIL_PRES": 184.89094750000007,
          "ADD_PRES": 0
        },
        {
          "LEVEL": -12,
          "SOIL_PRES": 198.7942725000001,
          "ADD_PRES": 0
        },
        {
          "LEVEL": -13,
          "SOIL_PRES": 212.6975975000001,
          "ADD_PRES": 0
        },
        {
          "LEVEL": -14,
          "SOIL_PRES": 226.6009225000001,
          "ADD_PRES": 0
        },
        {
          "LEVEL": -15,
          "SOIL_PRES": 240.5042475000001,
          "ADD_PRES": 0
        },
        {
          "LEVEL": -16,
          "SOIL_PRES": 254.40757250000013,
          "ADD_PRES": 0
        },
        {
          "LEVEL": -17,
          "SOIL_PRES": 268.31089750000007,
          "ADD_PRES": 0
        },
        {
          "LEVEL": -18,
          "SOIL_PRES": 282.2142225000001,
          "ADD_PRES": 0
        },
        {
          "LEVEL": -19,
          "SOIL_PRES": 296.11754750000006,
          "ADD_PRES": 0
        },
        {
          "LEVEL": -20,
          "SOIL_PRES": 310.0208725000001,
          "ADD_PRES": 0
        },
        {
          "LEVEL": -21,
          "SOIL_PRES": 326.92419750000005,
          "ADD_PRES": 0
        }
      ]
    }
  }
}
```


---

### Parameter of Seismic Loads — `/db/POSL`

**方法**: POST, GET, PUT, DELETE | **参数**: 5 必填 + 9 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Parameters of Seismic Earth Name |
| `SZ` | 文字（字符串） | **是** | Seismic Zone |
| `EPA` | 数字 | **是** | Effective Peak Ground Acceleration |
| `SC` | 文字（字符串） | **是** | Site Class |
| `FA` | 数字 | **是** | Short-period site coefficient |
| `CODE` | 文字（字符串） | 否 | Seismic Load Code |
| `METHOD` | 文字（字符串） | 否 | Seismic Calculation Method• RES_DISP: Response Displacement Method• EQV_STATIC:  |
| `FV` | 数字 | 否 | Soil layer thickness |
| `SDS` | 数字 | 否 | Design spectral acceleration at short period |
| `SD1` | 数字 | 否 | Design spectral acceleration at 1-second period |
| `USER_GROUP` | 文字（字符串） | 否 | Seismic User Group |
| `IF` | 数字 | 否 | Importance Factor |
| `RMF` | 数字 | 否 | Response Modification Factor |
| `CALC_OPT` | 是/否（布尔值） | 否 | CalculateData |

**最简 JSON**：
```json
{
  "Argument": {
    "NAME": "<NAME>",
    "SZ": "<SZ>",
    "EPA": 0,
    "SC": "<SC>",
    "FA": 0
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "NAME": "KDS(2019)",
      "CODE": "KDS(41-17-00:2019)",
      "METHOD": "RES_DISP",
      "SZ": "1",
      "EPA": 0.22,
      "SC": "S1",
      "FA": 1.12,
      "FV": 0.84,
      "SDS": 0.41066666666666674,
      "SD1": 0.12319999999999999,
      "USER_GROUP": "1",
      "IF": 1.2,
      "RMF": 3
    }
  }
}
```


---

### Element Temperature — `/db/ETMP`

**方法**: POST, GET, PUT, DELETE | **参数**: 3 必填 + 2 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `ITEMS` | Array[Object] | **是** | Element Temperature• Insert the data as an object |
| `LCNAME` | 文字（字符串） | **是** | Load Case Name |
| `TEMP` | 数字 | **是** | Temperature |
| `ID` | 整数 | 否 | Serial Number |
| `GROUP_NAME` | 文字（字符串） | 否 | Load Group Name |

**最简 JSON**：
```json
{
  "ETMP": {
    "ITEMS": [],
    "properties": {
      "ITEMS": {
        "items": {
          "properties": {
            "LCNAME": "<LCNAME>",
            "TEMP": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "ITEMS": [
        {
          "ID": 1,
          "LCNAME": "Temp(+)",
          "GROUP_NAME": "",
          "TEMP": 35
        },
        {
          "ID": 2,
          "LCNAME": "Temp(-)",
          "GROUP_NAME": "",
          "TEMP": -20
        }
      ]
    }
  }
}
```


---

### Temperature Gradient — `/db/GTMP`

**方法**: POST, GET, PUT, DELETE | **参数**: 5 必填 + 6 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `ITEMS` | Array[Object] | **是** | Temperature Gradient• Insert the data as an object |
| `LCNAME` | 文字（字符串） | **是** | Load Case Name |
| `TYPE` | 整数 | **是** | Element Type• Beam: 1• Plate: 2 |
| `TZ` | 数字 | **是** | T2z - T1z |
| `TY` | 数字 | **是** | T2y-T1y |
| `ID` | 整数 | 否 | Serial Number |
| `GROUP_NAME` | 文字（字符串） | 否 | Load Group Name |
| `USE_HZ` | 是/否（布尔值） | 否 | Use Section Hz |
| `HZ` | 数字 | 否 | Hz value |
| `USE_HY` | 是/否（布尔值） | 否 | Use Section Hy |
| `HY` | 数字 | 否 | Hy value |

**最简 JSON**：
```json
{
  "GTMP": {
    "ITEMS": [],
    "properties": {
      "ITEMS": {
        "items": {
          "properties": {
            "LCNAME": "<LCNAME>",
            "TYPE": 0,
            "TZ": 0,
            "TY": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "2": {
      "ITEMS": [
        {
          "ID": 1,
          "LCNAME": "Temp(+)",
          "GROUP_NAME": "",
          "TYPE": 1,
          "TZ": 10,
          "USE_HZ": true,
          "TY": -10,
          "USE_HY": true
        },
        {
          "ID": 2,
          "LCNAME": "Temp(-)",
          "GROUP_NAME": "",
          "TYPE": 1,
          "TZ": 10,
          "USE_HZ": false,
          "HZ": 1.2,
          "TY": -10,
          "USE_HY": false,
          "HY": 0.5
        }
      ]
    }
  }
}
```


---

### Beam Section Temperature — `/db/BTMP`

**方法**: POST, GET, PUT, DELETE | **参数**: 3 必填 + 5 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `ITEMS` | Array[Object] | **是** | Section Temperature List• Insert the data as an object |
| `LCNAME` | 文字（字符串） | **是** | Load Case Name |
| `NUM` | 整数 | **是** | Number of Section Temperature ("vSECTTMP") |
| `ID` | 整数 | 否 | Serial Number |
| `GROUP_NAME` | 文字（字符串） | 否 | Load Group Name |
| `DIR` | 文字（字符串） | 否 | Direction• Local-y: "LY"• Local-z: "LZ" |
| `REF` | 文字（字符串） | 否 | Ref. Position• Centroid: "Centroid"• +End(Top): "Top"• - End(Bot): "Bot" |
| `bPSC` | 是/否（布尔值） | 否 | Section Type• General: false• PSC / Composite: true |

**最简 JSON**：
```json
{
  "BTMP": {
    "ITEMS": [],
    "properties": {
      "ITEMS": {
        "items": {
          "properties": {
            "LCNAME": "<LCNAME>",
            "NUM": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "51": {
      "ITEMS": [
        {
          "ID": 1,
          "LCNAME": "Temp(+)",
          "GROUP_NAME": "",
          "DIR": "LZ",
          "REF": "Centroid",
          "NUM": 1,
          "bPSC": false,
          "vSECTTMP": [
            {
              "TYPE": "ELEMENT",
              "VAL_B": 0.2,
              "VAL_H1": 0.1,
              "VAL_H2": 0.2,
              "VAL_T1": 3,
              "VAL_T2": 12.4
            }
          ]
        }
      ]
    }
  }
}
```


---

### System Temperature — `/db/STMP`

**方法**: POST, GET, PUT, DELETE | **参数**: 1 必填 + 2 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `LCNAME` | 文字（字符串） | **是** | Load Case Name |
| `TEMPER` | 数字 | 否 | System Temperature |
| `GROUP_NAME` | 文字（字符串） | 否 | Load Group Name |

**最简 JSON**：
```json
{
  "STMP": {
    "LCNAME": "<LCNAME>"
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "TEMPER": 12.5,
      "LCNAME": "Temp(+)",
      "GROUP_NAME": "LoadGroup1"
    },
    "2": {
      "TEMPER": -32.3,
      "LCNAME": "Temp(-)",
      "GROUP_NAME": "LoadGroup2"
    }
  }
}
```


---

### Nodal Temperature — `/db/NTMP`

**方法**: POST, GET, PUT, DELETE | **参数**: 3 必填 + 2 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `ITEMS` | Array[Object] | **是** | Nodal Temperature• Insert the data as an object |
| `LCNAME` | 文字（字符串） | **是** | Load Case Name |
| `TEMPER` | 数字 | **是** | Temperature |
| `ID` | 整数 | 否 | Serial Number |
| `GROUP_NAME` | 文字（字符串） | 否 | Load Group Name |

**最简 JSON**：
```json
{
  "NTMP": {
    "ITEMS": [],
    "properties": {
      "ITEMS": {
        "items": {
          "properties": {
            "LCNAME": "<LCNAME>",
            "TEMPER": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "190": {
      "ITEMS": [
        {
          "ID": 1,
          "LCNAME": "Temp(-)",
          "GROUP_NAME": "LoadGroup2",
          "TEMPER": -3
        },
        {
          "ID": 3,
          "LCNAME": "Temp(+)",
          "GROUP_NAME": "LoadGroup1",
          "TEMPER": 2
        }
      ]
    },
    "234": {
      "ITEMS": [
        {
          "ID": 1,
          "LCNAME": "Temp(-)",
          "GROUP_NAME": "LoadGroup2",
          "TEMPER": -5
        },
        {
          "ID": 3,
          "LCNAME": "Temp(+)",
          "GROUP_NAME": "LoadGroup1",
          "TEMPER": 3
        }
      ]
    }
  }
}
```


---

### Tendon Property — `/db/TDNT`

**方法**: POST, GET, PUT, DELETE | **参数**: 9 必填 + 16 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Tendon Name |
| `MATL` | 整数 | **是** | Tendon Material No. |
| `AREA` | 数字 | **是** | Total Tendon Area |
| `D_AREA` | 数字 | **是** | Dimeter• Post-Tension: Duct diameter• Pre-Tension: Strand diameter• External: No |
| `RM` | 整数 | **是** | Relaxation Coefficient - Code¹⁾ |
| `RV` | 整数 | **是** | Relaxation Coefficient - Factor¹⁾ |
| `FT` | 数字 | **是** | Relaxation coefficient - Factor (ξ)¹⁾ |
| `FPK` | 数字 | **是** | Characteristic Value of Strength (fpk) |
| `TDMFNAME` | 文字（字符串） | **是** | Relaxation Function Name |
| `TYPE` | 文字（字符串） | 否 | Tendon Type• Internal: "INTERAL"• External: "EXTERNAL" |
| `US` | 数字 | 否 | Ultimate strength |
| `YS` | 数字 | 否 | Yield strength |
| `LT` | 文字（字符串） | 否 | Tensioning Type• Post-Tension: "POST"• Pre-Tension: "PRE"• External: Not use |
| `ASB` | 数字 | 否 | Anchorage Slip - Begin• Post-Tension/External: Use• Pre-Tension: Not use |
| `ASE` | 数字 | 否 | Anchorage Slip - End• Post-Tension/External: Use• Pre-Tension: Not use |
| `bBONDED` | 是/否（布尔值） | 否 | Bond Type• Post-Tension: Use• Pre-Tension/External: Not use |
| `ALPHA` | 数字 | 否 | External Cable Moment Magnifier• External: Use• Pre/Post-Tension: Not use |
| `bOSRF` | 是/否（布尔值） | 否 | Application of Overstress Reduction Factor |
| `LR` | 是/否（布尔值） | 否 | Low Relaxation |
| ... | ... | ... | *还有 6 个可选参数* |

**最简 JSON**：
```json
{
  "TDNT": {
    "NAME": "<NAME>",
    "MATL": 0,
    "AREA": 0,
    "D_AREA": 0,
    "RM": 0,
    "RV": 0,
    "FT": 0,
    "FPK": 0,
    "TDMFNAME": "<TDMFNAME>"
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "NAME": "In_Pre_Magura",
      "TYPE": "INTERNAL",
      "MATL": 1,
      "AREA": 0.00504,
      "D_AREA": 0.0152,
      "RM": 0,
      "RV": 45,
      "US": 1860000,
      "YS": 1570000,
      "LT": "PRE"
    },
    "2": {
      "NAME": "In_Post_Magura",
      "TYPE": "INTERNAL",
      "MATL": 1,
      "AREA": 0.00504,
      "D_AREA": 0.1,
      "RM": 0,
      "RV": 45,
      "US": 1860000,
      "YS": 1570000,
      "LT": "POST",
      "ASB": 0.006,
      "ASE": 0.006,
      "bBONDED": true,
      "FF": 0.3,
      "WF": 0.0066
    },
    "3": {
      "NAME": "Ext_Magura",
      "TYPE": "EXTERNAL",
      "MATL": 1,
      "AREA": 0.00504,
      "RM": 0,
      "RV": 10,
      "US": 1860000,
      "YS": 1570000,
      "ASB": 0.006,
      "ASE": 0.006,
      "ALPHA": 3000,
      "FF": 0.3
    }
  }
}
```


---

### Tendon Profile — `/db/TDNA`

**方法**: POST, GET, PUT, DELETE | **参数**: 13 必填 + 29 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Tendon Name |
| `TDN_PROP` | 整数 | **是** | Tendon Property No. |
| `ELEM` | 整数数组 | **是** | Assigned Elements No. |
| `CURVE` | 文字（字符串） | **是** | Curve Type• Spline: "SPLINE"• Round: "ROUND" |
| `INPUT` | 文字（字符串） | **是** | Input Type• 2D: "2D"• 3D: "3D" |
| `LENG_OPT` | 文字（字符串） | **是** | Transfer Length Option• User defined Length: "USER"• Auto Calculation: "AUTO1"•  |
| `SHAPE` | 文字（字符串） | **是** | Reference Axis• Element Type: "ELEMENT"• Straight Type: "STRAIGHT"• Curve Type:  |
| `INS_PT` | 文字（字符串） | **是** | Profile Insertion Point Type• End-I: "END-I"• End-J: "END-J" |
| `INS_ELEM` | 整数 | **是** | Profile Insertion Point Element No. |
| `PROF` | Array[Object] | **是** | 3D Profile• Insert the data as an object |
| `PROFY` | Array[Object] | **是** | Profile in x-y plane• Insert the data as an object |
| `PROFZ` | Array[Object] | **是** | Profile in x-z plane• Insert the data as an object |
| `PT` | Array[Number, 3] | **是** | Coordinates• [x, y, z] |
| `BELENG` | 数字 | 否 | Straight Length of Tendon - Begin• Only for Spline Type |
| `ELENG` | 数字 | 否 | Straight Length of Tendon - End• Only for Spline Type |
| `TDN_GRUP` | 整数 | 否 | Tendon Group No. |
| `BLEN` | 数字 | 否 | Transfer Length - Begin |
| `ELEN` | 数字 | 否 | Transfer Length - End |
| `bTP` | 是/否（布尔值） | 否 | Typical Tendon |
| `CNT` | 数字 | 否 | No. of Tendons• Required if "bTP" = true |
| `DeBondBLEN` | 数字 | 否 | Debonded Length - Begin• Only for Pre-tensioning |
| `DeBondELEN` | 数字 | 否 | Debonded Length - End• Only for Pre-tensioning |
| `IP` | Array[Number, 3] | 否 | Profile Insertion Point• [x, y, z] |
| ... | ... | ... | *还有 19 个可选参数* |

**最简 JSON**：
```json
{
  "TDNA": {
    "NAME": "<NAME>",
    "TDN_PROP": 0,
    "ELEM": 0,
    "CURVE": "<CURVE>",
    "INPUT": "<INPUT>",
    "LENG_OPT": "<LENG_OPT>",
    "SHAPE": "<SHAPE>",
    "INS_PT": "<INS_PT>",
    "INS_ELEM": 0,
    "PROF": [],
    "PROFY": [],
    "PROFZ": [],
    "properties": {
      "PROF": {
        "items": {
          "properties": {
            "PT": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "NAME": "2D/Spline/Element",
      "TDN_PROP": 1,
      "ELEM": [
        1101,
        1102,
        1103,
        1104,
        1105,
        1106,
        1107,
        1108,
        1109,
        1110,
        1111,
        1112,
        1113,
        1114,
        1115,
        1116,
        1117,
        1118,
        1119,
        1120,
        1121,
        1122,
        1123,
        1124,
        1125,
        1126,
        1127,
        1128,
        1129,
        1130
      ],
      "BELENG": 0.3,
      "ELENG": 0.3,
      "CURVE": "SPLINE",
      "INPUT": "2D",
      "TDN_GRUP": 1,
      "LENG_OPT": "USER",
      "bTP": true,
      "CNT": 1,
      "DeBondBLEN": 0,
      "DeBondELEN": 0,
      "SHAPE": "ELEMENT",
      "INS_PT": "END-I",
      "INS_ELEM": 1101,
      "AXIS_IJ": "I-J",
      "XAR_ANGLE": 0,
      "bPJ": true,
      "OFF_YZ": [
        0,
        0
      ],
      "PROFY": [
        {
          "PT": [
            0,
            -0.5
          ],
          "bFIX": true,
          "R": 1.2
        },
        {
          "PT": [
            30,
            -0.5
          ],
          "bFIX": true,
          "R": 1.2
        }
      ],
      "PROFZ": [
        {
          "PT": [
            0,
            -0.6
          ],
          "bFIX": true,
          "R": 1.3,
          "bBOTZ": false
        },
        {
          "PT": [
            30,
            -0.6
          ],
          "bFIX": true,
          "R": 1.3,
          "bBOTZ": false
        }
      ]
    }
  }
}
```


---

### Tendon Location for Composite Section — `/db/TDCS`

**方法**: POST, GET, PUT, DELETE | **参数**: 3 必填 + 0 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TDNA` | 整数 | **是** | Tendon Profile |
| `CSCS` | 整数 | **是** | Composite Section for Concstruction Stage |
| `PART_NUM` | 整数 | **是** | Part Number |

**最简 JSON**：
```json
{
  "TDCS": {
    "TDNA": 0,
    "CSCS": 0,
    "PART_NUM": 0
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "TDNA": 1,
      "CSCS": 1,
      "PART_NUM": 1
    }
  }
}
```


---

### Tendon Prestress — `/db/TDPL`

**方法**: POST, GET, PUT, DELETE | **参数**: 5 必填 + 5 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `ITEMS` | Array[Object] | **是** | Tendon Prestress• Insert the data as an object |
| `LCNAME` | 文字（字符串） | **是** | Load Case Name |
| `TENDON_NAME` | 文字（字符串） | **是** | Tendon Profile Name |
| `BEGIN` | 数字 | **是** | Jaking Force at Begin |
| `END` | 数字 | **是** | Jaking Force at End |
| `ID` | 整数 | 否 | Serial Number |
| `GROUP_NAME` | 文字（字符串） | 否 | Load Group Name |
| `TYPE` | 文字（字符串） | 否 | Prestress Load Type• Stress: "STRESS"• Force: "FORCE" |
| `ORDER` | 文字（字符串） | 否 | Jacking Step• Begin: "BEGIN"• End: "END"• Both: "BOTH" |
| `GROUTING` | 整数 | 否 | Grouting Stage |

**最简 JSON**：
```json
{
  "TDPL": {
    "ITEMS": [],
    "properties": {
      "ITEMS": {
        "items": {
          "properties": {
            "LCNAME": "<LCNAME>",
            "TENDON_NAME": "<TENDON_NAME>",
            "BEGIN": 0,
            "END": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "2": {
      "ITEMS": [
        {
          "ID": 1,
          "LCNAME": "PS",
          "GROUP_NAME": "LoadGroup",
          "TENDON_NAME": "2D/Round/Element",
          "TYPE": "FORCE",
          "ORDER": "BOTH",
          "BEGIN": 1360000,
          "END": 1360000,
          "GROUTING": 1
        }
      ]
    },
    "6": {
      "ITEMS": [
        {
          "ID": 1,
          "LCNAME": "PS",
          "GROUP_NAME": "LoadGroup",
          "TENDON_NAME": "2D/Round/Curve",
          "TYPE": "STRESS",
          "ORDER": "BOTH",
          "BEGIN": 1360000,
          "END": 1360000,
          "GROUTING": 1
        }
      ]
    }
  }
}
```


---

### Prestress Beam Loads — `/db/PRST`

**方法**: POST, GET, PUT, DELETE | **参数**: 3 必填 + 6 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `ITEMS` | Array[Object] | **是** | Prestress Beam Loads• Insert the data as an object |
| `LCNAME` | 文字（字符串） | **是** | Load Case Name |
| `TENSION` | 数字 | **是** | Tension |
| `ID` | 整数 | 否 | Serial Number |
| `GROUP_NAME` | 文字（字符串） | 否 | Load Group Name |
| `DIR` | 整数 | 否 | Direction• Local y: 0• Local z: 1 |
| `DISTANCE_I` | 数字 | 否 | Distance - I (Di) |
| `DISTANCE_M` | 数字 | 否 | Distance - M (Dm) |
| `DISTANCE_J` | 数字 | 否 | Distance - J (Dj) |

**最简 JSON**：
```json
{
  "PRST": {
    "ITEMS": [],
    "properties": {
      "ITEMS": {
        "items": {
          "properties": {
            "LCNAME": "<LCNAME>",
            "TENSION": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1101": {
      "ITEMS": [
        {
          "ID": 1,
          "LCNAME": "PS",
          "GROUP_NAME": "LoadGroup",
          "DIR": 1,
          "TENSION": 1360,
          "DISTANCE_I": 0.2,
          "DISTANCE_M": 0.3,
          "DISTANCE_J": 0.4
        }
      ]
    },
    "1102": {
      "ITEMS": [
        {
          "ID": 1,
          "LCNAME": "PS",
          "GROUP_NAME": "LoadGroup",
          "DIR": 1,
          "TENSION": 1360,
          "DISTANCE_I": 0.2,
          "DISTANCE_M": 0.3,
          "DISTANCE_J": 0.4
        }
      ]
    },
    "1103": {
      "ITEMS": [
        {
          "ID": 1,
          "LCNAME": "PS",
          "GROUP_NAME": "LoadGroup",
          "DIR": 1,
          "TENSION": 1360,
          "DISTANCE_I": 0.2,
          "DISTANCE_M": 0.3,
          "DISTANCE_J": 0.4
        }
      ]
    }
  }
}
```


---

### Pretension Loads — `/db/PTNS`

**方法**: POST, GET, PUT, DELETE | **参数**: 3 必填 + 2 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `ITEMS` | Array[Object] | **是** | Pretension Loads• Insert the data as an object |
| `LCNAME` | 文字（字符串） | **是** | Load Case Name |
| `TENSION` | 数字 | **是** | Pretension Load |
| `ID` | 整数 | 否 | Serial Number |
| `GROUP_NAME` | 文字（字符串） | 否 | Load Group Name |

**最简 JSON**：
```json
{
  "PTNS": {
    "ITEMS": [],
    "properties": {
      "ITEMS": {
        "items": {
          "properties": {
            "LCNAME": "<LCNAME>",
            "TENSION": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "3431": {
      "ITEMS": [
        {
          "ID": 1,
          "LCNAME": "PrS1",
          "GROUP_NAME": "LoadGroup",
          "TENSION": 130
        }
      ]
    },
    "3432": {
      "ITEMS": [
        {
          "ID": 1,
          "LCNAME": "PrS1",
          "GROUP_NAME": "LoadGroup",
          "TENSION": 130
        }
      ]
    },
    "3433": {
      "ITEMS": [
        {
          "ID": 1,
          "LCNAME": "PrS2",
          "GROUP_NAME": "LoadGroup",
          "TENSION": 130
        }
      ]
    }
  }
}
```


---

### External Type Load Case for Pretension — `/db/EXLD`

**方法**: POST, GET, PUT, DELETE | **参数**: 1 必填 + 0 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `LCNAME_ITEM` | 字符串数组 | **是** | Load Case Name• Only load cases with pre-tension load |

**最简 JSON**：
```json
{
  "EXLD": {
    "LCNAME_ITEM": "<LCNAME_ITEM>"
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "LCNAME_ITEM": [
        "PrS1",
        "PrS2"
      ]
    }
  }
}
```


---

### Moving Load Code — `/db/MVCD`

**方法**: POST, GET, PUT, DELETE | **参数**: 1 必填 + 0 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `CODE` | 文字（字符串） | **是** | Moving Load Code¹⁾ |

**最简 JSON**：
```json
{
  "MVCD": {
    "CODE": "<CODE>"
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "CODE": "EUROCODE"
    }
  }
}
```


---

### Traffic Line Lanes — `/db/LLAN`

**方法**: POST, GET, PUT, DELETE | **参数**: 7 必填 + 12 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `COMMON` | 对象（一组键值对） | **是** | Common Items |
| `LL_NAME` | 文字（字符串） | **是** | Name of Line Lane |
| `LOAD_DIST` | 文字（字符串） | **是** | Load Distribution• Lane Element: "LANE"• Cross Beam: "CROSS" |
| `MOVING` | 文字（字符串） | **是** | Moving Direction• Forward: "FORWARD"• Backward: "BACKWARD"• Both: "BOTH" |
| `WIDTH` | 数字 | **是** | Lane Width¹⁾ |
| `LANE_ITEMS` | Array[Object] | **是** | Lane Items• Insert the data as an object |
| `ELEM` | 整数 | **是** | Element No. |
| `GROUP_NAME` | 文字（字符串） | 否 | Name of Structure Group³⁾ |
| `SKEW_START` | 数字 | 否 | Skew Start³⁾ |
| `SKEW_END` | 数字 | 否 | Skew End³⁾ |
| `WHEEL_SPACE` | 数字 | 否 | Wheel Spacing |
| `OPT_AUTO_LANE` | 是/否（布尔值） | 否 | Transverse Lane Optimization²⁾ |
| `ALLOW_WIDTH` | 数字 | 否 | Allow Width for Optimization²⁾ |
| `SPECIAL_LANE_ITEMS` | Array | 否 | Usedonlywhenimporting |
| `ECC` | 数字 | 否 | Eccentricity |
| `FACT` | 数字 | 否 | Impact Factor |
| `SPAN_START` | 是/否（布尔值） | 否 | Span Start |
| ... | ... | ... | *还有 2 个可选参数* |

**最简 JSON**：
```json
{
  "LLAN": {
    "COMMON": {
      "LL_NAME": "<LL_NAME>",
      "LOAD_DIST": "<LOAD_DIST>",
      "MOVING": "<MOVING>",
      "WIDTH": 0
    },
    "LANE_ITEMS": [],
    "properties": {
      "LANE_ITEMS": {
        "items": {
          "properties": {
            "ELEM": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "COMMON": {
        "LL_NAME": "LL_01",
        "LOAD_DIST": "LANE",
        "GROUP_NAME": "",
        "SKEW_START": 0,
        "SKEW_END": 0,
        "MOVING": "FORWARD",
        "WHEEL_SPACE": 1.8,
        "WIDTH": 3,
        "OPT_AUTO_LANE": true,
        "ALLOW_WIDTH": 3
      },
      "LANE_ITEMS": [
        {
          "ELEM": 1,
          "ECC": -1.5
        },
        {
          "ELEM": 2,
          "ECC": -1.5
        },
        {
          "ELEM": 3,
          "ECC": -1.5
        }
      ]
    },
    "2": {
      "COMMON": {
        "LL_NAME": "LL_02",
        "LOAD_DIST": "CROSS",
        "GROUP_NAME": "CrossBeam",
        "SKEW_START": 10,
        "SKEW_END": 10,
        "MOVING": "BOTH",
        "WHEEL_SPACE": 1.8,
        "WIDTH": 3,
        "OPT_AUTO_LANE": true,
        "ALLOW_WIDTH": 3
      },
      "LANE_ITEMS": [
        {
          "ELEM": 163,
          "ECC": -1.5
        },
        {
          "ELEM": 164,
          "ECC": -1.5
        },
        {
          "ELEM": 165,
          "ECC": -1.55
        }
      ]
    }
  }
}
```


---

### Traffic Line Lanes - China — `/db/LLANch`

**方法**: POST, GET, PUT, DELETE | **参数**: 7 必填 + 11 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `COMMON` | 对象（一组键值对） | **是** | Common Items |
| `LL_NAME` | 文字（字符串） | **是** | Name of Line Lane |
| `LOAD_DIST` | 文字（字符串） | **是** | Load Distribution• Lane Element: "LANE"• Cross Beam: "CROSS" |
| `MOVING` | 文字（字符串） | **是** | Moving Direction• Forward: "FORWARD"• Backward: "BACKWARD"• Both: "BOTH" |
| `WIDTH` | 数字 | **是** | Lane Width• Unavailable Key |
| `LANE_ITEMS` | Array[Object] | **是** | Lane Items• Insert the data as an object |
| `ELEM` | 整数 | **是** | Element No. |
| `GROUP_NAME` | 文字（字符串） | 否 | Name of Structure Group |
| `SKEW_START` | 数字 | 否 | Skew Start |
| `SKEW_END` | 数字 | 否 | Skew End |
| `WHEEL_SPACE` | 数字 | 否 | Wheel Spacing |
| `OPT_AUTO_LANE` | 是/否（布尔值） | 否 | Transverse Lane Optimization |
| `ALLOW_WIDTH` | 数字 | 否 | Allow Width for Optimization |
| `SPECIAL_LANE_ITEMS` | Array | 否 | Usedonlywhenimporting |
| `ECC` | 数字 | 否 | Eccentricity |
| `SPAN` | 数字 | 否 | Span Length |
| `SPAN_START` | 是/否（布尔值） | 否 | Span Start |
| ... | ... | ... | *还有 1 个可选参数* |

**最简 JSON**：
```json
{
  "LLANCH": {
    "COMMON": {
      "LL_NAME": "<LL_NAME>",
      "LOAD_DIST": "<LOAD_DIST>",
      "MOVING": "<MOVING>",
      "WIDTH": 0
    },
    "LANE_ITEMS": [],
    "properties": {
      "LANE_ITEMS": {
        "items": {
          "properties": {
            "ELEM": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "COMMON": {
        "LL_NAME": "LL_01",
        "LOAD_DIST": "LANE",
        "GROUP_NAME": "",
        "SKEW_START": 0,
        "SKEW_END": 0,
        "MOVING": "BOTH",
        "WHEEL_SPACE": 1.8,
        "WIDTH": 3,
        "OPT_AUTO_LANE": true,
        "ALLOW_WIDTH": 3
      },
      "LANE_ITEMS": [
        {
          "ELEM": 1,
          "ECC": -1.5,
          "SPAN": 12,
          "SPAN_START": true,
          "SCALE_FACTOR": 1.1
        },
        {
          "ELEM": 2,
          "ECC": -1.5,
          "SPAN": 12,
          "SPAN_START": true,
          "SCALE_FACTOR": 1.1
        },
        {
          "ELEM": 3,
          "ECC": -1.5,
          "SPAN": 12,
          "SPAN_START": true,
          "SCALE_FACTOR": 1.1
        }
      ]
    },
    "2": {
      "COMMON": {
        "LL_NAME": "LL_02",
        "LOAD_DIST": "CROSS",
        "GROUP_NAME": "CrossBeam",
        "SKEW_START": 10,
        "SKEW_END": 15,
        "MOVING": "BACKWARD",
        "WHEEL_SPACE": 1.8,
        "WIDTH": 3,
        "OPT_AUTO_LANE": true,
        "ALLOW_WIDTH": 3
      },
      "LANE_ITEMS": [
        {
          "ELEM": 163,
          "ECC": -1.5,
          "SPAN": 12,
          "SPAN_START": true,
          "SCALE_FACTOR": 1.1
        },
        {
          "ELEM": 164,
          "ECC": -1.5,
          "SPAN": 12,
          "SPAN_START": false,
          "SCALE_FACTOR": 1.1
        },
        {
          "ELEM": 165,
          "ECC": -1.5,
          "SPAN": 12,
          "SPAN_START": false,
          "SCALE_FACTOR": 1.1
        }
      ]
    }
  }
}
```


---

### Traffic Line Lanes - India — `/db/LLANid`

**方法**: POST, GET, PUT, DELETE | **参数**: 7 必填 + 11 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `COMMON` | 对象（一组键值对） | **是** | Common Items |
| `LL_NAME` | 文字（字符串） | **是** | Name of Line Lane |
| `LOAD_DIST` | 文字（字符串） | **是** | Load Distribution• Lane Element: "LANE"• Cross Beam: "CROSS" |
| `MOVING` | 文字（字符串） | **是** | Moving Direction• Forward: "FORWARD"• Backward: "BACKWARD"• Both: "BOTH" |
| `WIDTH` | 数字 | **是** | Lane Width• Unavailable Key |
| `LANE_ITEMS` | Array[Object] | **是** | Lane Items• Insert the data as an object |
| `ELEM` | 整数 | **是** | Element No. |
| `GROUP_NAME` | 文字（字符串） | 否 | Name of Structure Group |
| `SKEW_START` | 数字 | 否 | Skew Start |
| `SKEW_END` | 数字 | 否 | Skew End |
| `WHEEL_SPACE` | 数字 | 否 | Wheel Spacing |
| `OPT_AUTO_LANE` | 是/否（布尔值） | 否 | Transverse Lane Optimization |
| `ALLOW_WIDTH` | 数字 | 否 | Allow Width for Optimization |
| `SPECIAL_LANE_ITEMS` | Array | 否 | Usedonlywhenimporting |
| `ECC` | 数字 | 否 | Eccentricity |
| `IMPACT_SPAN` | 整数 | 否 | Option• IF/CDA: 0• Span Length: 1 |
| `IMPACT_FACTOR` | 数字 | 否 | Scale Factor• When "IMPACT_SPAN": 0 |
| ... | ... | ... | *还有 1 个可选参数* |

**最简 JSON**：
```json
{
  "LLANID": {
    "COMMON": {
      "LL_NAME": "<LL_NAME>",
      "LOAD_DIST": "<LOAD_DIST>",
      "MOVING": "<MOVING>",
      "WIDTH": 0
    },
    "LANE_ITEMS": [],
    "properties": {
      "LANE_ITEMS": {
        "items": {
          "properties": {
            "ELEM": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "COMMON": {
        "LL_NAME": "LL_01",
        "LOAD_DIST": "LANE",
        "GROUP_NAME": "",
        "SKEW_START": 0,
        "SKEW_END": 0,
        "MOVING": "BOTH",
        "WHEEL_SPACE": 1.8,
        "WIDTH": 0,
        "OPT_AUTO_LANE": false,
        "ALLOW_WIDTH": 0
      },
      "LANE_ITEMS": [
        {
          "ELEM": 1,
          "ECC": -1.5,
          "SPAN": 12,
          "IMPACT_SPAN": 1,
          "IMPACT_FACTOR": 0
        },
        {
          "ELEM": 2,
          "ECC": -1.5,
          "SPAN": 12,
          "IMPACT_SPAN": 1,
          "IMPACT_FACTOR": 0
        },
        {
          "ELEM": 3,
          "ECC": -1.5,
          "SPAN": 12,
          "IMPACT_SPAN": 1,
          "IMPACT_FACTOR": 0
        }
      ]
    },
    "2": {
      "COMMON": {
        "LL_NAME": "LL_02",
        "LOAD_DIST": "CROSS",
        "GROUP_NAME": "CrossBeam",
        "SKEW_START": 10,
        "SKEW_END": 15,
        "MOVING": "BACKWARD",
        "WHEEL_SPACE": 1.8,
        "WIDTH": 0,
        "OPT_AUTO_LANE": false,
        "ALLOW_WIDTH": 0
      },
      "LANE_ITEMS": [
        {
          "ELEM": 163,
          "ECC": -1.5,
          "SPAN": 0,
          "IMPACT_SPAN": 0,
          "IMPACT_FACTOR": 1
        },
        {
          "ELEM": 164,
          "ECC": -1.5,
          "SPAN": 0,
          "IMPACT_SPAN": 0,
          "IMPACT_FACTOR": 1
        },
        {
          "ELEM": 165,
          "ECC": -1.5,
          "SPAN": 0,
          "IMPACT_SPAN": 0,
          "IMPACT_FACTOR": 1
        }
      ]
    }
  }
}
```


---

### Traffic Line Lanes - Transverse — `/db/LLANtr`

**方法**: POST, GET, PUT, DELETE | **参数**: 4 必填 + 1 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `LL_NAME` | 文字（字符串） | **是** | Name of Line Lane |
| `LANE_ITEMS` | Array[Object] | **是** | Lane Items• Insert the data as an object |
| `ELEM` | 整数 | **是** | Element ID |
| `FACTOR` | 数字 | **是** | Factor |
| `SPECIAL_LANE_ITEMS` | Array | 否 | Usedonlywhenimporting |

**最简 JSON**：
```json
{
  "LLANTR": {
    "LL_NAME": "<LL_NAME>",
    "LANE_ITEMS": [],
    "properties": {
      "LANE_ITEMS": {
        "items": {
          "properties": {
            "ELEM": 0,
            "FACTOR": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "LL_NAME": "LL_01",
      "LANE_ITEMS": [
        {
          "ELEM": 1,
          "FACTOR": 1.1
        },
        {
          "ELEM": 2,
          "FACTOR": 1.1
        },
        {
          "ELEM": 3,
          "FACTOR": 1.1
        }
      ]
    },
    "2": {
      "LL_NAME": "LL_02",
      "LANE_ITEMS": [
        {
          "ELEM": 163,
          "FACTOR": 1.2
        },
        {
          "ELEM": 164,
          "FACTOR": 1.2
        },
        {
          "ELEM": 165,
          "FACTOR": 1.2
        }
      ]
    }
  }
}
```


---

### Traffic Line Lanes - Moving Load Optimizaion — `/db/LLANop`

**方法**: POST, GET, PUT, DELETE | **参数**: 8 必填 + 15 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `LL_NAME` | 文字（字符串） | **是** | Name of Line Lane |
| `LOAD_DIST` | 文字（字符串） | **是** | Load Distribution• Lane Element: "LANE"• Cross Beam: "CROSS" |
| `MOVING` | 文字（字符串） | **是** | Moving Direction• Forward: "FORWARD"• Backward: "BACKWARD"• Both: "BOTH" |
| `OPTIM_WIDTH` | 数字 | **是** | Optimization Lane |
| `LANE_WIDTH` | 数字 | **是** | Lane Width |
| `OFFSET_TYPE` | 整数 | **是** | Offset Type (Generate Analysis Lanes)• Number of Lane: 0• Offset from Centerline |
| `LANE_ITEMS` | Array[Object] | **是** | Lane Items• Insert the data as an object |
| `ELEM` | 整数 | **是** | Element No. |
| `GROUP_NAME` | 文字（字符串） | 否 | Name of Structure Group²⁾ |
| `SKEW_START` | 数字 | 否 | Skew Start²⁾ |
| `SKEW_END` | 数字 | 否 | Skew End²⁾ |
| `DIVIDE_NUM` | 整数 | 否 | Divide Number (Number of Lanes)• if "OFFSET_TYPE": 0 |
| `ANAL_LANE_OFFSET` | 数字 | 否 | Analysis Lane Offset• if "OFFSET_TYPE": 1 |
| `WHEEL_SPACE` | 数字 | 否 | Wheel Spacing |
| `MARGIN` | 数字 | 否 | Margin |
| `OPT_STRADD` | 是/否（布尔值） | 否 | Use Straddling Lane Type¹⁾ |
| `SPECIAL_LANE_ITEMS` | Array | 否 | Usedonlywhenimporting |
| `ECC` | 数字 | 否 | Eccentricity |
| ... | ... | ... | *还有 5 个可选参数* |

**最简 JSON**：
```json
{
  "LLANOP": {
    "LL_NAME": "<LL_NAME>",
    "LOAD_DIST": "<LOAD_DIST>",
    "MOVING": "<MOVING>",
    "OPTIM_WIDTH": 0,
    "LANE_WIDTH": 0,
    "OFFSET_TYPE": 0,
    "LANE_ITEMS": [],
    "properties": {
      "LANE_ITEMS": {
        "items": {
          "properties": {
            "ELEM": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "LL_NAME": "LL_01",
      "LOAD_DIST": "LANE",
      "GROUP_NAME": "",
      "SKEW_START": 0,
      "SKEW_END": 0,
      "MOVING": "BOTH",
      "OPTIM_WIDTH": 5,
      "LANE_WIDTH": 3,
      "OFFSET_TYPE": 0,
      "DIVIDE_NUM": 2,
      "ANAL_LANE_OFFSET": 1,
      "WHEEL_SPACE": 1.8288000000000002,
      "MARGIN": 0.1,
      "LANE_ITEMS": [
        {
          "ELEM": 1,
          "ECC": -1.5,
          "FACT": 1.25,
          "SPAN_START": true
        },
        {
          "ELEM": 2,
          "ECC": -1.5,
          "FACT": 1.25,
          "SPAN_START": true
        },
        {
          "ELEM": 3,
          "ECC": -1.5,
          "FACT": 1.25,
          "SPAN_START": true
        }
      ]
    },
    "2": {
      "LL_NAME": "LL_02",
      "LOAD_DIST": "CROSS",
      "GROUP_NAME": "CrossBeam",
      "SKEW_START": 10,
      "SKEW_END": 15,
      "MOVING": "BACKWARD",
      "OPTIM_WIDTH": 5,
      "LANE_WIDTH": 3,
      "OFFSET_TYPE": 1,
      "DIVIDE_NUM": 2,
      "ANAL_LANE_OFFSET": 3,
      "WHEEL_SPACE": 1.8288000000000002,
      "MARGIN": 0.1,
      "LANE_ITEMS": [
        {
          "ELEM": 163,
          "ECC": -1.5,
          "FACT": 1.25,
          "SPAN_START": true
        },
        {
          "ELEM": 164,
          "ECC": -1.5,
          "FACT": 1.25,
          "SPAN_START": false
        },
        {
          "ELEM": 165,
          "ECC": -1.5,
          "FACT": 1.25,
          "SPAN_START": false
        }
      ]
    }
  }
}
```


---

### Traffic Surface Lanes — `/db/SLAN`

**方法**: POST, GET, PUT, DELETE | **参数**: 5 必填 + 14 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Name of Surface Lane |
| `WIDTH` | 数字 | **是** | Lane Width |
| `MV_DIR` | 文字（字符串） | **是** | Moving Direction• Forward: "FORWARD"• Backward: "BACKWARD"• Both: "BOTH" |
| `LANE_ITEMS` | Array[Object] | **是** | Lane Items• Insert the data as an object |
| `NODE` | 整数 | **是** | Node No. |
| `WHEEL_SPACE` | 数字 | 否 | Wheel Spacing |
| `SKEW_START` | 数字 | 否 | Skew Start |
| `SKEW_END` | 数字 | 否 | Skew End |
| `bOPTIMIZE` | 是/否（布尔值） | 否 | Transverse Lane Optimization¹⁾ |
| `ALLOW_WIDTH` | 数字 | 否 | Allow Width for Optimization¹⁾ |
| `SEQ` | 整数 | 否 | Sequence Number (Unique) |
| `OFFSET` | 数字 | 否 | Offset Distance to Lane Center |
| `IMPACT_FACTOR` | 数字 | 否 | Impact Factor |
| `bSPAN_START` | 是/否（布尔值） | 否 | Span Start |
| `CENTRI_FORCE` | 数字 | 否 | Centrifugal Force Factor |
| ... | ... | ... | *还有 4 个可选参数* |

**最简 JSON**：
```json
{
  "SLAN": {
    "NAME": "<NAME>",
    "WIDTH": 0,
    "MV_DIR": "<MV_DIR>",
    "LANE_ITEMS": [],
    "properties": {
      "LANE_ITEMS": {
        "items": {
          "properties": {
            "NODE": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "NAME": "LL_01",
      "WIDTH": 3,
      "WHEEL_SPACE": 1.8,
      "SKEW_START": 10,
      "SKEW_END": 15,
      "bOPTIMIZE": true,
      "ALLOW_WIDTH": 3,
      "MV_DIR": "BOTH",
      "LANE_ITEMS": [
        {
          "NODE": 1,
          "OFFSET": -1.5
        },
        {
          "NODE": 2,
          "OFFSET": -1.5
        },
        {
          "NODE": 3,
          "OFFSET": -1.5
        },
        {
          "NODE": 4,
          "OFFSET": -1.5
        }
      ]
    }
  }
}
```


---

### Traffic Surface Lanes - China — `/db/SLANch`

**方法**: POST, GET, PUT, DELETE | **参数**: 5 必填 + 8 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Name of Surface Lane |
| `WIDTH` | 数字 | **是** | Lane Width |
| `MV_DIR` | 文字（字符串） | **是** | Moving Direction• Forward: "FORWARD"• Backward: "BACKWARD"• Both: "BOTH" |
| `LANE_ITEMS` | Array[Object] | **是** | Lane Items• Insert the data as an object |
| `NODE` | 整数 | **是** | Node No. |
| `WHEEL_SPACE` | 数字 | 否 | Wheel Spacing |
| `SKEW_START` | 数字 | 否 | Skew Start |
| `SKEW_END` | 数字 | 否 | Skew End |
| `bOPTIMIZE` | 是/否（布尔值） | 否 | Transverse Lane Optimization |
| `ALLOW_WIDTH` | 数字 | 否 | Allow Width for Optimization |
| `SEQ` | 整数 | 否 | Sequence Number (Unique) |
| `OFFSET` | 数字 | 否 | Offset Distance to Lane Center |
| `SPAN_LENGTH` | 数字 | 否 | Span Length |

**最简 JSON**：
```json
{
  "SLANCH": {
    "NAME": "<NAME>",
    "WIDTH": 0,
    "MV_DIR": "<MV_DIR>",
    "LANE_ITEMS": [],
    "properties": {
      "LANE_ITEMS": {
        "items": {
          "properties": {
            "NODE": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "NAME": "LL_01",
      "WIDTH": 3,
      "WHEEL_SPACE": 1.8,
      "SKEW_START": 10,
      "SKEW_END": 15,
      "bOPTIMIZE": true,
      "ALLOW_WIDTH": 3,
      "MV_DIR": "BOTH",
      "LANE_ITEMS": [
        {
          "NODE": 1,
          "OFFSET": -1.5,
          "SPAN_LENGTH": 12
        },
        {
          "NODE": 2,
          "OFFSET": -1.5,
          "SPAN_LENGTH": 12
        },
        {
          "NODE": 3,
          "OFFSET": -1.5,
          "SPAN_LENGTH": 12
        },
        {
          "NODE": 4,
          "OFFSET": -1.5,
          "SPAN_LENGTH": 12
        }
      ]
    }
  }
}
```


---

### Traffic Surface Lanes - Moving Load Optimization — `/db/SLANop`

**方法**: POST, GET, PUT, DELETE | **参数**: 8 必填 + 13 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `LANE_NAME` | 文字（字符串） | **是** | Name of Surface Lane |
| `MOVING` | 文字（字符串） | **是** | Moving Direction• Forward: "FORWARD"• Backward: "BACKWARD"• Both: "BOTH" |
| `OPTIMIZE_WIDTH` | 数字 | **是** | Optimization Lane |
| `LANE_WIDTH` | 数字 | **是** | Lane Width |
| `OFFSET_TYPE` | 整数 | **是** | Offset Type (Generate Analysis Lanes)• Number of Lane: 0• Offset from Centerline |
| `CHINA_ITEMS` | Array[Object] | **是** | Lane Items• Insert the data as an object |
| `ITEMS` | Array[Object] | **是** | Lane Items• Insert the data as an object |
| `NODE_KEY` | 整数 | **是** | Node No. |
| `LANE_ID` | 整数 | 否 | LaneID |
| `SKEW_START` | 数字 | 否 | Skew Start |
| `SKEW_END` | 数字 | 否 | Skew End |
| `ANALYSIS_LANE_OFFSET` | 数字 | 否 | Analysis Lane Offset• if "OFFSET_TYPE": 1 |
| `WHEEL_SPACE` | 数字 | 否 | Wheel Spacing |
| `MARGIN` | 数字 | 否 | Margin |
| `OPT_STRADD` | 是/否（布尔值） | 否 | Use Straddling Lane Type¹⁾ |
| `DIVIDE_NUM` | 整数 | 否 | Divide Number (Number of Lanes)• if "OFFSET_TYPE": 0 |
| `OFFSET` | 数字 | 否 | Offset Distance to Lane Center |
| `FACTOR` | 数字 | 否 | Impact Factor |
| ... | ... | ... | *还有 3 个可选参数* |

**最简 JSON**：
```json
{
  "SLANOP": {
    "LANE_NAME": "<LANE_NAME>",
    "MOVING": "<MOVING>",
    "OPTIMIZE_WIDTH": 0,
    "LANE_WIDTH": 0,
    "OFFSET_TYPE": 0,
    "CHINA_ITEMS": [],
    "ITEMS": [],
    "properties": {
      "CHINA_ITEMS": {
        "items": {
          "properties": {
            "NODE_KEY": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "LANE_NAME": "LL_01",
      "SKEW_START": 10,
      "SKEW_END": 15,
      "MOVING": "BOTH",
      "OPTIMIZE_WIDTH": 4,
      "LANE_WIDTH": 3,
      "WHEEL_SPACE": 1.8288,
      "MARGIN": 0.1,
      "OFFSET_TYPE": 0,
      "DIVIDE_NUM": 2,
      "ITEMS": [
        {
          "NODE_KEY": 1,
          "OFFSET": -1.5,
          "FACTOR": 1.25,
          "SPAN_START": true
        },
        {
          "NODE_KEY": 2,
          "OFFSET": -1.5,
          "FACTOR": 1.25,
          "SPAN_START": false
        },
        {
          "NODE_KEY": 3,
          "OFFSET": -1.5,
          "FACTOR": 1.25,
          "SPAN_START": false
        },
        {
          "NODE_KEY": 4,
          "OFFSET": -1.5,
          "FACTOR": 1.25,
          "SPAN_START": false
        }
      ]
    },
    "2": {
      "LANE_NAME": "LL_02",
      "SKEW_START": 10,
      "SKEW_END": 15,
      "MOVING": "BACKWARD",
      "OPTIMIZE_WIDTH": 4,
      "LANE_WIDTH": 3,
      "ANALYSIS_LANE_OFFSET": 2,
      "WHEEL_SPACE": 1.8288,
      "MARGIN": 0.1,
      "OFFSET_TYPE": 1,
      "ITEMS": [
        {
          "NODE_KEY": 83,
          "OFFSET": -1.5,
          "FACTOR": 1.25,
          "SPAN_START": true
        },
        {
          "NODE_KEY": 84,
          "OFFSET": -1.5,
          "FACTOR": 1.25,
          "SPAN_START": false
        },
        {
          "NODE_KEY": 85,
          "OFFSET": -1.5,
          "FACTOR": 1.25,
          "SPAN_START": false
        },
        {
          "NODE_KEY": 86,
          "OFFSET": -1.5,
          "FACTOR": 1.25,
          "SPAN_START": false
        }
      ]
    }
  }
}
```


---

### Vehicles - AASHTO Standard — `/db/MVHL`

**方法**: POST, GET, PUT, DELETE | **参数**: 9 必填 + 11 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `MVLD_CODE` | 整数 | **是** | Function Name• AASHTO Standard: 1 |
| `VEHICLE_LOAD_NAME` | 文字（字符串） | **是** | Vehicular Load Name |
| `VEHICLE_LOAD_NUM` | 整数 | **是** | Vehicular Load Number• Standard: 1• User Defined: 2 |
| `VEHICLE_TYPE_NAME` | 文字（字符串） | **是** | Vehicular Type Name¹⁾ |
| `STANDARD_CODE` | 文字（字符串） | **是** | Standard Code¹⁾ |
| `USER_LOAD_TYPE` | 文字（字符串） | **是** | User Defined Load Type• Truck/Lane: "Truck/Lane"• Train: "Train Load" |
| `VEH_DEFAULT` | 对象（一组键值对） | **是** | Vehicle |
| `POINT_LOAD` | 数字 | **是** | Load |
| `POINT_DIST` | 数字 | **是** | Spacing |
| `UNIFORM_LOAD` | 数字 | 否 | Uniform Distribution Load |
| `DYN_LOAD_ALLOWANCE` | 整数 | 否 | Dynamic Load Allowance (%)• Only for Turkey - KGM-45 |
| `W1` | 数字 | 否 | Distribution Load - dW1 |
| `W2` | 数字 | 否 | Distribution Load - dW2 |
| `D1` | 数字 | 否 | Spacing - dD1 |
| `D2` | 数字 | 否 | Spacing - dD2 |
| `PL` | 数字 | 否 | Axle Load for Member Force |
| `PLM` | 数字 | 否 | Axle Load for Moment |
| `PLV` | 数字 | 否 | Axle Load for Shear force |
| `CENT_F` | 是/否（布尔值） | 否 | AddCentrifugalForce |
| ... | ... | ... | *还有 1 个可选参数* |

**最简 JSON**：
```json
{
  "MVHL": {
    "MVLD_CODE": 0,
    "VEHICLE_LOAD_NAME": "<VEHICLE_LOAD_NAME>",
    "VEHICLE_LOAD_NUM": 0,
    "VEHICLE_TYPE_NAME": "<VEHICLE_TYPE_NAME>",
    "STANDARD_CODE": "<STANDARD_CODE>",
    "USER_LOAD_TYPE": "<USER_LOAD_TYPE>",
    "VEH_DEFAULT": {},
    "properties": {
      "LOAD_ITEMS": {
        "items": {
          "properties": {
            "POINT_LOAD": 0,
            "POINT_DIST": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "MVLD_CODE": 1,
      "VEHICLE_LOAD_NAME": "US(ASL)_H15-44",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "H15-44",
      "STANDARD_CODE": "AASHTO-STD",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    },
    "2": {
      "MVLD_CODE": 1,
      "VEHICLE_LOAD_NAME": "US(ASL)_HS15-44",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "HS15-44",
      "STANDARD_CODE": "AASHTO-STD",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    },
    "3": {
      "MVLD_CODE": 1,
      "VEHICLE_LOAD_NAME": "US(ASL)_H15-44L",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "H15-44L",
      "STANDARD_CODE": "AASHTO-STD",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    },
    "4": {
      "MVLD_CODE": 1,
      "VEHICLE_LOAD_NAME": "US(ASL)_HS15-44L",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "HS15-44L",
      "STANDARD_CODE": "AASHTO-STD",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    },
    "5": {
      "MVLD_CODE": 1,
      "VEHICLE_LOAD_NAME": "US(ASL)_H20-44",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "H20-44",
      "STANDARD_CODE": "AASHTO-STD",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    },
    "6": {
      "MVLD_CODE": 1,
      "VEHICLE_LOAD_NAME": "US(ASL)_HS20-44",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "HS20-44",
      "STANDARD_CODE": "AASHTO-STD",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    },
    "7": {
      "MVLD_CODE": 1,
      "VEHICLE_LOAD_NAME": "US(ASL)_H20-44L",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "H20-44L",
      "STANDARD_CODE": "AASHTO-STD",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    },
    "8": {
      "MVLD_CODE": 1,
      "VEHICLE_LOAD_NAME": "US(ASL)_HS20-44L",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "HS20-44L",
      "STANDARD_CODE": "AASHTO-STD",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    },
    "9": {
      "MVLD_CODE": 1,
      "VEHICLE_LOAD_NAME": "US(ASL)_HS-25",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "HS-25",
      "STANDARD_CODE": "AASHTO-STD",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    },
    "10": {
      "MVLD_CODE": 1,
      "VEHICLE_LOAD_NAME": "US(ASL)_HS-25L",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "HS-25L",
      "STANDARD_CODE": "AASHTO-STD",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    },
    "11": {
      "MVLD_CODE": 1,
      "VEHICLE_LOAD_NAME": "US(ASL)_AML",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "AML",
      "STANDARD_CODE": "AASHTO-STD",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    },
    "12": {
      "MVLD_CODE": 1,
      "VEHICLE_LOAD_NAME": "US(ALL)_AASHTOLegalType3",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "AASHTOLegalType3",
      "STANDARD_CODE": "ASSHTO-LEGAL",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    },
    "13": {
      "MVLD_CODE": 1,
      "VEHICLE_LOAD_NAME": "US(ALL)_AASHTOLegalType3S2",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "AASHTOLegalType3S2",
      "STANDARD_CODE": "ASSHTO-LEGAL",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    },
    "14": {
      "MVLD_CODE": 1,
      "VEHICLE_LOAD_NAME": "US(ALL)_AASHTOLegalType3-3",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "AASHTOLegalType3-3",
      "STANDARD_CODE": "ASSHTO-LEGAL",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    },
    "15": {
      "MVLD_CODE": 1,
      "VEHICLE_LOAD_NAME": "US(ALL)_AASHTOLegalLaneType",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "AASHTOLegalLaneType",
      "STANDARD_CODE": "ASSHTO-LEGAL",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    },
    "16": {
      "MVLD_CODE": 1,
      "VEHICLE_LOAD_NAME": "US(CSL17)_P5-Design",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "P5-Design",
      "STANDARD_CODE": "CALTRANS_2017",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    },
    "17": {
      "MVLD_CODE": 1,
      "VEHICLE_LOAD_NAME": "US(CSL17)_P7-Design",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "P7-Design",
      "STANDARD_CODE": "CALTRANS_2017",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    },
    "18": {
      "MVLD_CODE": 1,
      "VEHICLE_LOAD_NAME": "US(CSL17)_P9-Design",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "P9-Design",
      "STANDARD_CODE": "CALTRANS_2017",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    },
    "19": {
      "MVLD_CODE": 1,
      "VEHICLE_LOAD_NAME": "US(CSL17)_P11-Design",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "P11-Design",
      "STANDARD_CODE": "CALTRANS_2017",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    },
    "20": {
      "MVLD_CODE": 1,
      "VEHICLE_LOAD_NAME": "US(CSL17)_P13-Design",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "P13-Design",
      "STANDARD_CODE": "CALTRANS_2017",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    },
    "21": {
      "MVLD_CODE": 1,
      "VEHICLE_LOAD_NAME": "US(CSL17)_P15-Design",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "P15-Design",
      "STANDARD_CODE": "CALTRANS_2017",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    },
    "22": {
      "MVLD_CODE": 1,
      "VEHICLE_LOAD_NAME": "US(CSL17)_P5-VS",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "P5-VS",
      "STANDARD_CODE": "CALTRANS_2017",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    },
    "23": {
      "MVLD_CODE": 1,
      "VEHICLE_LOAD_NAME": "US(CSL17)_P7-VS",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "P7-VS",
      "STANDARD_CODE": "CALTRANS_2017",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    },
    "24": {
      "MVLD_CODE": 1,
      "VEHICLE_LOAD_NAME": "US(CSL17)_P9-VS",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "P9-VS",
      "STANDARD_CODE": "CALTRANS_2017",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    },
    "25": {
      "MVLD_CODE": 1,
      "VEHICLE_LOAD_NAME": "US(CSL17)_P11-VS",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "P11-VS",
      "STANDARD_CODE": "CALTRANS_2017",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    },
    "26": {
      "MVLD_CODE": 1,
      "VEHICLE_LOAD_NAME": "US(CSL17)_P13-VS",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "P13-VS",
      "STANDARD_CODE": "CALTRANS_2017",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    },
    "27": {
      "MVLD_CODE": 1,
      "VEHICLE_LOAD_NAME": "US(CSL17)_P15-VS",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "P15-VS",
      "STANDARD_CODE": "CALTRANS_2017",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    },
    "28": {
      "MVLD_CODE": 1,
      "VEHICLE_LOAD_NAME": "US(CSL)_P5-Design",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "P5-Design",
      "STANDARD_CODE": "CALTRANS",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    },
    "29": {
      "MVLD_CODE": 1,
      "VEHICLE_LOAD_NAME": "US(CSL)_P7-Design",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "P7-Design",
      "STANDARD_CODE": "CALTRANS",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    },
    "30": {
      "MVLD_CODE": 1,
      "VEHICLE_LOAD_NAME": "US(CSL)_P9-Design",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "P9-Design",
      "STANDARD_CODE": "CALTRANS",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    },
    "31": {
      "MVLD_CODE": 1,
      "VEHICLE_LOAD_NAME": "US(CSL)_P11-Design",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "P11-Design",
      "STANDARD_CODE": "CALTRANS",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    },
    "32": {
      "MVLD_CODE": 1,
      "VEHICLE_LOAD_NAME": "US(CSL)_P13-Design",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "P13-Design",
      "STANDARD_CODE": "CALTRANS",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    },
    "33": {
      "MVLD_CODE": 1,
      "VEHICLE_LOAD_NAME": "US(CSL)_P15-Design",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "P15-Design",
      "STANDARD_CODE": "CALTRANS",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    },
    "34": {
      "MVLD_CODE": 1,
      "VEHICLE_LOAD_NAME": "US(CSL)_P5-VS",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "P5-VS",
      "STANDARD_CODE": "CALTRANS",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    },
    "35": {
      "MVLD_CODE": 1,
      "VEHICLE_LOAD_NAME": "US(CSL)_P7-VS",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "P7-VS",
      "STANDARD_CODE": "CALTRANS",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    },
    "36": {
      "MVLD_CODE": 1,
      "VEHICLE_LOAD_NAME": "US(CSL)_P9-VS",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "P9-VS",
      "STANDARD_CODE": "CALTRANS",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    },
    "37": {
      "MVLD_CODE": 1,
      "VEHICLE_LOAD_NAME": "US(CSL)_P11-VS",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "P11-VS",
      "STANDARD_CODE": "CALTRANS",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    },
    "38": {
      "MVLD_CODE": 1,
      "VEHICLE_LOAD_NAME": "US(CSL)_P13-VS",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "P13-VS",
      "STANDARD_CODE": "CALTRANS",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    },
    "39": {
      "MVLD_CODE": 1,
      "VEHICLE_LOAD_NAME": "US(CSL)_P15-VS",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "P15-VS",
      "STANDARD_CODE": "CALTRANS",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    },
    "40": {
      "MVLD_CODE": 1,
      "VEHICLE_LOAD_NAME": "US(Turkey)_H30-S24",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "H30-S24",
      "STANDARD_CODE": "TURKEY",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    },
    "41": {
      "MVLD_CODE": 1,
      "VEHICLE_LOAD_NAME": "US(Turkey)_H30-S24L",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "H30-S24L",
      "STANDARD_CODE": "TURKEY",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    },
    "42": {
      "MVLD_CODE": 1,
      "VEHICLE_LOAD_NAME": "US(Turkey)_H20-S16",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "H20-S16",
      "STANDARD_CODE": "TURKEY",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    },
    "43": {
      "MVLD_CODE": 1,
      "VEHICLE_LOAD_NAME": "US(Turkey)_H20-S16L",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "H20-S16L",
      "STANDARD_CODE": "TURKEY",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    },
    "44": {
      "MVLD_CODE": 1,
      "VEHICLE_LOAD_NAME": "US(Turkey)_KGM-45",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "KGM-45",
      "STANDARD_CODE": "TURKEY",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    },
    "45": {
      "MVLD_CODE": 1,
      "VEHICLE_LOAD_NAME": "US(Ohters)_CE-80",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "CE-80",
      "STANDARD_CODE": "OTHERS",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    },
    "46": {
      "MVLD_CODE": 1,
      "VEHICLE_LOAD_NAME": "US(Ohters)_UIC80",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "UIC80",
      "STANDARD_CODE": "OTHERS",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    },
    "47": {
      "MVLD_CODE": 1,
      "VEHICLE_LOAD_NAME": "US(Ohters)_M1600",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "M1600",
      "STANDARD_CODE": "OTHERS",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    },
    "48": {
      "MVLD_CODE": 1,
      "VEHICLE_LOAD_NAME": "US(Ohters)_S1600",
      "VEHICLE_LOAD_NUM": 1,
      "VEHICLE_TYPE_NAME": "S1600",
      "STANDARD_CODE": "OTHERS",
      "VEH_DEFAULT": {
        "DYN_LOAD_ALLOWANCE": 0,
        "CENT_F": false
      }
    }
  }
}
```


---

### Vehicles - Transverse — `/db/MVHLtr`

**方法**: POST, GET, PUT, DELETE | **参数**: 10 必填 + 2 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Vehicular Load Name |
| `P` | 数字 | **是** | Wheel Load(P) |
| `W` | 数字 | **是** | Distribution Width |
| `LW` | 数字 | **是** | Longitudinal Width |
| `NUM` | 整数 | **是** | Max. Number of Lanes (n) |
| `DW` | 数字 | **是** | Distance between Wheels (Dw) |
| `DV` | 数字 | **是** | Min. Distance between Vehicle (Dv) |
| `ML` | 数字 | **是** | Location (Ml) |
| `MW` | 数字 | **是** | Width (Mw) |
| `LEFT_LANES` | 整数 | **是** | Max. Number of Left Lanes (n1) |
| `DE` | 数字 | 否 | Edge Distance of Wheel Loads (De) |
| `OPT_MEDIAN_STRIP` | 是/否（布尔值） | 否 | Median Strip Option |

**最简 JSON**：
```json
{
  "MVHLTR": {
    "NAME": "<NAME>",
    "P": 0,
    "W": 0,
    "LW": 0,
    "NUM": 0,
    "DW": 0,
    "DV": 0,
    "ML": 0,
    "MW": 0,
    "LEFT_LANES": 0
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "NAME": "Trans",
      "P": 120,
      "W": 2.3,
      "LW": 10,
      "NUM": 4,
      "DW": 0.3,
      "DV": 0.4,
      "DE": 0.5,
      "OPT_MEDIAN_STRIP": false
    },
    "2": {
      "NAME": "Trans_Medians",
      "P": 120,
      "W": 2.3,
      "LW": 10,
      "NUM": 4,
      "DW": 0.3,
      "DV": 0.4,
      "DE": 0.5,
      "OPT_MEDIAN_STRIP": true,
      "ML": 15,
      "MW": 1,
      "LEFT_LANES": 2
    }
  }
}
```


---

### Moving Load Cases — `/db/MVLD`

**方法**: POST, GET, PUT, DELETE | **参数**: 32 必填 + 3 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `LCNAME` | 对象（一组键值对） | **是** | Load Case Name |
| `TYPE` | 对象（一组键值对） | **是** | Load Type¹⁾• General Load: 0• Load Case for Permit Vehicle: 1• Moving Load Optim |
| `AUTO_OPTIMIZE` | 对象（一组键值对） | **是** | Moving Load Optimization |
| `VEHICLE_LOAD_NAME` | 文字（字符串） | **是** | Permit Vehicle Name |
| `LANE_NAME` | 文字（字符串） | **是** | Loaded Lane Name |
| `SCALE_FACTORS` | Array[Number,6] | **是** | Multiple Presence Factor• [L1, L2, L3, More, More, More] |
| `FATIGUE` | 是/否（布尔值） | **是** | Fatigue Option• Load Model Fatigue: true |
| `MIN_VEHL_DIST` | 数字 | **是** | Min. Vehicle Distance |
| `MIN_NUM_VEHICLE` | 整数 | **是** | Min. Number of Vehicle |
| `MAX_NUM_VEHICLE` | 整数 | **是** | Max. Number of Vehicle |
| `LOAD_MODEL` | 整数 | **是** | Select Load Model• General: 0• Fatigue: 1• Heavy Load Platform: 2• Rail Traffic  |
| `OPTIMIZE_ITEMS` | Array[Object] | **是** | Assignment Vehicle• Insert the data as an object |
| `PERMIT_LOAD` | 对象（一组键值对） | **是** | Load Case for Permit Vehicle |
| `REF_LANE` | 文字（字符串） | **是** | Reference Lane |
| `SCALE_FACTOR` | 数字 | **是** | Scale Factor |
| `ASL` | 对象（一组键值对） | **是** | Australia Heavy Load Platform |
| `MULTIPLE_FACTOR` | 数字 | **是** | Unobstructed Lane Scale Factor• 0.5 |
| `VEHICLE_LOAD_NAME2` | 文字（字符串） | **是** | Load Case Data - M1600 or S1600 |
| `MIN_LOADED_LANE` | 整数 | **是** | Min. Number of Loaded Lanes |
| `MAX_LOADED_LANE` | 整数 | **是** | Max. Number of Loaded Lanes |
| `LINE_ITEMS` | 对象（一组键值对） | **是** | Defined Lane |
| `DEFAULT` | 对象（一组键值对） | **是** | General Data |
| `COMB_OPTION` | 文字（字符串） | **是** | Loading Effect• Combined: "COMBINED"• Independent: "INDEPENDENT" |
| `LOAD_COMB_TYPE` | 整数 | **是** | Load Combination Type• Limit State Group I: 0• Limit State Group I - Fatigue: 1• |
| `LANE_FACTOR_TYPE` | 整数 | **是** | Lane Factor Type• Multiple Presence Factor: 1 |
| `_2_LANE_FACTOR_1` | 数字 | **是** | Multi Lane Factor in KS Rail Load• 2 Lane - Lane 1 |
| `_2_LANE_FACTOR_2` | 数字 | **是** | Multi Lane Factor in KS Rail Load• 2 Lane - Lane 2 |
| `_3_LANE_FACTOR_1` | 数字 | **是** | Multi Lane Factor in KS Rail Load• Above 3 Lane - Lane 1 |
| `_3_LANE_FACTOR_2` | 数字 | **是** | Multi Lane Factor in KS Rail Load• Above 3 Lane - Lane 2 |
| `_3_LANE_FACTOR_3` | 数字 | **是** | Multi Lane Factor in KS Rail Load• Above 3 Lane - Lane 3 |
| `_3_LANE_FACTOR_4` | 数字 | **是** | Multi Lane Factor in KS Rail Load• Above 3 Lane - Lane 4 |
| `SUB_LOAD_DATAS` | Array[Object] | **是** | Sub Load Cases• Insert data as object |
| `DESC` | 对象（一组键值对） | 否 | Description |
| `NUM_LOADED_LANES` | 整数 | 否 | NumLoadedLanes |
| `ECC` | 数字 | 否 | Eccentricity |

**最简 JSON**：
```json
{
  "MVLD": {
    "LCNAME": {},
    "TYPE": {},
    "AUTO_OPTIMIZE": {
      "LANE_NAME": "<LANE_NAME>",
      "MIN_VEHL_DIST": 0,
      "MIN_NUM_VEHICLE": 0,
      "MAX_NUM_VEHICLE": 0,
      "OPTIMIZE_ITEMS": []
    },
    "ASL": {
      "MULTIPLE_FACTOR": 0,
      "VEHICLE_LOAD_NAME2": "<VEHICLE_LOAD_NAME2>",
      "MIN_LOADED_LANE": 0,
      "MAX_LOADED_LANE": 0,
      "LINE_ITEMS": {}
    },
    "DEFAULT": {
      "COMB_OPTION": "<COMB_OPTION>",
      "LOAD_COMB_TYPE": 0,
      "LANE_FACTOR_TYPE": 0,
      "_2_LANE_FACTOR_1": 0,
      "_2_LANE_FACTOR_2": 0,
      "_3_LANE_FACTOR_1": 0,
      "_3_LANE_FACTOR_2": 0,
      "_3_LANE_FACTOR_3": 0,
      "_3_LANE_FACTOR_4": 0,
      "SUB_LOAD_DATAS": []
    },
    "PERMIT_LOAD": {
      "REF_LANE": "<REF_LANE>",
      "SCALE_FACTOR": 0
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "LCNAME": "MV_Case1",
      "DESC": "",
      "TYPE": 0,
      "DEFAULT": {
        "SCALE_FACTORS": [
          1,
          0.9,
          0.8,
          0.7,
          0.65,
          0.65
        ],
        "COMB_OPTION": "COMBINED",
        "LANE_FACTOR_TYPE": 1,
        "SUB_LOAD_DATAS": [
          {
            "VEHICLE_TYPE": "VL",
            "VEHICLE_NAME": "ST_KL-510FTG",
            "SCALE_FACTOR": 1,
            "MIN_LOADED_LANE": 1,
            "MAX_LOADED_LANE": 2,
            "LANE_NAMES": [
              "LL_01",
              "LL_02"
            ]
          }
        ]
      }
    },
    "2": {
      "LCNAME": "MV_Case2",
      "DESC": "",
      "TYPE": 0,
      "DEFAULT": {
        "SCALE_FACTORS": [
          1,
          0.9,
          0.8,
          0.7,
          0.65,
          0.65
        ],
        "COMB_OPTION": "INDEPENDENT",
        "LANE_FACTOR_TYPE": 1,
        "SUB_LOAD_DATAS": [
          {
            "VEHICLE_TYPE": "VL",
            "VEHICLE_NAME": "ST_KL-510FTG",
            "SCALE_FACTOR": 1,
            "MIN_LOADED_LANE": 1,
            "MAX_LOADED_LANE": 2,
            "LANE_NAMES": [
              "LL_01",
              "LL_02"
            ]
          }
        ]
      }
    }
  }
}
```


---

### Moving Load Cases - China — `/db/MVLDch`

**方法**: POST, GET, PUT, DELETE | **参数**: 18 必填 + 3 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `LCNAME` | 对象（一组键值对） | **是** | Load Case Name |
| `BRIDGE_TYPE` | 文字（字符串） | **是** | Bridge Type• Old Urban Bridge: 0• Highway Bridge/New Urban Bridge: 1• JTG B01-20 |
| `SCALE_FACTOR_O` | Array[Number, 8] | **是** | Scale factor for Old Urban Bridge• [1, 2, 3, 4, 5, 7, >= 8] |
| `SCALE_FACTOR_N` | Array[Number, 8] | **是** | Scale factor for Highway Bridge/New Urban Bridge• [1, 2, 3, 4, 5, 7, >= 8] |
| `SCALE_FACTOR_JTG` | Array[Number, 8] | **是** | Scale factor for JTG B01-2014• [1, 2, 3, 4, 5, 7, >= 8] |
| `MIN_VEHICLE_DIST` | 数字 | **是** | Min. Vehicle Distance |
| `LOADED_LANE_NAME` | 文字（字符串） | **是** | Loaded Lane Name |
| `MIN_NUM_VEHICLE` | 整数 | **是** | Min. Number of Vehicle |
| `MAX_NUM_VEHICLE` | 整数 | **是** | Max. Number of Vehicle |
| `LOADING_EFFECT` | 整数 | **是** | Combination Option• Combined: 0• Independent: 1 |
| `AUTO_OPTIMIZE_ITEMS` | Array[Object] | **是** | Assignment Vehicle• Insert the data as an object |
| `VEHICLE_TYPE` | 文字（字符串） | **是** | Type of Vehicle Class• Vehicle Load: "VL"• Vehicle Class: "VC" |
| `VEHICLE_CLASS` | 文字（字符串） | **是** | Name of Vehicle Class |
| `SCALE_FACTOR` | 数字 | **是** | Scale Factor |
| `MIN_NUM_LOADED_LANES` | 整数 | **是** | Min. Number of Loaded Lane |
| `MAX_NUM_LOADED_LANES` | 整数 | **是** | Max. Number of Loaded Lane |
| `SELECTED_LANES` | 字符串数组 | **是** | Selected Lane |
| `VEHICLE_NAME` | 文字（字符串） | **是** | Name of Vehicle Class |
| `DESC` | 文字（字符串） | 否 | Description |
| `OPT_AUTO_OPTIMIZE` | 是/否（布尔值） | 否 | Moving Load Optimization• General Load: false• Moving Load Optimization: true |
| `SUB_LOAD_ITEMS` | Array[Object] | 否 | Sub-Load Cases• Insert the data as an object |

**最简 JSON**：
```json
{
  "MVLDCH": {
    "LCNAME": {},
    "BRIDGE_TYPE": "<BRIDGE_TYPE>",
    "SCALE_FACTOR_O": 0,
    "SCALE_FACTOR_N": 0,
    "SCALE_FACTOR_JTG": 0,
    "MIN_VEHICLE_DIST": 0,
    "LOADED_LANE_NAME": "<LOADED_LANE_NAME>",
    "MIN_NUM_VEHICLE": 0,
    "MAX_NUM_VEHICLE": 0,
    "LOADING_EFFECT": 0,
    "AUTO_OPTIMIZE_ITEMS": [],
    "properties": {
      "SUB_LOAD_ITEMS": {
        "items": {
          "properties": {
            "VEHICLE_TYPE": "<VEHICLE_TYPE>",
            "VEHICLE_CLASS": "<VEHICLE_CLASS>",
            "SCALE_FACTOR": 0,
            "MIN_NUM_LOADED_LANES": 0,
            "MAX_NUM_LOADED_LANES": 0,
            "SELECTED_LANES": "<SELECTED_LANES>"
          }
        }
      },
      "AUTO_OPTIMIZE_ITEMS": {
        "items": {
          "properties": {
            "VEHICLE_NAME": "<VEHICLE_NAME>"
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "LCNAME": "MV_Case1",
      "DESC": "",
      "OPT_AUTO_OPTIMIZE": false,
      "BRIDGE_TYPE": 2,
      "SCALE_FACTOR_O": [
        1,
        1,
        0.8,
        0.67,
        0.6,
        0.55,
        0.55,
        0.55
      ],
      "SCALE_FACTOR_N": [
        1,
        1,
        0.78,
        0.67,
        0.6,
        0.55,
        0.52,
        0.5
      ],
      "SCALE_FACTOR_JTG": [
        1.2,
        1,
        0.78,
        0.67,
        0.6,
        0.55,
        0.52,
        0.5
      ],
      "LOADING_EFFECT": 1,
      "SUB_LOAD_ITEMS": [
        {
          "VEHICLE_CLASS": "CH(CJJ11)_C-CD(A/B)",
          "VEHICLE_TYPE": "VL",
          "SCALE_FACTOR": 1,
          "MIN_NUM_LOADED_LANES": 1,
          "MAX_NUM_LOADED_LANES": 2,
          "SELECTED_LANES": [
            "LL_01",
            "LL_02"
          ]
        }
      ]
    },
    "2": {
      "LCNAME": "MV_Case2",
      "DESC": "",
      "OPT_AUTO_OPTIMIZE": false,
      "BRIDGE_TYPE": 1,
      "SCALE_FACTOR_O": [
        1,
        1,
        0.8,
        0.67,
        0.6,
        0.55,
        0.55,
        0.55
      ],
      "SCALE_FACTOR_N": [
        1,
        1,
        0.78,
        0.67,
        0.6,
        0.55,
        0.52,
        0.5
      ],
      "SCALE_FACTOR_JTG": [
        1.2,
        1,
        0.78,
        0.67,
        0.6,
        0.55,
        0.52,
        0.5
      ],
      "LOADING_EFFECT": 0,
      "SUB_LOAD_ITEMS": [
        {
          "VEHICLE_CLASS": "CH(CJJ11)_C-CD(A/B)",
          "VEHICLE_TYPE": "VL",
          "SCALE_FACTOR": 1,
          "MIN_NUM_LOADED_LANES": 1,
          "MAX_NUM_LOADED_LANES": 2,
          "SELECTED_LANES": [
            "LL_01",
            "LL_02"
          ]
        }
      ]
    },
    "3": {
      "LCNAME": "MV_Case3",
      "DESC": "",
      "OPT_AUTO_OPTIMIZE": false,
      "BRIDGE_TYPE": 0,
      "SCALE_FACTOR_O": [
        1,
        1,
        0.8,
        0.67,
        0.6,
        0.55,
        0.55,
        0.55
      ],
      "SCALE_FACTOR_N": [
        1,
        1,
        0.78,
        0.67,
        0.6,
        0.55,
        0.52,
        0.5
      ],
      "SCALE_FACTOR_JTG": [
        1.2,
        1,
        0.78,
        0.67,
        0.6,
        0.55,
        0.52,
        0.5
      ],
      "LOADING_EFFECT": 1,
      "SUB_LOAD_ITEMS": [
        {
          "VEHICLE_CLASS": "CH(CJJ11)_C-CD(A/B)",
          "VEHICLE_TYPE": "VL",
          "SCALE_FACTOR": 1,
          "MIN_NUM_LOADED_LANES": 1,
          "MAX_NUM_LOADED_LANES": 2,
          "SELECTED_LANES": [
            "LL_01",
            "LL_02"
          ]
        }
      ]
    },
    "4": {
      "LCNAME": "MV_Case4",
      "DESC": "",
      "OPT_AUTO_OPTIMIZE": true,
      "BRIDGE_TYPE": 2,
      "SCALE_FACTOR_O": [
        1,
        1,
        0.8,
        0.67,
        0.6,
        0.55,
        0.55,
        0.55
      ],
      "SCALE_FACTOR_N": [
        1,
        1,
        0.78,
        0.67,
        0.6,
        0.55,
        0.52,
        0.5
      ],
      "SCALE_FACTOR_JTG": [
        1.2,
        1,
        0.78,
        0.67,
        0.6,
        0.55,
        0.52,
        0.5
      ],
      "MIN_VEHICLE_DIST": 1,
      "LOADED_LANE_NAME": "LL_01",
      "MAX_NUM_VEHICLE": 2,
      "LOADING_EFFECT": 0,
      "AUTO_OPTIMIZE_ITEMS": [
        {
          "VEHICLE_NAME": "CH(CJJ11)_C-CD(A/B)",
          "VEHICLE_TYPE": "VL",
          "SCALE_FACTOR": 1
        },
        {
          "VEHICLE_NAME": "CH(CJJ11)_C-CL(A)",
          "VEHICLE_TYPE": "VL",
          "SCALE_FACTOR": 1
        }
      ]
    }
  }
}
```


---

### Moving Load Cases - India — `/db/MVLDid`

**方法**: POST, GET, PUT, DELETE | **参数**: 15 必填 + 5 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `LCNAME` | 文字（字符串） | **是** | Load Case Name |
| `SCALE_FACTOR` | 数字 | **是** | Scale Factor |
| `NUM_LOADED_LANES` | 整数 | **是** | Number of Loaded Lanes |
| `PERMIT_VEHICLE` | 整数 | **是** | Permit Vehicle ID |
| `REF_LANE` | 整数 | **是** | Reference Lane ID |
| `ECCEN` | 数字 | **是** | Eccentricity |
| `PERMIT_SCALE_FACTOR` | 数字 | **是** | Scale Factor |
| `SUB_LOAD_ITEMS` | Array[Object] | **是** | Sub-Load Cases• Insert the data as an object |
| `MIN_NUM_LOADED_LANES` | 整数 | **是** | Min. Number of Loaded Lanes |
| `MAX_NUM_LOADED_LANES` | 整数 | **是** | Max. Number of Loaded Lanes |
| `VEHICLE_CLASS_1` | 文字（字符串） | **是** | Vehicle Class I |
| `SELECTED_LANES` | 字符串数组 | **是** | Selected Lanes for Carriageway |
| `VEHICLE_CLASS_2` | 文字（字符串） | **是** | Vehicle Class II |
| `Footway` | 文字（字符串） | **是** | Vehicle Footway |
| `SELECTED_FOOTWAY_LANES` | 字符串数组 | **是** | Selected Lanes for Footway |
| `DESC` | 文字（字符串） | 否 | Description |
| `OPT_AUTO_LL` | 是/否（布尔值） | 否 | Auto Live Load Combinations• General Load: false• Auto Live Load Combinations: t |
| `OPT_LC_FOR_PERMIT_LOAD` | 是/否（布尔值） | 否 | Load Cases for Permit Vehicle• General Load: false• Load Cases for Permit Vehicl |
| `CARRIAGE_WAY_WIDTH` | 数字 | 否 | Carriageway Width |
| `CARRIAGE_WAY_LOADING` | 数字 | 否 | Carriageway Loading |

**最简 JSON**：
```json
{
  "MVLDID": {
    "LCNAME": "<LCNAME>",
    "SCALE_FACTOR": 0,
    "NUM_LOADED_LANES": 0,
    "PERMIT_VEHICLE": 0,
    "REF_LANE": 0,
    "ECCEN": 0,
    "PERMIT_SCALE_FACTOR": 0,
    "SUB_LOAD_ITEMS": [],
    "properties": {
      "SUB_LOAD_ITEMS": {
        "items": {
          "properties": {
            "MIN_NUM_LOADED_LANES": 0,
            "MAX_NUM_LOADED_LANES": 0,
            "VEHICLE_CLASS_1": "<VEHICLE_CLASS_1>",
            "SELECTED_LANES": "<SELECTED_LANES>",
            "VEHICLE_CLASS_2": "<VEHICLE_CLASS_2>",
            "SELECTED_FOOTWAY_LANES": "<SELECTED_FOOTWAY_LANES>"
          }
        }
      }
    }
  },
  "Footway": "<Footway>"
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "LCNAME": "MV_Case1",
      "DESC": "",
      "SCALE_FACTOR": [
        1,
        0.9,
        0.8,
        0.8
      ],
      "NUM_LOADED_LANES": 2,
      "SUB_LOAD_ITEMS": [
        {
          "VEHICLE_CLASS_1": "IN(IRC)_(25t1)_BroadGauge-1676mm",
          "SCALE_FACTOR": 1,
          "MIN_NUM_LOADED_LANES": 1,
          "MAX_NUM_LOADED_LANES": 2,
          "SELECTED_LANES": [
            "LL_01",
            "LL_02"
          ]
        }
      ]
    },
    "2": {
      "LCNAME": "MV_Case2",
      "DESC": "",
      "OPT_AUTO_LL": true,
      "SCALE_FACTOR": [
        1,
        0.9,
        0.8,
        0.8
      ],
      "NUM_LOADED_LANES": 2,
      "SUB_LOAD_ITEMS": [
        {
          "VEHICLE_CLASS_1": "IN(IRC6)_ClassA",
          "VEHICLE_CLASS_2": "IN(IRC6)_Class40R",
          "FOOTWAY": "IN(IRC6)_Footway",
          "SCALE_FACTOR": 1,
          "CARRIAGE_WAY_WIDTH": 0,
          "CARRIAGE_WAY_LOADING": 0,
          "SELECTED_LANES": [
            "LL_01",
            "LL_02"
          ],
          "SELECTED_FOOTWAY_LANES": [
            "LL_03"
          ]
        }
      ]
    },
    "3": {
      "LCNAME": "MV_Case3",
      "DESC": "",
      "SCALE_FACTOR": [
        1,
        0.9,
        0.8,
        0.8
      ],
      "OPT_LC_FOR_PERMIT_LOAD": true,
      "PERMIT_VEHICLE": 66,
      "REF_LANE": 1,
      "ECCEN": 1.2,
      "PERMIT_SCALE_FACTOR": 1
    }
  }
}
```


---

### Moving Load Cases - BS — `/db/MVLDbs`

**方法**: POST, GET, PUT, DELETE | **参数**: 19 必填 + 3 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `LCNAME` | 文字（字符串） | **是** | Load Case Name |
| `LOADMODEL` | 文字（字符串） | **是** | Select Load Model• Standard Load (BD 37/01, BS 5400): "STANDER"• Special Load (B |
| `DGNCOMBFACTORTYPE` | 文字（字符串） | **是** | Type of Design Combination Factor• if "bAUTOLIVELOADCOMB": true◦ Ultimate Limit  |
| `COMBMETHOD` | 文字（字符串） | **是** | Combination of Loads• if "bAUTOLIVELOADCOMB": true◦ Combination 1: "COMB_1"◦ Com |
| `LCDATA_STANDARD` | 对象（一组键值对） | **是** | Standard Load |
| `LOADINGEFFECT` | 文字（字符串） | **是** | Loading Effect• "INDEPEND" |
| `SUBLOADDATA` | Array[Object] | **是** | Sub-Load Cases• Insert the data as an object |
| `LCDATA_SPECIAL` | 对象（一组键值对） | **是** | Special Load |
| `VEHICLE_NAME` | 文字（字符串） | **是** | Standard Vehicle |
| `SPECIAL_VIHICLE_NAME` | 文字（字符串） | **是** | Special Vehicle |
| `SELECTEDLANES` | 字符串数组 | **是** | Selected Lanes |
| `STRAD_LANE` | Array[Object] | **是** | HB Straddling Two Lanes• Insert the data as an object |
| `LCDATA_ALLMODE` | 对象（一组键值对） | **是** | CS 454 Assessment |
| `REMAINING_LANE` | 字符串数组 | **是** | Remaining Area• Only for ALL Model 1 |
| `LCDATA_STANDARD_OPTI` | 对象（一组键值对） | **是** | Standard Load for Moving Load Optimization |
| `OPTI_BASE` | 对象（一组键值对） | **是** | Base data |
| `OPTI_VEHICLE_BASE` | Array[Object] | **是** | HB Stradding Two Lanes• Insert the data as an object |
| `LCDATA_SPECIAL_OPTI` | 对象（一组键值对） | **是** | Special Load for Moving Load Optimization |
| `LCDATA_ALLMODE_OPTI` | 对象（一组键值对） | **是** | CS 454 Assessment for Moving Load Optimization |
| `DESC` | 文字（字符串） | 否 | Description |
| `bAUTOOPTIMIZE` | 是/否（布尔值） | 否 | Moving Load Optimization• General Load: false• Moving Load Optimization: true |
| `bAUTOLIVELOADCOMB` | 是/否（布尔值） | 否 | Auto Live Load Combinations |

**最简 JSON**：
```json
{
  "MVLDBS": {
    "LCNAME": "<LCNAME>",
    "LOADMODEL": "<LOADMODEL>",
    "DGNCOMBFACTORTYPE": "<DGNCOMBFACTORTYPE>",
    "COMBMETHOD": "<COMBMETHOD>",
    "LCDATA_STANDARD": {
      "SUBLOADDATA": []
    },
    "LCDATA_STANDARD_OPTI": {
      "OPTI_VEHICLE_BASE": []
    },
    "LCDATA_SPECIAL": {},
    "LCDATA_ALLMODE_OPTI": {},
    "LCDATA_ALLMODE": {},
    "LCDATA_SPECIAL_OPTI": {}
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "LCNAME": "MV_Case1",
      "DESC": "",
      "bAUTOOPTIMIZE": false,
      "LOADMODEL": "STANDER",
      "bAUTOLIVELOADCOMB": true,
      "DGNCOMBFACTORTYPE": "ULTIMATE",
      "COMBMETHOD": "COMB_1",
      "LCDATA_STANDARD": {
        "LOADINGEFFECT": "INDEPEND",
        "SUBLOADDATA": [
          {
            "SCALEFACTOR": 1,
            "NUMLOADEDLANE": 4,
            "VEHICLE_NAME": "BS_(BD21)_HA&HB(Auto)",
            "SELECTEDLANES": [
              "LL_01",
              "LL_02",
              "LL_03",
              "LL_04"
            ],
            "STRAD_LANE": [
              {
                "STARDD_LANE_1": "LL_03",
                "STARDD_LANE_2": "LL_04"
              }
            ]
          }
        ]
      }
    },
    "2": {
      "LCNAME": "MV_Case2",
      "DESC": "",
      "bAUTOOPTIMIZE": false,
      "LOADMODEL": "SPECAIL",
      "bAUTOLIVELOADCOMB": true,
      "DGNCOMBFACTORTYPE": "SERVICEABIL",
      "COMBMETHOD": "COMB_2_3",
      "LCDATA_SPECIAL": {
        "VEHICLE_NAME": "BS_(BD21)_HA",
        "SPECIAL_VIHICLE_NAME": "BS_(CS458)_SOV250_Auto",
        "SELECTEDLANES": [
          "LL_01",
          "LL_02",
          "LL_03",
          "LL_04"
        ],
        "STRAD_LANE": [
          {
            "STARDD_LANE_1": "LL_03",
            "STARDD_LANE_2": "LL_04"
          }
        ]
      }
    },
    "3": {
      "LCNAME": "MV_Case3",
      "DESC": "",
      "bAUTOOPTIMIZE": false,
      "LOADMODEL": "ALL_MODE_1",
      "bAUTOLIVELOADCOMB": true,
      "DGNCOMBFACTORTYPE": "SERVICEABIL",
      "COMBMETHOD": "COMB_2_3",
      "LCDATA_ALLMODE": {
        "VEHICLE_NAME": "BS_(CS454)_A-4AXLE",
        "SPECIAL_VIHICLE_NAME": "BS_(BD37)_HB",
        "SELECTEDLANES": [
          "LL_02",
          "LL_03",
          "LL_04"
        ],
        "STRAD_LANE": [
          {
            "STARDD_LANE_1": "LL_03",
            "STARDD_LANE_2": "LL_04"
          }
        ],
        "REMAINING_LANE": [
          "LL_01"
        ]
      }
    },
    "4": {
      "LCNAME": "MV_Case4",
      "DESC": "",
      "bAUTOOPTIMIZE": false,
      "LOADMODEL": "ALL_MODE_2",
      "bAUTOLIVELOADCOMB": true,
      "DGNCOMBFACTORTYPE": "ULTIMATE",
      "COMBMETHOD": "COMB_1",
      "LCDATA_ALLMODE": {
        "VEHICLE_NAME": "BS_(CS454)_ALLMODEL2(UDL+KEL)",
        "SPECIAL_VIHICLE_NAME": "BS_(BD37)_HB",
        "SELECTEDLANES": [
          "LL_01",
          "LL_02",
          "LL_03",
          "LL_04"
        ],
        "STRAD_LANE": [
          {
            "STARDD_LANE_1": "LL_03",
            "STARDD_LANE_2": "LL_04"
          }
        ]
      }
    },
    "5": {
      "LCNAME": "MV_Case5",
      "DESC": "",
      "bAUTOOPTIMIZE": false,
      "LOADMODEL": "SPECAIL",
      "bAUTOLIVELOADCOMB": false,
      "DGNCOMBFACTORTYPE": "ULTIMATE",
      "COMBMETHOD": "COMB_1",
      "LCDATA_SPECIAL": {
        "VEHICLE_NAME": "BS_(BD21)_HA",
        "SPECIAL_VIHICLE_NAME": "",
        "SELECTEDLANES": [
          "LL_01",
          "LL_02",
          "LL_03",
          "LL_04"
        ],
        "STRAD_LANE": [
          {
            "STARDD_LANE_1": "LL_03",
            "STARDD_LANE_2": "LL_04"
          }
        ]
      }
    },
    "6": {
      "LCNAME": "MV_Case6",
      "DESC": "",
      "bAUTOOPTIMIZE": true,
      "LOADMODEL": "STANDER",
      "bAUTOLIVELOADCOMB": true,
      "DGNCOMBFACTORTYPE": "ULTIMATE",
      "COMBMETHOD": "COMB_1",
      "LCDATA_STANDARD_OPTI": {
        "LOADINGEFFECT": "INDEPEND",
        "OPTI_BASE": {
          "MINVEHLDIST": 1,
          "ASSIGN_LANE": "LL_01",
          "NUMLOADEDLANES": 2
        },
        "OPTI_VEHICLE_BASE": [
          {
            "VEHICLE_TYPE": "VL",
            "VEHICLE_NAME": "BS_(BD21)_HA&HB(Auto)",
            "SCALE_FACTOR": 1
          },
          {
            "VEHICLE_TYPE": "VL",
            "VEHICLE_NAME": "BS_(BD37)_HA&HB(Auto)",
            "SCALE_FACTOR": 1
          }
        ]
      }
    },
    "7": {
      "LCNAME": "MV_Case7",
      "DESC": "",
      "bAUTOOPTIMIZE": true,
      "LOADMODEL": "SPECAIL",
      "bAUTOLIVELOADCOMB": true,
      "DGNCOMBFACTORTYPE": "SERVICEABIL",
      "COMBMETHOD": "COMB_2_3",
      "LCDATA_SPECIAL_OPTI": {
        "VEHICLE_NAME": "BS_(BD21)_HA",
        "SPECIAL_VIHICLE_NAME": "BS_(CS458)_SOV250_Auto",
        "OPTI_BASE": {
          "MINVEHLDIST": 1,
          "ASSIGN_LANE": "LL_01",
          "NUMLOADEDLANES": 2
        }
      }
    },
    "8": {
      "LCNAME": "MV_Case8",
      "DESC": "",
      "bAUTOOPTIMIZE": true,
      "LOADMODEL": "ALL_MODE_1",
      "bAUTOLIVELOADCOMB": true,
      "DGNCOMBFACTORTYPE": "SERVICEABIL",
      "COMBMETHOD": "COMB_2_3",
      "LCDATA_ALLMODE_OPTI": {
        "VEHICLE_NAME": "BS_(CS454)_A-4AXLE",
        "SPECIAL_VIHICLE_NAME": "BS_(BD37)_HB",
        "OPTI_BASE": {
          "MINVEHLDIST": 1,
          "ASSIGN_LANE": "LL_01",
          "NUMLOADEDLANES": 2
        },
        "REMAINING_LANE": [
          "LL_03",
          "LL_04"
        ]
      }
    },
    "9": {
      "LCNAME": "MV_Case9",
      "DESC": "",
      "bAUTOOPTIMIZE": true,
      "LOADMODEL": "ALL_MODE_2",
      "bAUTOLIVELOADCOMB": true,
      "DGNCOMBFACTORTYPE": "ULTIMATE",
      "COMBMETHOD": "COMB_1",
      "LCDATA_ALLMODE_OPTI": {
        "VEHICLE_NAME": "BS_(CS454)_ALLMODEL2(UDL+KEL)",
        "SPECIAL_VIHICLE_NAME": "BS_(BD37)_HB",
        "OPTI_BASE": {
          "MINVEHLDIST": 1,
          "ASSIGN_LANE": "LL_01",
          "NUMLOADEDLANES": 2
        }
      }
    },
    "10": {
      "LCNAME": "MV_Case10",
      "DESC": "",
      "bAUTOOPTIMIZE": true,
      "LOADMODEL": "ALL_MODE_2",
      "bAUTOLIVELOADCOMB": false,
      "DGNCOMBFACTORTYPE": "ULTIMATE",
      "COMBMETHOD": "COMB_1",
      "LCDATA_ALLMODE_OPTI": {
        "VEHICLE_NAME": "BS_(CS454)_ALLMODEL2(UDL+KEL)",
        "SPECIAL_VIHICLE_NAME": "",
        "OPTI_BASE": {
          "MINVEHLDIST": 1,
          "ASSIGN_LANE": "LL_02",
          "NUMLOADEDLANES": 2
        }
      }
    }
  }
}
```


---

### Moving Load Cases - Eurocode — `/db/MVLDeu`

**方法**: POST, GET, PUT, DELETE | **参数**: 31 必填 + 2 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `LCNAME` | 文字（字符串） | **是** | Load Case Name |
| `TYPE_LOADMODEL` | 整数 | **是** | Select Load Model• LM 1, FLM 1 / Footbridge: 1• LM 2,3,4 / FLM 2,3,4 / Footbridg |
| `OPT_COMB` | 文字（字符串） | **是** | Loading Effect• Combined: 0• Independent: 1 |
| `VHLNAME1` | 文字（字符串） | **是** | Load Case - Vehicle |
| `VHLNAME2` | 文字（字符串） | **是** | Load Case - Footway |
| `OPT_LEADING` | 是/否（布尔值） | **是** | Ignore ψ factor |
| `MINVHLDIST` | 数字 | **是** | Min. Vehicle Distance |
| `OPTIMIZE_LANE_NAME` | 文字（字符串） | **是** | Assignement Lane |
| `MIN_NUM_VHL` | 整数 | **是** | Min. Number of Vehicle |
| `MAX_NUM_VHL` | 整数 | **是** | Max. Number of Vehicle |
| `LOADEDLANE` | 整数 | **是** | Number of Loaded Lane |
| `SCALE_FACTOR1` | 数字 | **是** | ψ1 factor for Lane 1 |
| `SCALE_FACTOR2` | 数字 | **是** | ψ1 factor for Lane 2 |
| `SCALE_FACTOR3` | 数字 | **是** | ψ1 factor for Lane 3 or More |
| `OPT_PSI_FACTOR` | 是/否（布尔值） | **是** | Ignore ψ1 factor |
| `MULTI_FACTOR1` | 数字 | **是** | Multi Presence Factor for Lane 1 |
| `MULTI_FACTOR2` | 数字 | **是** | Multi Presence Factor for Lane 2 |
| `MULTI_FACTOR3` | 数字 | **是** | Multi Presence Factor for Lane 3 or More |
| `OPTIMIZE_LIST` | Array[Object] | **是** | Sub-Load Cases• Insert the data as an object |
| `SUB_LOAD_LIST` | Array[Object] | **是** | Sub-Load Cases• Insert the data as an object |
| `SLN_LIST` | 字符串数组 | **是** | Selected Lanes |
| `SRA_LIST` | 字符串数组 | **是** | Remaining Area |
| `FLN_LIST` | 字符串数组 | **是** | Footway Lanes• For LM 1, FLM 1 / Footbridge |
| `STL_LIST` | Array[Object] | **是** | Straddling Lanes• For LM 1 & 3 Multi (Straddling)• Insert the data as an object |
| `NAME1` | 文字（字符串） | **是** | Start Lane Name |
| `NAME2` | 文字（字符串） | **是** | End Lane Name |
| `TYPE` | 整数 | **是** | Vehicle Load Type¹⁾ |
| `NAME` | 文字（字符串） | **是** | Vehicle Load Name |
| `SCALE_FACTOR` | 数字 | **是** | Scale Factor |
| `MIN_LOAD_LANE_TYPE` | 整数 | **是** | Min. Number of Loaded Lanes |
| `MAX_LOAD_LANE_TYPE` | 整数 | **是** | Max. Number of Loaded Lanes |
| `OPT_AUTO_OPTIMIZE` | 是/否（布尔值） | 否 | Moving Load Optimization• General Load: false• Moving Load Optimization: true |
| `DESC` | 文字（字符串） | 否 | Description |

**最简 JSON**：
```json
{
  "MVLDEU": {
    "LCNAME": "<LCNAME>",
    "TYPE_LOADMODEL": 0,
    "OPT_COMB": "<OPT_COMB>",
    "VHLNAME1": "<VHLNAME1>",
    "VHLNAME2": "<VHLNAME2>",
    "OPT_LEADING": true,
    "MINVHLDIST": 0,
    "OPTIMIZE_LANE_NAME": "<OPTIMIZE_LANE_NAME>",
    "MIN_NUM_VHL": 0,
    "MAX_NUM_VHL": 0,
    "LOADEDLANE": 0,
    "SCALE_FACTOR1": 0,
    "SCALE_FACTOR2": 0,
    "SCALE_FACTOR3": 0,
    "OPT_PSI_FACTOR": true,
    "MULTI_FACTOR1": 0,
    "MULTI_FACTOR2": 0,
    "MULTI_FACTOR3": 0,
    "OPTIMIZE_LIST": [],
    "SUB_LOAD_LIST": [],
    "SLN_LIST": "<SLN_LIST>",
    "SRA_LIST": "<SRA_LIST>",
    "FLN_LIST": "<FLN_LIST>",
    "STL_LIST": [],
    "properties": {
      "STL_LIST": {
        "items": {
          "properties": {
            "NAME1": "<NAME1>",
            "NAME2": "<NAME2>"
          }
        }
      },
      "OPTIMIZE_LIST": {
        "items": {
          "properties": {
            "TYPE": 0,
            "NAME": "<NAME>",
            "SCALE_FACTOR": 0
          }
        }
      },
      "SUB_LOAD_LIST": {
        "items": {
          "properties": {
            "MIN_LOAD_LANE_TYPE": 0,
            "MAX_LOAD_LANE_TYPE": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "LCNAME": "MV_Case1",
      "OPT_AUTO_OPTIMIZE": false,
      "TYPE_LOADMODEL": 1,
      "DESC": "",
      "VHLNAME1": "EU_(R)_LoadModel1",
      "VHLNAME2": "EU_(FF)_Uniformload(Road)",
      "OPT_LEADING": false,
      "SLN_LIST": [
        "LL_01",
        "LL_02"
      ],
      "SRA_LIST": [
        "LL_04"
      ],
      "FLN_LIST": [
        "LL_03"
      ]
    },
    "2": {
      "LCNAME": "MV_Case2",
      "OPT_AUTO_OPTIMIZE": false,
      "TYPE_LOADMODEL": 2,
      "DESC": "",
      "OPT_COMB": 1,
      "OPT_LEADING": true,
      "SUB_LOAD_LIST": [
        {
          "TYPE": 2,
          "NAME": "EU_(FF)_ConcentratedLoad",
          "SCALE_FACTOR": 1,
          "MIN_LOAD_LANE_TYPE": 1,
          "MAX_LOAD_LANE_TYPE": 4,
          "SLN_LIST": [
            "LL_01",
            "LL_02",
            "LL_03",
            "LL_04"
          ]
        }
      ]
    },
    "3": {
      "LCNAME": "MV_Case3",
      "OPT_AUTO_OPTIMIZE": false,
      "TYPE_LOADMODEL": 3,
      "DESC": "",
      "VHLNAME1": "EU_(R)_LoadModel1",
      "VHLNAME2": "UD_LoadModel3",
      "OPT_LEADING": false,
      "SLN_LIST": [
        "LL_01",
        "LL_02"
      ],
      "SRA_LIST": [
        "LL_04"
      ]
    },
    "4": {
      "LCNAME": "MV_Case4",
      "OPT_AUTO_OPTIMIZE": false,
      "TYPE_LOADMODEL": 4,
      "DESC": "",
      "VHLNAME1": "EU_(R)_LoadModel1",
      "VHLNAME2": "EU_(R)_LoadModel3(UKNA)_SOV250_Auto",
      "OPT_LEADING": false,
      "SLN_LIST": [
        "LL_01",
        "LL_03",
        "LL_04"
      ],
      "SRA_LIST": [
        "LL_02"
      ],
      "STL_LIST": [
        {
          "NAME1": "LL_03",
          "NAME2": "LL_04"
        }
      ]
    },
    "5": {
      "LCNAME": "MV_Case5",
      "OPT_AUTO_OPTIMIZE": false,
      "TYPE_LOADMODEL": 5,
      "DESC": "",
      "OPT_COMB": 1,
      "SCALE_FACTOR1": 0.8,
      "SCALE_FACTOR2": 0.7,
      "SCALE_FACTOR3": 0.6,
      "OPT_PSI_FACTOR": false,
      "MULTI_FACTOR1": 1,
      "MULTI_FACTOR2": 1,
      "MULTI_FACTOR3": 0.75,
      "SUB_LOAD_LIST": [
        {
          "TYPE": 2,
          "NAME": "EU_(RFL)_HSLMB",
          "SCALE_FACTOR": 1,
          "MIN_LOAD_LANE_TYPE": 1,
          "MAX_LOAD_LANE_TYPE": 4,
          "SLN_LIST": [
            "LL_01",
            "LL_02",
            "LL_03",
            "LL_04"
          ]
        }
      ]
    },
    "6": {
      "LCNAME": "MV_Case6",
      "OPT_AUTO_OPTIMIZE": true,
      "TYPE_LOADMODEL": 1,
      "DESC": "",
      "VHLNAME1": "EU_(R)_LoadModel1",
      "VHLNAME2": "EU_(FF)_Uniformload(Road)",
      "OPT_LEADING": false,
      "MINVHLDIST": 1,
      "OPTIMIZE_LANE_NAME": "LL_01",
      "LOADEDLANE": 3,
      "SLN_LIST": [
        "LL_01",
        "LL_03",
        "LL_04"
      ]
    },
    "7": {
      "LCNAME": "MV_Case7",
      "OPT_AUTO_OPTIMIZE": true,
      "TYPE_LOADMODEL": 2,
      "DESC": "",
      "OPT_COMB": 1,
      "OPT_LEADING": false,
      "MINVHLDIST": 1,
      "OPTIMIZE_LANE_NAME": "LL_01",
      "MIN_NUM_VHL": 1,
      "MAX_NUM_VHL": 2,
      "OPTIMIZE_LIST": [
        {
          "TYPE": 2,
          "NAME": "EU_(FF)_ConcentratedLoad",
          "SCALE_FACTOR": 1
        },
        {
          "TYPE": 2,
          "NAME": "EU_(FF)_Uniformload(Footbridge)",
          "SCALE_FACTOR": 1
        }
      ]
    },
    "8": {
      "LCNAME": "MV_Case8",
      "OPT_AUTO_OPTIMIZE": true,
      "TYPE_LOADMODEL": 3,
      "DESC": "",
      "VHLNAME1": "EU_(R)_LoadModel1",
      "VHLNAME2": "EU_(R)_LoadModel3_Auto",
      "OPT_LEADING": true,
      "MINVHLDIST": 1,
      "OPTIMIZE_LANE_NAME": "LL_01",
      "LOADEDLANE": 3,
      "SLN_LIST": [
        "LL_01",
        "LL_03",
        "LL_04"
      ]
    },
    "9": {
      "LCNAME": "MV_Case9",
      "OPT_AUTO_OPTIMIZE": true,
      "TYPE_LOADMODEL": 4,
      "DESC": "",
      "VHLNAME1": "EU_(R)_LoadModel1",
      "VHLNAME2": "EU_(R)_LoadModel3(UKNA)_SOV250_Auto",
      "OPT_LEADING": true,
      "MINVHLDIST": 1,
      "OPTIMIZE_LANE_NAME": "LL_02",
      "LOADEDLANE": 3,
      "SLN_LIST": [
        "LL_01",
        "LL_03",
        "LL_04"
      ],
      "STL_LIST": [
        {
          "NAME1": "LL_03",
          "NAME2": "LL_04"
        },
        {
          "NAME1": "LL_03",
          "NAME2": "LL_04"
        },
        {
          "NAME1": "LL_03",
          "NAME2": "LL_04"
        },
        {
          "NAME1": "LL_03",
          "NAME2": "LL_04"
        },
        {
          "NAME1": "LL_03",
          "NAME2": "LL_04"
        },
        {
          "NAME1": "LL_03",
          "NAME2": "LL_04"
        }
      ]
    },
    "10": {
      "LCNAME": "MV_Case10",
      "OPT_AUTO_OPTIMIZE": true,
      "TYPE_LOADMODEL": 5,
      "DESC": "",
      "OPT_COMB": 1,
      "MINVHLDIST": 1,
      "OPTIMIZE_LANE_NAME": "LL_01",
      "MIN_NUM_VHL": 1,
      "MAX_NUM_VHL": 2,
      "SCALE_FACTOR1": 0.8,
      "SCALE_FACTOR2": 0.7,
      "SCALE_FACTOR3": 0.6,
      "OPT_PSI_FACTOR": false,
      "MULTI_FACTOR1": 1,
      "MULTI_FACTOR2": 1,
      "MULTI_FACTOR3": 0.75,
      "OPTIMIZE_LIST": [
        {
          "TYPE": 2,
          "NAME": "EU_(FF)_ConcentratedLoad",
          "SCALE_FACTOR": 1
        },
        {
          "TYPE": 2,
          "NAME": "EU_(FF)_Uniformload(Footbridge)",
          "SCALE_FACTOR": 1
        }
      ]
    }
  }
}
```


---

### Moving Load Cases - Poland — `/db/MVLDpl`

**方法**: POST, GET, PUT, DELETE | **参数**: 17 必填 + 3 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `LCNAME` | 文字（字符串） | **是** | Load Case Name |
| `LOAD_MODEL` | 整数 | **是** | Select Load Model• Vehicle S/ Vehicle 2S Type: 1• Vehicle K Type: 2• Military Lo |
| `AUTO_OPTIMIZE` | 对象（一组键值对） | **是** | Sub-Load Cases |
| `VEHICLE_LOAD_NAME` | 文字（字符串） | **是** | Vehicle Name |
| `LANE_NAME` | 文字（字符串） | **是** | Loaded Lane |
| `MIN_VEHL_DIST` | 数字 | **是** | Min. Vehicle Distance |
| `MIN_NUM_VEHICLE` | 整数 | **是** | Min. Number of Vehicle |
| `MAX_NUM_VEHICLE` | 整数 | **是** | Max. Number of Vehicle |
| `NUM_LOADED_LANES` | 整数 | **是** | Number of Loaded Lanes |
| `COMB_OPTION` | 文字（字符串） | **是** | Loading Effect• Combined: "COMBINED"• Independent: "INDEPENDENT" |
| `OPTIMIZE_ITEMS` | Array[Object] | **是** | Sub-Load Cases• Insert the data as an object |
| `PERMIT_LOAD` | 对象（一组键值对） | **是** | Permit Vehicle |
| `REF_LANE` | 文字（字符串） | **是** | Reference Lane |
| `ECC` | 数字 | **是** | Eccentricity |
| `SCALE_FACTOR` | 数字 | **是** | Scale Factor |
| `DEFAULT` | 对象（一组键值对） | **是** | Sub-Load Cases |
| `SUB_LOAD_DATAS` | Array[Object] | **是** | Sub-Load Cases• Insert the data as an object |
| `DESC` | 文字（字符串） | 否 | Description |
| `bAUTO_OPTIMIZE` | 是/否（布尔值） | 否 | Moving Load Optimization• General Load: false• Moving Load Optimization: true |
| `bPERMIT_LOAD` | 是/否（布尔值） | 否 | Load Case for Permit Vehicle• General Load: false• Permit Vehicle: true |

**最简 JSON**：
```json
{
  "MVLDPL": {
    "LCNAME": "<LCNAME>",
    "LOAD_MODEL": 0,
    "AUTO_OPTIMIZE": {
      "LANE_NAME": "<LANE_NAME>",
      "MIN_VEHL_DIST": 0,
      "MIN_NUM_VEHICLE": 0,
      "MAX_NUM_VEHICLE": 0,
      "NUM_LOADED_LANES": 0,
      "OPTIMIZE_ITEMS": []
    },
    "DEFAULT": {
      "SUB_LOAD_DATAS": []
    },
    "PERMIT_LOAD": {
      "REF_LANE": "<REF_LANE>",
      "ECC": 0,
      "SCALE_FACTOR": 0
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "LCNAME": "MV1",
      "DESC": "",
      "LOAD_MODEL": 1,
      "bAUTO_OPTIMIZE": false,
      "bPERMIT_LOAD": false,
      "DEFAULT": {
        "COMB_OPTION": "INDEPENDENT",
        "SUB_LOAD_DATAS": [
          {
            "VEHICLE_NAME": "Sidewalks,stairsandwalkways",
            "SCALE_FACTOR": 1,
            "MIN_LOADED_LANE": 1,
            "MAX_LOADED_LANE": 2,
            "LANE_NAMES": [
              "L1",
              "L2"
            ]
          }
        ]
      }
    },
    "2": {
      "LCNAME": "MV2",
      "DESC": "",
      "LOAD_MODEL": 2,
      "bAUTO_OPTIMIZE": false,
      "bPERMIT_LOAD": false,
      "DEFAULT": {
        "COMB_OPTION": "INDEPENDENT",
        "VEHICLE_LOAD_NAME": "VehicleK",
        "SUB_LOAD_DATAS": [
          {
            "LANE_NAMES": [
              "L1",
              "L2"
            ]
          }
        ]
      }
    },
    "3": {
      "LCNAME": "MV3",
      "DESC": "",
      "LOAD_MODEL": 3,
      "bAUTO_OPTIMIZE": false,
      "bPERMIT_LOAD": false,
      "DEFAULT": {
        "COMB_OPTION": "INDEPENDENT",
        "VEHICLE_LOAD_NAME": "TrackedVehicle",
        "SUB_LOAD_DATAS": [
          {
            "LANE_NAMES": [
              "L1",
              "L2"
            ]
          }
        ]
      }
    }
  }
}
```


---

### Moving Load Cases - Transverse — `/db/MVLDtr`

**方法**: POST, GET, PUT, DELETE | **参数**: 6 必填 + 1 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `LCNAME` | 文字（字符串） | **是** | Load Case Name |
| `MVHL_NAME` | 文字（字符串） | **是** | Vehicle Name |
| `SCALEFACTOR` | 数字 | **是** | Scale Factor |
| `LLAN_NAME` | 文字（字符串） | **是** | Line Lane |
| `NUM_LANE` | 整数 | **是** | Number of Loaded Lanes |
| `ITEMS` | 数字数组 | **是** | Factors• Length: NUM_LANE + 1 |
| `DESC` | 文字（字符串） | 否 | Description |

**最简 JSON**：
```json
{
  "MVLDTR": {
    "LCNAME": "<LCNAME>",
    "MVHL_NAME": "<MVHL_NAME>",
    "SCALEFACTOR": 0,
    "LLAN_NAME": "<LLAN_NAME>",
    "NUM_LANE": 0,
    "ITEMS": 0
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "LCNAME": "MV_Case1",
      "DESC": "",
      "MVHL_NAME": "Trans",
      "SCALEFACTOR": 1,
      "LLAN_NAME": "LL_01",
      "NUM_LANE": 3,
      "ITEMS": [
        1,
        1,
        0.9,
        0.75
      ]
    }
  }
}
```


---

### Concurrent Reaction Group — `/db/CRGR`

**方法**: POST, GET, PUT, DELETE | **参数**: 1 必填 + 0 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `GROUPS` | 字符串数组 | **是** | Structure Group Names |

**最简 JSON**：
```json
{
  "CRGR": {
    "GROUPS": "<GROUPS>"
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "GROUPS": [
        "Main3",
        "Main4",
        "Main5"
      ]
    }
  }
}
```


---

### Concurrent Joint Force Group — `/db/CJFG`

**方法**: POST, GET, PUT, DELETE | **参数**: 1 必填 + 0 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `GROUPS` | 字符串数组 | **是** | Structure Group Names |

**最简 JSON**：
```json
{
  "CJFG": {
    "GROUPS": "<GROUPS>"
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "GROUPS": [
        "Main1",
        "Main2",
        "Main3",
        "Main4"
      ]
    }
  }
}
```


---

### Vehicle Classes — `/db/MVHC`

**方法**: POST, GET, PUT, DELETE | **参数**: 2 必填 + 0 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `VEHICLE_CLS_NAME` | 文字（字符串） | **是** | Vehicle Class Name |
| `VEHICLE_LD_NAMES` | 字符串数组 | **是** | Selected Vehicle List |

**最简 JSON**：
```json
{
  "MVHC": {
    "VEHICLE_CLS_NAME": "<VEHICLE_CLS_NAME>",
    "VEHICLE_LD_NAMES": "<VEHICLE_LD_NAMES>"
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "VEHICLE_CLS_NAME": "VCN1",
      "VEHICLE_LD_NAMES": [
        "DB-18"
      ]
    }
  }
}
```


---

### Plate Element for Influence Surface — `/db/SINF`

**方法**: POST, GET, PUT, DELETE | **参数**: 1 必填 + 0 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `ELEM_LISTS` | 整数数组 | **是** | Assigned Element List |

**最简 JSON**：
```json
{
  "SINF": {
    "ELEM_LISTS": 0
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "ELEM_LISTS": [
        438,
        439,
        444,
        462,
        463
      ]
    }
  }
}
```


---

### Lane Support - Negative Moments at Interior Piers — `/db/MLSP`

**方法**: POST, GET, PUT, DELETE | **参数**: 5 必填 + 0 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TYPE` | 文字（字符串） | **是** | Input Type• Auto: "Auto Input"◦ Only for AASHTO LRFD |
| `ELEMENT_NO` | 整数 | **是** | Element ID |
| `ELEMENT_TYPE` | 文字（字符串） | **是** | Element Type• Beam: "BEAM"• Plate: "PLATE" |
| `POSITION` | 文字（字符串） | **是** | Support Position• Only for "BEAM"◦ Both: "Both"◦ End-i: "End-I"◦ End-j: "End-J" |
| `GROUP_NAME` | 文字（字符串） | **是** | Structure Group Name• Only for "Auto Input" |

**最简 JSON**：
```json
{
  "MLSP": {
    "TYPE": "<TYPE>",
    "ELEMENT_NO": 0,
    "ELEMENT_TYPE": "<ELEMENT_TYPE>",
    "POSITION": "<POSITION>",
    "GROUP_NAME": "<GROUP_NAME>"
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "TYPE": "AutoInput",
      "GROUP_NAME": "CrossBeam"
    }
  }
}
```


---

### Lane Support - Reactions at Interior Piers — `/db/MLSR`

**方法**: POST, GET, PUT, DELETE | **参数**: 1 必填 + 0 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NODE` | 整数 | **是** | Fixed Value: 0 |

**最简 JSON**：
```json
{
  "MLSR": {
    "NODE": 0
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "60": {
      "NODE": 0
    },
    "201": {
      "NODE": 0
    },
    "202": {
      "NODE": 0
    },
    "203": {
      "NODE": 0
    }
  }
}
```


---

### Dynamic Load Allowance — `/db/DYLA`

**方法**: POST, GET, PUT, DELETE | **参数**: 2 必填 + 0 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `FACTOR` | 数字 | **是** | Impact Factor (%) |
| `ITEMS` | 字符串数组 | **是** | Selected Structure Group List |

**最简 JSON**：
```json
{
  "DYLA": {
    "FACTOR": 0,
    "ITEMS": "<ITEMS>"
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "FACTOR": 15,
      "ITEMS": [
        "Main4",
        "Main5",
        "Main6"
      ]
    },
    "2": {
      "FACTOR": 10,
      "ITEMS": [
        "Main1",
        "Main2",
        "Main7"
      ]
    }
  }
}
```


---

### Additional Impact Factor — `/db/IMPF`

**方法**: POST, GET, PUT, DELETE | **参数**: 9 必填 + 1 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `ITEM` | Array[Object] | **是** | Additional Impact Factor• Insert the data as an object |
| `ID` | 整数 | **是** | Serial Number |
| `LANE_TYPE` | 文字（字符串） | **是** | Lane Type• Line Lane: "LINE" |
| `LANE_NAME` | 文字（字符串） | **是** | Lane Name |
| `FACT_TYPE` | 文字（字符串） | **是** | Factor Type• Effective Span Length: "EFF_SPAN_LEN_AUTO" |
| `FACTOR` | 数字 | **是** | Factor• Impact Factor: greater than 0 and less than or equal to 0.3• Effective S |
| `ELEMTYPE` | 文字（字符串） | **是** | Element Type• Beam: "BEAM"• Truss: "TRUSS"• Plate: "PLATE" |
| `PARTS` | 布尔数组 | **是** | Parts• Beam: [i, 1/4, 1/2, 3/4, j]• Plate: [cent, i, j, k, l] |
| `COMPONENTS` | 布尔数组 | **是** | Components• Beam: [My_max, My_min, Mz_max, Mz_min, Fx_max, Fx_min]• Truss: [Max, |
| `ITEMS` | Array | 否 | Items |

**最简 JSON**：
```json
{
  "ITEM": [],
  "IMPF": {
    "properties": {
      "ITEMS": {
        "items": {
          "properties": {
            "ID": 0,
            "LANE_TYPE": "<LANE_TYPE>",
            "LANE_NAME": "<LANE_NAME>",
            "FACT_TYPE": "<FACT_TYPE>",
            "FACTOR": 0,
            "ELEMTYPE": "<ELEMTYPE>",
            "PARTS": true,
            "COMPONENTS": true
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "82": {
      "ITEMS": [
        {
          "ID": 1,
          "LANE_TYPE": "LINE",
          "LANE_NAME": "LL_01",
          "FACT_TYPE": "IMPACT_FACT",
          "FACTOR": 0.3
        },
        {
          "ID": 2,
          "LANE_TYPE": "LINE",
          "LANE_NAME": "LL_02",
          "FACT_TYPE": "IMPACT_FACT",
          "FACTOR": 0.3
        }
      ]
    }
  }
}
```


---

### Railway Dynamic Factor — `/db/DYFG`

**方法**: POST, GET, PUT, DELETE | **参数**: 5 必填 + 1 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `INPUT_TYPE` | 整数 | **是** | Input Type• Auto Input: 0• User Input: 1 |
| `LENGTH` | 数字 | **是** | Determinant Length (Lφ) |
| `MAINTAIN_TYPE` | 整数 | **是** | Quality of Track Maintenance• Carefully maintained: 0• Standard maintenance: 1 |
| `HEIGHT_COVER` | 数字 | **是** | Height of Cover (h)• if "OPT_REDUCE_EFF": true |
| `DYN_FACTOR` | 数字 | **是** | Dynamic Factor (φ)• if "INPUT_TYPE": 1 |
| `OPT_REDUCE_EFF` | 是/否（布尔值） | 否 | Consider Reduced Dynamic Effect |

**最简 JSON**：
```json
{
  "DYFG": {
    "INPUT_TYPE": 0,
    "LENGTH": 0,
    "MAINTAIN_TYPE": 0,
    "HEIGHT_COVER": 0,
    "DYN_FACTOR": 0
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "INPUT_TYPE": 0,
      "LENGTH": 12,
      "MAINTAIN_TYPE": 0,
      "OPT_REDUCE_EFF": true,
      "HEIGHT_COVER": 1
    }
  }
}
```


---

### Railway Dynamic Factor by Element — `/db/DYNF`

**方法**: POST, GET, PUT, DELETE | **参数**: 5 必填 + 1 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `INPUT_TYPE` | 整数 | **是** | Input Type• Auto Input: 0• User Input: 1 |
| `LENGTH` | 数字 | **是** | Determinant Length (Lφ) |
| `MAINTAIN_TYPE` | 整数 | **是** | Quality of Track Maintenance• Carefully maintained: 0• Standard maintenance: 1 |
| `HEIGHT_COVER` | 数字 | **是** | Height of Cover (h)• if "OPT_REDUCE_EFF": true |
| `DYN_FACTOR` | 数字 | **是** | Dynamic Factor (φ)• if "INPUT_TYPE": 1 |
| `OPT_REDUCE_EFF` | 是/否（布尔值） | 否 | Consider Reduced Dynamic Effect |

**最简 JSON**：
```json
{
  "DYNF": {
    "INPUT_TYPE": 0,
    "LENGTH": 0,
    "MAINTAIN_TYPE": 0,
    "HEIGHT_COVER": 0,
    "DYN_FACTOR": 0
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "249": {
      "INPUT_TYPE": 0,
      "LENGTH": 12,
      "MAINTAIN_TYPE": 1,
      "OPT_REDUCE_EFF": true,
      "HEIGHT_COVER": 1
    }
  }
}
```


---

## Response Spectrum Functions - User Type — `/db/SPFC`

**HTTP 方法**: POST, GET, PUT, DELETE | **参数总数**: 120（7 必填 + 113 可选）

### 1. 这是什么？（工程含义）

**Response Spectrum Functions - User Type** — 这是模型数据库的创建和查询操作，属于 Dynamic Loads 类别。

RS Function Name

> 简单说：这个接口用来**Response Spectrum Functions - User Type**。

### 2. JSON 结构（逐层解释）

下面按照从外到内的顺序解释每一层的 JSON 结构：

```json
{
  "SPFC": {
    "NAME": "<NAME>",
    "iTYPE": 0,
    "iMETHOD (可选)": "0",
    "DRATIO (可选)": "0.05",
    "DESC (可选)": "Blank",
    "RMF (可选)": 0,
    "STR (可选)": {},
    "OPT (可选)": {},
    "VAL (可选)": {},
    "SCALE": 0,
    "GRAV": 0,
    "STR": {
      "SPEC_CODE (可选)": "<SPEC_CODE>",
      "EQ_ (可选)": "<EQ_>",
      "DIV (可选)": "<DIV>",
      "BT (可选)": "<BT>",
      "ZM (可选)": "<ZM>",
      "ST (可选)": "<ST>",
      "SI (可选)": "<SI>",
      "SPECTYPE (可选)": "<SPECTYPE>",
      "GROUTYPE (可选)": "<GROUTYPE>",
      "PARATYPE (可选)": "<PARATYPE>",
      "RESIONTYPE (可选)": "<RESIONTYPE>",
      "NATIONALANNEX (可选)": "<NATIONALANNEX>",
      "REGION (可选)": "<REGION>",
      "METHOD (可选)": "<METHOD>"
    },
    "OPT": {
      "SFI (可选)": 0,
      "SC_ (可选)": 0,
      "NSC (可选)": 0,
      "nLForce (可选)": 0,
      "LARGEBRIDEGE (可选)": false,
      "bVACC (可选)": false,
      "iVACC (可选)": 0,
      "bE2_005 (可选)": false,
      "SCCOPT (可选)": 0,
      "iSPTYPE (可选)": 0,
      "iSEISZONEFACTOR (可选)": 0,
      "iSEISSOURCETYPE (可选)": 0,
      "SOILCLASS (可选)": 0,
      "KD (可选)": 0,
      "KR (可选)": 0,
      "ZA (可选)": 0,
      "ZV (可选)": 0,
      "iSEISZONE (可选)": 0,
      "iEQMETHOD (可选)": 0,
      "bRELIEVE (可选)": false,
      "iSPECTYPE (可选)": 0,
      "iSPECUSE (可选)": 0,
      "iSUBZONE (可选)": 0,
      "iGROUTYPE (可选)": 0,
      "IMPORTANT_BRIDGE (可选)": false,
      "RESION_SEISMICITY (可选)": 0,
      "SOIL_CATEGORY (可选)": 0,
      "BYCODE (可选)": false,
      "RISK_CATEGORY (可选)": 0
    },
    "VAL": {
      "aTG (可选)": [],
      "aIF (可选)": [],
      "aSRA (可选)": [],
      "aSRA_T (可选)": [],
      "aNSF (可选)": [],
      "aSC (可选)": [],
      "aMSRACC (可选)": [],
      "aSMF (可选)": [],
      "aSCP (可选)": [],
      "aEP (可选)": [],
      "DP (可选)": 0,
      "MaxEQ (可选)": 0,
      "G (可选)": 0,
      "EPA (可选)": 0,
      "SMAX (可选)": 0,
      "DP2 (可选)": 0,
      "ETA1 (可选)": 0,
      "ETA2 (可选)": 0,
      "GAMMA (可选)": 0,
      "A (可选)": 0,
      "SOILFACTOR (可选)": 0,
      "TB (可选)": 0,
      "TC (可选)": 0,
      "TD (可选)": 0,
      "AGR (可选)": 0,
      "I_ (可选)": 0,
      "XI (可选)": 0,
      "Q (可选)": 0,
      "B (可选)": 0,
      "TS (可选)": 0,
      "SPTYPE (可选)": 0,
      "IE (可选)": 0,
      "R_ (可选)": 0,
      "CDISTANCE (可选)": 0,
      "Q0 (可选)": 0,
      "KW (可选)": 0,
      "ALPHA (可选)": 0,
      "CO (可选)": 0,
      "KH (可选)": 0,
      "CZ (可选)": 0,
      "V (可选)": 0,
      "AG (可选)": 0,
      "DPFAC (可选)": 0,
      "IF (可选)": 0,
      "SMFACTOR (可选)": 0,
      "RMFACTOR (可选)": 0,
      "ZONEFACTOR (可选)": 0,
      "TL (可选)": 0,
      "PGA (可选)": 0,
      "PHI (可选)": 0,
      "DEPTH (可选)": 0,
      "FO (可选)": 0,
      "TCSTAR (可选)": 0,
      "KP (可选)": 0,
      "Z (可选)": 0,
      "MU (可选)": 0,
      "USERDEFSEISZONE (可选)": 0,
      "FUNDAMENTAL_PERIOD (可选)": 0,
      "K1 (可选)": 0,
      "K2 (可选)": 0,
      "K3 (可选)": 0,
      "K4 (可选)": 0,
      "KPSI (可选)": 0,
      "PERIOD": 0
    },
    "aFUNC": [],
    "properties": {
      "aFUNC": {
        "items": {
          "properties": {
            "VALUE": 0
          }
        }
      }
    }
  }
}
```

**第 1 层：`SPFC`** — 12 个参数在这一层

- `"NAME"`: 文字（字符串） — RS Function Name
- `"iTYPE"`: 整数 — Spectral Data Type• Normalized Accel.: 1• Acceleration: 2• Velocity: 3• Displacement: 4
- `"iMETHOD"`: 整数 — Scaling Method• Scale Factor: 0• Maximum Value: 1
- `"SCALE"`: 数字 — Scaling Value
- `"GRAV"`: 数字 — Gravity• Only for Normalized Accel.
- `"DRATIO"`: 数字 — Damping Ratio
- `"DESC"`: 文字（字符串） — Description
- `"RMF"`: 数字 — ResponseModificationFactor
- ... *还有 4 个参数*

**第 2 层：`SPFC.OPT`** — 29 个参数在这一层

- `"SFI"`: 整数 — SeismicFortificationIntensity
- `"SC_"`: 整数 — SiteClass
- `"NSC"`: 整数 — SeismicDesignCategory
- `"nLForce"`: 整数 — nLForce
- `"LARGEBRIDEGE"`: 是/否（布尔值） — LargeBridege
- `"bVACC"`: 是/否（布尔值） — VerticalAccelerationSpec
- `"iVACC"`: 整数 — VerticalAccelerationSpecType
- `"bE2_005"`: 是/否（布尔值） — ThinkE20.05
- ... *还有 21 个参数*

**第 3 层：`SPFC.STR`** — 14 个参数在这一层

- `"SPEC_CODE"`: 文字（字符串） — DesignSpectrumType
- `"EQ_"`: 文字（字符串） — EarthResponse
- `"DIV"`: 文字（字符串） — Division
- `"BT"`: 文字（字符串） — BridgeType
- `"ZM"`: 文字（字符串） — ZoningMap
- `"ST"`: 文字（字符串） — SiteType
- `"SI"`: 文字（字符串） — SeismicIntensity
- `"SPECTYPE"`: 文字（字符串） — SpectrumType
- ... *还有 6 个参数*

**第 4 层：`SPFC.VAL`** — 64 个参数在这一层

- `"aTG"`: Array — DesignCharacteristicPeriodofGroundMotion(TG,TG1,TG2)
- `"aIF"`: Array — ImportanceFactor(Ci,Cs,Cd)
- `"aSRA"`: Array — SpectralResponseAcceleration(Sds,Sd1,Sms,Sm1)
- `"aSRA_T"`: Array — SpectralResponseAcceleration(Sds_t,Sd1_t,Sms_t,Sm1_t)
- `"aNSF"`: Array — NearSourceFactor(Nda,Ndv,Nma,Nmv)
- `"aSC"`: Array — SeismicCoefficient(Ca,Cv)
- `"aMSRACC"`: Array — MappedSpectralResponseAccelerationatShortPeriods(Ss,S1)
- `"aSMF"`: Array — SiteMagnifyFactor(Fda,Fdv,Fma,Fmv)
- ... *还有 56 个参数*

**第 5 层：`SPFC.properties.aFUNC.items.properties`** — 1 个参数在这一层

- `"VALUE"`: 数字 — Value• Depend on Spectral Data Type


### 3. 必填 vs 可选参数

**必填参数**（不填会报错）：

| 参数名 | 类型 | JSON 路径 | 说明 |
|--------|------|-----------|------|
| `NAME` | 文字（字符串） | `SPFC.NAME` | RS Function Name |
| `iTYPE` | 整数 | `SPFC.iTYPE` | Spectral Data Type• Normalized Accel.: 1• Acceleration: 2• V |
| `SCALE` | 数字 | `SPFC.SCALE` | Scaling Value |
| `GRAV` | 数字 | `SPFC.GRAV` | Gravity• Only for Normalized Accel. |
| `PERIOD` | 数字 | `SPFC.VAL.PERIOD` | Period (sec) |
| `aFUNC` | Array[Object] | `SPFC.aFUNC` | Function Data• Insert the data as an object• for User Type |
| `VALUE` | 数字 | `SPFC.properties.aFUNC.items.properties.VALUE` | Value• Depend on Spectral Data Type |

**可选参数**（填不填都行）：

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `iMETHOD` | 整数 | `0` | Scaling Method• Scale Factor: 0• Maximum Value: 1 |
| `DRATIO` | 数字 | `0.05` | Damping Ratio |
| `DESC` | 文字（字符串） | `Blank` | Description |
| `RMF` | 数字 | `无` | ResponseModificationFactor |
| `STR` | 对象（一组键值对） | `无` | StringDataByCode |
| `SPEC_CODE` | 文字（字符串） | `无` | DesignSpectrumType |
| `SFI` | 整数 | `无` | SeismicFortificationIntensity |
| `SC_` | 整数 | `无` | SiteClass |
| `EQ_` | 文字（字符串） | `无` | EarthResponse |
| `DIV` | 文字（字符串） | `无` | Division |
| `BT` | 文字（字符串） | `无` | BridgeType |
| `ZM` | 文字（字符串） | `无` | ZoningMap |
| `ST` | 文字（字符串） | `无` | SiteType |
| `SI` | 文字（字符串） | `无` | SeismicIntensity |
| `SPECTYPE` | 文字（字符串） | `无` | SpectrumType |


### 4. 可选参数放在哪里？

可选参数必须放在正确的 JSON 层级中。以下是每个可选参数的具体位置：

- `iMETHOD` 的路径：**"SPFC" → "iMETHOD"**
  意思是：在 JSON 中依次打开 SPFC, iMETHOD，最后填入 `iMETHOD` 的值
- `DRATIO` 的路径：**"SPFC" → "DRATIO"**
  意思是：在 JSON 中依次打开 SPFC, DRATIO，最后填入 `DRATIO` 的值
- `DESC` 的路径：**"SPFC" → "DESC"**
  意思是：在 JSON 中依次打开 SPFC, DESC，最后填入 `DESC` 的值
- `RMF` 的路径：**"SPFC" → "RMF"**
  意思是：在 JSON 中依次打开 SPFC, RMF，最后填入 `RMF` 的值
- `STR` 的路径：**"SPFC" → "STR"**
  意思是：在 JSON 中依次打开 SPFC, STR，最后填入 `STR` 的值
- `SPEC_CODE` 的路径：**"SPFC" → "STR" → "SPEC_CODE"**
  意思是：在 JSON 中依次打开 SPFC, STR, SPEC_CODE，最后填入 `SPEC_CODE` 的值
- `SFI` 的路径：**"SPFC" → "OPT" → "SFI"**
  意思是：在 JSON 中依次打开 SPFC, OPT, SFI，最后填入 `SFI` 的值
- `SC_` 的路径：**"SPFC" → "OPT" → "SC_"**
  意思是：在 JSON 中依次打开 SPFC, OPT, SC_，最后填入 `SC_` 的值
- `EQ_` 的路径：**"SPFC" → "STR" → "EQ_"**
  意思是：在 JSON 中依次打开 SPFC, STR, EQ_，最后填入 `EQ_` 的值
- `DIV` 的路径：**"SPFC" → "STR" → "DIV"**
  意思是：在 JSON 中依次打开 SPFC, STR, DIV，最后填入 `DIV` 的值

**理解 JSON 路径**：想象你在文件夹里找文件——`A.B.C` 就像 `A文件夹/B文件夹/C文件`。


### 5. 参数之间的关系

以下参数之间存在关联关系：

- `GRAV`：Gravity• Only for Normalized Accel.
- `iTYPE` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `iMETHOD` 有多个可选值（见参数表），不同取值会影响后续参数的需求

**一般规律**：`TYPE` 类参数决定结构类型，然后 `PARAM` 类参数的格式由 `TYPE` 决定。


### 6. 最小可运行代码

以下是能跑起来的最简代码：

```python
import requests
import urllib3
urllib3.disable_warnings()  # 关闭 SSL 警告

# MIDAS 服务地址（根据你的产品修改端口）
BASE = "https://127.0.0.1:1102"

url = f"{BASE}/db/SPFC"

# JSON 数据 — 这是你要发给 MIDAS 的内容
data = {
#     "SPFC": {
#         "NAME": "<NAME>",
#         "iTYPE": 0,
#         "SCALE": 0,
#         "GRAV": 0,
#         "VAL": {
#             "PERIOD": 0
#         },
#         "aFUNC": [],
#         "properties": {
#             "aFUNC": {
#                 "items": {
#                     "properties": {
#                         "VALUE": 0
#                     }
#                 }
#             }
#         }
#     }
# }

# 发送请求
r = requests.post(url, json=data, verify=False)

# 检查结果
if r.status_code == 200:
    print("成功！")
    print(r.json())
else:
    print(f"失败，错误码：{r.status_code}")
```

**运行前确认**：MIDAS Civil 已经打开，并且加载了一个项目。


### 7. 工程意义

参数化建模的核心。一旦掌握，你可以用几十行代码代替几小时的点鼠标操作。参数变化时，重新生成模型只需要几秒钟。

### 8. 常见错误

使用这个接口时最容易犯的错误：

1. **忘记填必填参数**：NAME、iTYPE、SCALE、GRAV、PERIOD、aFUNC、VALUE 是必填的，漏掉任何一个都会报错。
2. **JSON 层级放错**：这个接口有 5 个层级，参数放错层级就不会生效。注意看每个参数的 `json_path`。
3. **数组格式错误**：aTG、aIF、aSRA 需要数组类型，要写成 `[1, 2, 3]` 而不是 `1, 2, 3`。
4. **URL 写错**：确认路径是 `/db/SPFC`——多一个斜杠或少一个都会导致 404 错误。


### 9. Python 批量生成案例

如果你需要创建多个类似的调用（例如创建 100 个节点），可以用列表+循环来生成：

```python
import requests
import urllib3
urllib3.disable_warnings()

BASE = "https://127.0.0.1:1102"

# 定义基础数据模板
def make_data(**kwargs):
    """根据参数生成 Response Spectrum Functions - User Type 的 JSON 数据。"""
    data = {"SPFC": {"NAME": "<NAME>", "iTYPE": 0, "SCALE": 0, "GRAV": 0, "VAL": {"PERIOD": 0}, "aFUNC": [], "properties": {"aFUNC": {"items": {"properties": {"VALUE": 0}}}}}}
    # 在这里修改需要变化的值
    for key, value in kwargs.items():
        # 根据 json_path 更新对应位置的值
        pass  # 具体逻辑见下面的 for 循环例子
    return data

# 批量调用
results = []
for i in range(1, 11):  # 生成 10 个
    data = make_data()    # 在这里修改参数
    r = requests.post(f"{BASE}/db/SPFC", json=data, verify=False)
    results.append(r.json())
    print(f'第 {i} 个完成')
```


### 10. for 循环优化案例

对于批量操作，直接写 for 循环每次发一个请求效率不够高。以下是优化技巧：

**技巧 1：利用 Assign 结构一次发送多个对象**

很多 DB 接口支持在一次请求中发送多个对象，通过 `Assign` 下的编号 `"1"`, `"2"`, ... 区分。

```python
# ❌ 慢：循环 100 次，每次发一个节点
for i in range(100):
    data = {"Assign": {"1": {"X": i, "Y": 0, "Z": 0}}}
    requests.post(url, json=data, verify=False)

# ✅ 快：一次发 100 个节点
nodes = {}
for i in range(100):
    nodes[str(i+1)] = {"X": i, "Y": 0, "Z": 0}
data = {"Assign": nodes}
requests.post(url, json=data, verify=False)
```

**技巧 2：使用列表推导式预生成数据**（在 Response Spectrum Functions - User Type 中适用）

```python
# 列表推导式 — 一行代码生成所有节点的坐标
nodes = {str(i+1): {"X": i*5.0, "Y": 0, "Z": 0} for i in range(100)}
data = {"Assign": nodes}
requests.post(url, json=data, verify=False)
```

**通用优化原则**：

1. 能一次发多个就不要循环发单个
2. 用 `requests.Session()` 代替 `requests.post()` 做批量请求
3. 先生成所有数据，再统一发送，不要在循环里逐个生成+发送



---

### Response Spectrum Load Cases — `/db/SPLC`

**方法**: POST, GET, PUT, DELETE | **参数**: 19 必填 + 27 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Spectrum Load Case Name |
| `SCALE` | 数字 | **是** | Scale Factor |
| `PMFT` | 数字 | **是** | Period Modification Factor |
| `NDP` | 数字 | **是** | Value for Non-dissipative |
| `aFUNCNAME` | 字符串数组 | **是** | Spectrum Name List |
| `iMDTYPE` | 整数 | **是** | Damping Method• Modal: 1• Mass & Stiffness Proportional: 2• Strain Energy Propor |
| `iCOEF` | 整数 | **是** | Damping Type• Calculation from Modal Damping: 2 |
| `iCALC` | 整数 | **是** | Coefficients Calculation method• Frequency: 1• Period: 2 |
| `FP1` | 数字 | **是** | Frequency / Period - Mode1 |
| `FP2` | 数字 | **是** | Frequency / Period - Mode2 |
| `DR1` | 数字 | **是** | Damping ratio - Mode1 |
| `DR2` | 数字 | **是** | Damping Ratio - Mode2 |
| `bACCECC_AUTO` | 是/否（布尔值） | **是** | Eccentricity Data• Automatic: true• User Defined: fasle |
| `bACCECC_CONSIDER_GL` | 是/否（布尔值） | **是** | Limit Minimum Accidental Torsional Moment |
| `aACCECC_ECCEN_LIST` | Array[Object] | **是** | Accidental Eccentricity User List |
| `ACCECC_PERTCENT` | 数字 | **是** | Eccentricitiy Percentage |
| `STORY` | 文字（字符串） | **是** | Story |
| `CROSS` | 数字 | **是** | Cross Position |
| `Along` | 数字 | **是** | Along Position |
| `DIR` | 文字（字符串） | 否 | Direction• X-Y: "XY"• Z: "Z" |
| `ANGLE` | 数字 | 否 | Excitation angle |
| `bDAMP` | 是/否（布尔值） | 否 | Apply Damping Method |
| `INTERP` | 文字（字符串） | 否 | Interpolation of spectral data• Linear: "LINEAR"• Logarithm: "LOG" |
| `DESC` | 文字（字符串） | 否 | Description |
| `COMTYPE` | 文字（字符串） | 否 | Modal Combination Type• SRSS: "SRSS"• CQC: "CQC"• ABS: "ABS"• Linear: "Linear" |
| `bADDSIGN` | 是/否（布尔值） | 否 | Add signs to the results |
| `iSIGNTYPE` | 整数 | 否 | Add signs to the results type• Along the Major Mode Direction: 0• Along the Abso |
| `bMODE` | 是/否（布尔值） | 否 | Select mode shapes |
| `bAUTO` | 是/否（布尔值） | 否 | AutoSearchAngle |
| ... | ... | ... | *还有 17 个可选参数* |

**最简 JSON**：
```json
{
  "SPLC": {
    "NAME": "<NAME>",
    "SCALE": 0,
    "PMFT": 0,
    "NDP": 0,
    "aFUNCNAME": "<aFUNCNAME>",
    "iMDTYPE": 0,
    "iCOEF": 0,
    "iCALC": 0,
    "FP1": 0,
    "FP2": 0,
    "DR1": 0,
    "DR2": 0,
    "bACCECC_AUTO": true,
    "bACCECC_CONSIDER_GL": true,
    "aACCECC_ECCEN_LIST": [],
    "properties": {
      "aACCECC_ECCEN_LIST": {
        "items": {
          "properties": {
            "STORY": "<STORY>",
            "CROSS": 0
          }
        }
      }
    }
  },
  "ACCECC_PERTCENT": 0,
  "Along": 0
}
```

**官方示例**：
```json
{
  "Assign": {
    "6": {
      "NAME": "LC00",
      "DIR": "XY",
      "ANGLE": 0,
      "SCALE": 1,
      "PMFT": 1,
      "bDAMP": false,
      "INTERP": "LOG",
      "DESC": "",
      "COMTYPE": "CQC",
      "bADDSIGN": true,
      "iSIGNTYPE": 0,
      "bMODE": true,
      "aFUNCNAME": [
        "RS_func"
      ],
      "aUSEMODE": [
        {
          "bUSE": true,
          "MSFACTOR": 1
        },
        {
          "bUSE": true,
          "MSFACTOR": 1
        },
        {
          "bUSE": true,
          "MSFACTOR": 1
        }
      ]
    }
  }
}
```


---

### Time History Global Control — `/db/THGC`

**方法**: POST, GET, PUT, DELETE | **参数**: 8 必填 + 20 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `GNT` | 整数 | **是** | Geometric Nonlinearity Type• None: 0• Large Displacements: 1• P-Delta: 2 |
| `ILT` | 整数 | **是** | Initial load type• Perform Nonlinear Static Analysis for Initial load: 0• Import |
| `bPCF` | 是/否（布尔值） | **是** | Permit Cconvergence Failure |
| `MAXNS` | 整数 | **是** | Max. Number of Sub-steps |
| `MAXIT` | 整数 | **是** | Maximum Iteration |
| `SLC` | 文字（字符串） | **是** | Static Load Case Name |
| `SF` | Real | **是** | Scale Factor |
| `LCT` | 整数 | **是** | Load Case Type• Static Load Case: 1• Construction Load: 18 |
| `ENERGYRESULT` | 是/否（布尔值） | 否 | Time History Energy Result |
| `SDVI` | 是/否（布尔值） | 否 | Viscous Damper / Oil Damper Result |
| `SDVE` | 是/否（布尔值） | 否 | Viscoelastic Damper Result |
| `SDST` | 是/否（布尔值） | 否 | Steel Damper Result |
| `SDHY` | 是/否（布尔值） | 否 | Hysteretic Isolator Result |
| `SDIS` | 是/否（布尔值） | 否 | Isolator Result |
| `bMSSSTATUS` | 是/否（布尔值） | 否 | Model Yield Status |
| `IEPI` | 是/否（布尔值） | 否 | Ignore Elements for NL. Analysis Initial Load Option |
| `NSTEP` | 整数 | 否 | Increment Step [nstep] |
| `bROT` | 是/否（布尔值） | 否 | Result Output Type• Final Step Only: false• Step Number Increment for Output: tr |
| ... | ... | ... | *还有 10 个可选参数* |

**最简 JSON**：
```json
{
  "THGC": {
    "GNT": 0,
    "ILT": 0,
    "bPCF": true,
    "MAXNS": 0,
    "MAXIT": 0,
    "properties": {
      "aILL": {
        "items": {
          "properties": {
            "SLC": "<SLC>",
            "SF": {},
            "LCT": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "ENERGYRESULT": false,
      "SDVI": false,
      "SDVE": false,
      "SDST": false,
      "SDHY": false,
      "SDIS": false,
      "bMSSSTATUS": false,
      "GNT": 0,
      "ILT": 0,
      "IEPI": true,
      "NSTEP": 1,
      "bROT": false,
      "SNIO": 1,
      "bPCF": true,
      "MAXNS": 10,
      "MAXIT": 10,
      "bDN": true,
      "bFN": false,
      "bEN": false,
      "DN": 0.001,
      "FN": 0.001,
      "EN": 0.001,
      "bULSM": false,
      "ULSM": 5,
      "aILL": [
        {
          "SLC": "Pretension",
          "SF": 1,
          "LCT": 1
        },
        {
          "SLC": "EarthPressure",
          "SF": 1.2,
          "LCT": 1
        }
      ]
    }
  }
}
```


---

### Time History Global Control — `/db/THGC-M1ᴴˢ⁾`

**方法**: GET, PUT, DELETE | **参数**: 6 必填 + 5 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `GEO_NONL_TYPE` | integer (enum) | **是** | Geometric Nonlinearity Type• None: 0• Large Displacements: 1• P-Delta: 2 |
| `INIT_LOAD_TYPE` | integer (enum) | **是** | Initial Load Type• Perform Nonlinear Static Analysis: 0• Import Static Analysis  |
| `LC_NAME` | 文字（字符串） | **是** | Static Load Case Name |
| `SF` | 数字 | **是** | Scale Factor |
| `LC_TYPE` | 文字（字符串） | **是** | Load Case Type |
| `ITER_PARAM"²⁾` | 对象（一组键值对） | **是** | ITER_PARAM |
| `INIT_LOAD_LIST` | array [object] | 否 | Initial Load List |
| `INCREMENT_STEP"¹⁾` | 对象（一组键值对） | 否 | Increment Step for Initial Load Case |
| `IGNORE_ELEM` | 是/否（布尔值） | 否 | Consider 'Ignore Elements for NL. Analysis Initial Load' |
| `SEQ_LOAD_TYPE` | integer (enum) | 否 | Apply Specified Displacement - with respect to• Undisplaced Position: 0• Displac |
| `HINGE_OPT"³⁾` | 对象（一组键值对） | 否 | Inelastic Hinge Data Option |

**最简 JSON**：
```json
{
  "GEO_NONL_TYPE": {},
  "INIT_LOAD_TYPE": {},
  "LC_NAME": "<LC_NAME>",
  "SF": 0,
  "LC_TYPE": "<LC_TYPE>",
  "ITER_PARAM\"²⁾": {}
}
```


---

### Time History Output Option — `/db/THOO-M1ᴴˢ⁾`

**方法**: GET, PUT, DELETE | **参数**: 2 必填 + 8 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `OUT_OPT` | 对象（一组键值对） | **是** | Nonlinear Analysis Result Output Option |
| `RESULT_SELECTION` | 对象（一组键值对） | **是** | Time History Result Option |
| `Inelastic Hinge: All each Step Output Option• All Inelastic Elements: 0• Selected Elements: 1• No Step-by-Step: 2` | "HINGE_OUT" | 否 | (1) |
| `Fiber Section: All each Step Output Option• All Inelastic Elements: 0• Selected Elements: 1• No Step-by-Step: 2` | "FIBER_OUT" | 否 | (2) |
| `ENERGY_RESULT` | 是/否（布尔值） | 否 | Time History Energy Result |
| `SDVI` | 是/否（布尔值） | 否 | Viscous Damper / Oil Damper Result |
| `SDVE` | 是/否（布尔值） | 否 | Viscoelastic Damper Result |
| `SDST` | 是/否（布尔值） | 否 | Steel Damper Result |
| `SDHY` | 是/否（布尔值） | 否 | Hysteretic Isolator Result |
| `SDIS` | 是/否（布尔值） | 否 | Isolator Result |

**最简 JSON**：
```json
{
  "OUT_OPT": {},
  "RESULT_SELECTION": {}
}
```


---

### Time History Load Cases — `/db/THIS`

**方法**: POST, GET, PUT, DELETE | **参数**: 12 必填 + 46 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `COMMON` | 对象（一组键值对） | **是** | Common Setting |
| `NAME` | 文字（字符串） | **是** | Time History Load Case Name |
| `iATYPE` | 整数 | **是** | Analysis Type• Linear: 1• Nonlinear: 2 |
| `iAMETHOD` | 整数 | **是** | Analysis Method• Modal: 1• Direct Integration: 2• Static: 3 |
| `iTHTYPE` | 整数 | **是** | Time History Type• Transient: 1◦ Modal & Direct Integration |
| `iISTEP` | 整数 | **是** | Increment Steps |
| `ENDTIME` | 数字 | **是** | End Time |
| `INC` | 数字 | **是** | Time Increment |
| `iOUT` | 整数 | **是** | Step Number Increment For Output |
| `INITMETHOD` | 文字（字符串） | **是** | Dynamic Load Type• Initial Load (Global Control)¹⁾: "INIT"• Order in Sequential  |
| `iMDTYPE` | 整数 | **是** | Damping Method• Modal³⁾: 1• Mass & Stiffness Proportional⁴⁾: 2• Strain Energy Pr |
| `iNMM` | 整数 | **是** | Newmark Method Input Type• Constant Acceleration: 1• Linear Acceleration: 2• Use |
| `DESC` | 文字（字符串） | 否 | Description |
| `iGEOM` | 整数 | 否 | Geometric Nonlinearity Type• None: 0• Large Displacements: 1 |
| `INITLOAD` | 整数 | 否 | Useinitialload |
| `bSUBSEQ` | 是/否（布尔值） | 否 | Subsequentto-CheckBox |
| `SUBSEQ` | 整数 | 否 | Subsequentto-Type |
| `LCTYPE` | 文字（字符串） | 否 | LoadCaseType |
| `CASE` | 文字（字符串） | 否 | LoadCaseName |
| `bKEEP` | 是/否（布尔值） | 否 | KeepFinalStepLoadsConstant |
| `bDVA` | 是/否（布尔值） | 否 | CumulateD/V/AResults |
| `iINCCTRL` | 整数 | 否 | Increment Method• Load Control⁵⁾: 0• Displacement Control⁶⁾: 1 |
| ... | ... | ... | *还有 36 个可选参数* |

**最简 JSON**：
```json
{
  "THIS": {
    "COMMON": {
      "NAME": "<NAME>",
      "iATYPE": 0,
      "iAMETHOD": 0,
      "iTHTYPE": 0,
      "iISTEP": 0,
      "ENDTIME": 0,
      "INC": 0,
      "iOUT": 0,
      "INITMETHOD": "<INITMETHOD>",
      "iMDTYPE": 0
    },
    "iNMM": 0
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "3": {
      "COMMON": {
        "NAME": "LMT_01",
        "DESC": "",
        "iATYPE": 1,
        "iAMETHOD": 1,
        "iTHTYPE": 1,
        "iGEOM": 0,
        "ENDTIME": 10,
        "INC": 0.01,
        "iOUT": 1,
        "INITLOAD": 0,
        "INITMETHOD": "ORDER",
        "bSUBSEQ": true,
        "SUBSEQ": 0,
        "LCTYPE": "ST",
        "CASE": "DeadLoad",
        "bKEEP": false,
        "bDVA": false,
        "iMDTYPE": 1
      },
      "DALL": 0.005,
      "aDAMP": [
        {
          "iMODE": 1,
          "DAMPING": 0.006
        },
        {
          "iMODE": 2,
          "DAMPING": 0.007
        }
      ]
    },
    "4": {
      "COMMON": {
        "NAME": "LMT_02",
        "DESC": "",
        "iATYPE": 1,
        "iAMETHOD": 1,
        "iTHTYPE": 1,
        "iGEOM": 0,
        "ENDTIME": 10,
        "INC": 0.01,
        "iOUT": 1,
        "INITLOAD": 0,
        "INITMETHOD": "ORDER",
        "bSUBSEQ": true,
        "SUBSEQ": 1,
        "bKEEP": false,
        "bDVA": false,
        "iMDTYPE": 2
      },
      "iCOEF": 1,
      "bMASSP": true,
      "MASSC": 1.1,
      "bSTIFFP": true,
      "STIFFC": 1.2
    },
    "5": {
      "COMMON": {
        "NAME": "LMT_03",
        "DESC": "",
        "iATYPE": 1,
        "iAMETHOD": 1,
        "iTHTYPE": 1,
        "iGEOM": 0,
        "ENDTIME": 10,
        "INC": 0.01,
        "iOUT": 1,
        "INITLOAD": 0,
        "INITMETHOD": "ORDER",
        "bSUBSEQ": false,
        "bKEEP": false,
        "bDVA": false,
        "iMDTYPE": 2
      },
      "iCOEF": 2,
      "bMASSP": true,
      "bSTIFFP": true,
      "iCALC": 1,
      "FP1": 1.1,
      "DR1": 0.05,
      "FP2": 1.2,
      "DR2": 0.06
    },
    "6": {
      "COMMON": {
        "NAME": "LMT_04",
        "DESC": "",
        "iATYPE": 1,
        "iAMETHOD": 1,
        "iTHTYPE": 1,
        "iGEOM": 0,
        "ENDTIME": 10,
        "INC": 0.01,
        "iOUT": 1,
        "INITLOAD": 0,
        "INITMETHOD": "ORDER",
        "bSUBSEQ": true,
        "SUBSEQ": 0,
        "LCTYPE": "TH",
        "CASE": "LMT_03",
        "bKEEP": true,
        "bDVA": true,
        "iMDTYPE": 2
      },
      "iCOEF": 2,
      "bMASSP": true,
      "bSTIFFP": true,
      "iCALC": 2,
      "FP1": 0.01,
      "DR1": 0.05,
      "FP2": 0.02,
      "DR2": 0.06
    },
    "7": {
      "COMMON": {
        "NAME": "LMT_05",
        "DESC": "",
        "iATYPE": 1,
        "iAMETHOD": 1,
        "iTHTYPE": 1,
        "iGEOM": 0,
        "ENDTIME": 10,
        "INC": 0.01,
        "iOUT": 1,
        "INITLOAD": 0,
        "INITMETHOD": "ORDER",
        "bSUBSEQ": true,
        "SUBSEQ": 0,
        "LCTYPE": "CS",
        "CASE": "DeadLoad",
        "bKEEP": false,
        "bDVA": false,
        "iMDTYPE": 3
      }
    }
  }
}
```


---

### Time History Load Cases — `/db/THIS-M1ᴴˢ⁾`

**方法**: POST, GET, PUT, DELETE | **参数**: 46 必填 + 8 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Name |
| `OUTPUT_STEP` | 整数 | **是** | Step Number Increment for Output |
| `INIT_METHOD` | string (enum) | **是** | Initial Load Method• Initial Load: INIT• Order in Sequence Load: ORDER |
| `USE_INIT_LOAD` | 是/否（布尔值） | **是** | Use Initial Load (Defined in Time History Global Control) |
| `CUM_DVA` | 是/否（布尔值） | **是** | Cumulate D/V/A Results |
| `KEEP_LOAD` | 是/否（布尔值） | **是** | Keep Final Step Loads Constant |
| `SUBSEQ` | 对象（一组键值对） | **是** | Subsequent load options |
| `SUBSEQ_LOAD` | integer (enum) | **是** | Subsequent to - Type• Load Case: 0• Initial Element Forces(Table): 1• Initial Fo |
| `LCTYPE` | string (enum) | **是** | Subsequent load case type• Static: ST• Construction Stage: CS• Time History: TH |
| `CASE` | 文字（字符串） | **是** | Load Case Name |
| `ANAL_CASE` | 对象（一组键值对） | **是** | Analysis case options |
| `ANAL_TYPE` | integer (enum) | **是** | Analysis Type• Linear: 0• Nonlinear: 1 |
| `ANAL_METHOD` | integer (enum) | **是** | Analysis Method• Modal: 0• Direct Integration: 1• Static (Nonlinear ): 2 |
| `ENDTIME` | 数字 | **是** | End Time |
| `TIME_INC` | 数字 | **是** | Time Increment |
| `DAMPING` | 对象（一组键值对） | **是** | DAMPING |
| `DAMPING_METHOD` | integer (enum) | **是** | Damping Method• Direct Modal: 0• Mass & Stiffness Proportional: 1• Strain Energy |
| `ALL_DAMPING_RATIO` | 数字 | **是** | Damping Ratio for All Modes |
| `MODAL_DAMPING_RATIO` | array [object] | **是** | Modal Damping Overrides |
| `COEF_INPUT` | integer (enum) | **是** | Mass and Stiffness Coefficients Type• Direct Specification: 0• Calculate from Mo |
| `MASS_VALUE` | 数字 | **是** | MassProportional Value |
| `STIFF_VALUE` | 数字 | **是** | StiffnessProportional Value |
| `COEF_CALC` | integer (enum) | **是** | Coefficient Calculation Type• Frequency [Hz]: 0• Period [sec]: 1 |
| `FREQ1` | 数字 | **是** | Mode 1 Frequency |
| `FREQ2` | 数字 | **是** | Mode 2 Frequency |
| `PERIOD1` | 数字 | **是** | Mode 1 Period |
| `PERIOD2` | 数字 | **是** | Mode 2 Period |
| `DR1` | 数字 | **是** | Mode 1 Damping Ratio |
| `DR2` | 数字 | **是** | Mode 2 Damping Ratio |
| `TIME_PARAM` | 对象（一组键值对） | **是** | TIME_PARAM |
| `METHOD` | integer (enum) | **是** | Time Integration Parameters• Hilber-Hughes-Taylor Method: 0• Newmark Method: 1 |
| `NEWMARK_METHOD` | integer (enum) | **是** | Newmark Method Input Type• Constant Acceleration: 0• Linear Acceleration: 1• Use |
| `GAMMA` | 数字 | **是** | Gamma |
| `BETA` | 数字 | **是** | Beta |
| `NONL_CTRL_PARAM` | 对象（一组键值对） | **是** | NONL_CTRL_PARAM |
| `ITER_CTRL"¹⁾` | 对象（一组键值对） | **是** | Iteration Controls |
| `INC_STEP` | 整数 | **是** | Increment Steps |
| `INC_CTRL` | 对象（一组键值对） | **是** | Static Loading Control |
| `INC_METHOD` | integer (enum) | **是** | Increment Method• Load Control: 0• Displacement Control: 1 |
| `SF` | 数字 | **是** | Scale Factor |
| `DISP_CTRL` | 对象（一组键值对） | **是** | Displacement Control Option |
| `CTRL_OPT` | integer (enum) | **是** | Control Option• Global Control: 0• Master Node Control: 1 |
| `MAX_TRANS_DISP` | 数字 | **是** | Maximum Translational Displacement |
| `MASTER_NODE` | 整数 | **是** | Master Node |
| `MASTER_DIR` | integer (enum) | **是** | Master Direction• DX: 0• DY: 1• DZ: 2 |
| `MAX_DISP` | 数字 | **是** | Maximum Displacement |
| `DESC` | 文字（字符串） | 否 | Description |
| `OPT_USE` | 是/否（布尔值） | 否 | Use Subsequent to |
| `KEEP_ACC` | 是/否（布尔值） | 否 | Keep Final Step AccelerationsWhen {(Linear + Direct) or (Nonlinear + Direct) or  |
| `TH_TYPE` | integer (enum) | 否 | Time History Type• Transient: 0• Periodic: 1 |
| `USE_MASS` | 是/否（布尔值） | 否 | Use Mass Proportional |
| `USE_STIFF` | 是/否（布尔值） | 否 | UseStiffness Proportional |
| `PERFORM_ITER` | 是/否（布尔值） | 否 | Perform Iteration |
| `DAMP_UPDATE` | integer (enum) | 否 | Damping Matrix Update• No (Use Linear Stiffness): 0• No (Use Initial Stiffness): |

**最简 JSON**：
```json
{
  "NAME": "<NAME>",
  "OUTPUT_STEP": 0,
  "INIT_METHOD": {},
  "USE_INIT_LOAD": true,
  "CUM_DVA": true,
  "KEEP_LOAD": true,
  "SUBSEQ": {},
  "SUBSEQ_LOAD": {},
  "LCTYPE": {},
  "CASE": "<CASE>",
  "ANAL_CASE": {},
  "ANAL_TYPE": {},
  "ANAL_METHOD": {},
  "ENDTIME": 0,
  "TIME_INC": 0,
  "DAMPING": {},
  "DAMPING_METHOD": {},
  "ALL_DAMPING_RATIO": 0,
  "MODAL_DAMPING_RATIO": [],
  "COEF_INPUT": {},
  "MASS_VALUE": 0,
  "STIFF_VALUE": 0,
  "COEF_CALC": {},
  "FREQ1": 0,
  "FREQ2": 0,
  "PERIOD1": 0,
  "PERIOD2": 0,
  "DR1": 0,
  "DR2": 0,
  "TIME_PARAM": {},
  "METHOD": {},
  "NEWMARK_METHOD": {},
  "GAMMA": 0,
  "BETA": 0,
  "NONL_CTRL_PARAM": {},
  "ITER_CTRL\"¹⁾": {},
  "INC_STEP": 0,
  "INC_CTRL": {},
  "INC_METHOD": {},
  "SF": 0,
  "DISP_CTRL": {},
  "CTRL_OPT": {},
  "MAX_TRANS_DISP": 0,
  "MASTER_NODE": 0,
  "MASTER_DIR": {},
  "MAX_DISP": 0
}
```


---

### Time History Functions — `/db/THFC`

**方法**: POST, GET, PUT, DELETE | **参数**: 14 必填 + 2 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Time History Function Name |
| `FUNCTYPE` | 整数 | **是** | Time History Function Type• Time Function: 1• Sinusoidal: 2 |
| `iTYPE` | 整数 | **是** | Time Function Data Type• Normalized Accel.: 1• Acceleration: 2• Force: 3• Moment |
| `iMETHOD` | 整数 | **是** | Scaling Method• Scale Factor: 0• Maximum Value: 1 |
| `SCALE` | 数字 | **是** | Scale Factor• if "iMETHOD": 0 |
| `GRAV` | 数字 | **是** | Gravity |
| `aFUNCDATA` | 对象（一组键值对） | **是** | Time Value List |
| `CONS_A` | 数字 | **是** | Constant A |
| `CONS_C` | 数字 | **是** | Constant C |
| `FREQUENCY` | 数字 | **是** | Frequency |
| `DAMP_FACTOR` | 数字 | **是** | Damping Factor |
| `PHASE_ANGLE` | 数字 | **是** | Phase Angle |
| `TIME` | 数字 | **是** | Time |
| `VALUE` | 数字 | **是** | Value |
| `MAXVALUE` | 数字 | 否 | Maximum Value• if "iMETHOD": 1 |
| `DESC` | 文字（字符串） | 否 | Description |

**最简 JSON**：
```json
{
  "THFC": {
    "NAME": "<NAME>",
    "FUNCTYPE": 0,
    "iTYPE": 0,
    "iMETHOD": 0,
    "SCALE": 0,
    "GRAV": 0,
    "aFUNCDATA": {},
    "CONS_A": 0,
    "CONS_C": 0,
    "FREQUENCY": 0,
    "DAMP_FACTOR": 0,
    "PHASE_ANGLE": 0,
    "properties": {
      "aFUNCDATA": {
        "items": {
          "properties": {
            "TIME": 0,
            "VALUE": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "4": {
      "NAME": "ElCentroSite_Scale",
      "FUNCTYPE": 1,
      "iTYPE": 1,
      "iMETHOD": 0,
      "SCALE": 1,
      "GRAV": 9.806,
      "aFUNCDATA": [
        {
          "TIME": 0.02,
          "VALUE": 0.0051703039
        },
        {
          "TIME": 0.04,
          "VALUE": 0.0042117071
        },
        {
          "TIME": 0.06,
          "VALUE": 0.0032429125
        }
      ],
      "DESC": "1940,ElCentroSite,270Deg"
    },
    "5": {
      "NAME": "ElCentroSite_Max",
      "FUNCTYPE": 1,
      "iTYPE": 1,
      "iMETHOD": 1,
      "MAXVALUE": 0.2,
      "GRAV": 9.806,
      "aFUNCDATA": [
        {
          "TIME": 0.02,
          "VALUE": 0.0051703039
        },
        {
          "TIME": 0.04,
          "VALUE": 0.0042117071
        },
        {
          "TIME": 0.06,
          "VALUE": 0.0032429125
        }
      ],
      "DESC": "1940,ElCentroSite,270Deg"
    }
  }
}
```


---

### Ground Acceleration — `/db/THGA`

**方法**: POST, GET, PUT, DELETE | **参数**: 7 必填 + 4 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Time History Load Case Name |
| `FUNCX` | 文字（字符串） | **是** | X-dir. Function Name |
| `SCALEX` | 数字 | **是** | X-dir. Scale Factor |
| `FUNCY` | 文字（字符串） | **是** | Y-dir. Function Name |
| `SCALEY` | 数字 | **是** | Y-dir. Scale Factor |
| `FUNCZ` | 文字（字符串） | **是** | Z-dir. Function Name |
| `SCALEZ` | 数字 | **是** | Z-dir. Scale Factor |
| `ATIMEX` | 数字 | 否 | X-dir. Arrival Time |
| `ATIMEY` | 数字 | 否 | Y-dir. Arrival Time |
| `ATIMEZ` | 数字 | 否 | Z-dir. Arrival Time |
| `ANGLE` | 数字 | 否 | Angle of Horizontal Ground Acc. |

**最简 JSON**：
```json
{
  "THGA": {
    "NAME": "<NAME>",
    "FUNCX": "<FUNCX>",
    "SCALEX": 0,
    "FUNCY": "<FUNCY>",
    "SCALEY": 0,
    "FUNCZ": "<FUNCZ>",
    "SCALEZ": 0
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "NAME": "TH11",
      "FUNCX": "TF11",
      "SCALEX": 1.1,
      "ATIMEX": 0,
      "FUNCY": "TF1",
      "SCALEY": 1.2,
      "ATIMEY": 0,
      "FUNCZ": "Elcent_h",
      "SCALEZ": 1.3,
      "ATIMEZ": 0,
      "ANGLE": 0
    }
  }
}
```


---

### Dynamic Nodal Loads — `/db/THNL`

**方法**: POST, GET, PUT, DELETE | **参数**: 6 必填 + 1 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `ITEMS` | Array[Object] | **是** | Dynamic Nodal Loads• Insert the data as an object |
| `THLCNAME` | 文字（字符串） | **是** | Time History Load Case Name |
| `FUNC_NAME` | 文字（字符串） | **是** | Time History Function Name¹⁾ |
| `DIR` | 文字（字符串） | **是** | Direction• X: "X"• Y: "Y"• Z: "Z" |
| `ARRIVAL_TIME` | 数字 | **是** | Arrival Time |
| `SCALE_FACTOR` | 数字 | **是** | Scale Factor |
| `ID` | 整数 | 否 | Serial Number |

**最简 JSON**：
```json
{
  "THNL": {
    "ITEMS": [],
    "properties": {
      "ITEMS": {
        "items": {
          "properties": {
            "THLCNAME": "<THLCNAME>",
            "FUNC_NAME": "<FUNC_NAME>",
            "DIR": "<DIR>",
            "ARRIVAL_TIME": 0,
            "SCALE_FACTOR": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "ITEMS": [
        {
          "ID": 1,
          "THLCNAME": "TH1",
          "FUNC_NAME": "TH1",
          "DIR": "Y",
          "ARRIVAL_TIME": 10,
          "SCALE_FACTOR": 1.1
        }
      ]
    },
    "2": {
      "ITEMS": [
        {
          "ID": 1,
          "THLCNAME": "TH1",
          "FUNC_NAME": "TH1",
          "DIR": "Z",
          "ARRIVAL_TIME": 5,
          "SCALE_FACTOR": 1.2
        }
      ]
    }
  }
}
```


---

### Time Varying Static Loads — `/db/THSL`

**方法**: POST, GET, PUT, DELETE | **参数**: 4 必填 + 1 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `THIS_LCNAME` | 文字（字符串） | **是** | Time History Load Case Name |
| `SLOAD` | 文字（字符串） | **是** | Static Load Case Nome |
| `THIS_FUNCNAME` | 文字（字符串） | **是** | Time History Function Name¹⁾ |
| `SCALE` | 数字 | **是** | Scale Factor |
| `ATIME` | 数字 | 否 | Arrival Time |

**最简 JSON**：
```json
{
  "THSL": {
    "THIS_LCNAME": "<THIS_LCNAME>",
    "SLOAD": "<SLOAD>",
    "THIS_FUNCNAME": "<THIS_FUNCNAME>",
    "SCALE": 0
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "THIS_LCNAME": "TH11",
      "SLOAD": "SW",
      "THIS_FUNCNAME": "TF",
      "ATIME": 3,
      "SCALE": 1.2
    },
    "2": {
      "THIS_LCNAME": "TH11",
      "SLOAD": "Pretension",
      "THIS_FUNCNAME": "TF",
      "ATIME": 3,
      "SCALE": 1
    }
  }
}
```


---

### Multiple Support Excitation — `/db/THMS`

**方法**: POST, GET, PUT, DELETE | **参数**: 4 必填 + 9 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `ITEMS` | Array[Object] | **是** | Multiple Support Excitation• Insert the data as an object |
| `LCNAME` | 文字（字符串） | **是** | Time History Load Case Name |
| `FUNCX` | 文字（字符串） | **是** | X-dir. Function Name¹⁾ |
| `SCALEX` | 数字 | **是** | X-dir. scale factor |
| `ID` | 整数 | 否 | Serial Number |
| `ANGLE` | 数字 | 否 | Angle of Horizontal Ground Acc. |
| `ATIMEX` | 数字 | 否 | X-dir. arrival time |
| `FUNCY` | 文字（字符串） | 否 | Y-dir. Function Name¹⁾ |
| `SCALEY` | 数字 | 否 | Y-dir. scale factor |
| `ATIMEY` | 数字 | 否 | Y-dir. arrival time |
| `FUNCZ` | 文字（字符串） | 否 | Z-dir. Function Name¹⁾ |
| `SCALEZ` | 数字 | 否 | Z-dir. scale factor |
| `ATIMEZ` | 数字 | 否 | Z-dir. arrival time |

**最简 JSON**：
```json
{
  "THMS": {
    "ITEMS": [],
    "properties": {
      "ITEMS": {
        "items": {
          "properties": {
            "LCNAME": "<LCNAME>",
            "FUNCX": "<FUNCX>",
            "SCALEX": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "100": {
      "ITEMS": [
        {
          "ID": 1,
          "LCNAME": "LC1",
          "FUNCX": "FC1",
          "SCALEX": 1.1,
          "ATIMEX": 1,
          "FUNCY": "FC1",
          "SCALEY": 1.1,
          "ATIMEY": 1,
          "FUNCZ": "FC1",
          "SCALEZ": 1.1,
          "ATIMEZ": 1,
          "ANGLE": 0
        }
      ]
    }
  }
}
```


---

### Define Construction Stage — `/db/STAG`

**方法**: POST, GET, PUT, DELETE | **参数**: 7 必填 + 13 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | CS Stage Name |
| `DURATION` | 数字 | **是** | CS Stage Duration |
| `INCRE_STEP` | 整数 | **是** | Load Incremental Steps• if "bLOAD_STEP": true |
| `GRUP_NAME` | 文字（字符串） | **是** | Deactivated Structure Group Name |
| `BNGR_NAME` | 文字（字符串） | **是** | Activated Boundary Group Name |
| `POS` | 文字（字符串） | **是** | Support / Spring Position• "DEFORMED"• "ORIGINAL" |
| `LOAD_NAME` | 文字（字符串） | **是** | Deactivated Load Group Name |
| `bSV_RSLT` | 是/否（布尔值） | 否 | Save Result - Stage |
| `bSV_STEP` | 是/否（布尔值） | 否 | Save Result - Additional Steps |
| `bLOAD_STEP` | 是/否（布尔值） | 否 | Load Incremental Steps for Material Nonlinear Analysis |
| `ADD_STEP` | 数字数组 | 否 | Additional Step |
| `ACT_ELEM` | Array[Object] | 否 | Activation Structure Group• Insert the data as an object |
| `DACT_ELEM` | Array[Object] | 否 | Deactivation Structure Group• Insert the data as an object |
| `ACT_BNGR` | Array[Object] | 否 | Activation Boundary Group• Insert the data as an object |
| `DACT_BNGR` | 字符串数组 | 否 | Deactivated Boundary Group Name• [Boundary Group Name] |
| `ACT_LOAD` | Array[Object] | 否 | Activation Load Group• Insert the data as an object |
| `DACT_LOAD` | Array[Object] | 否 | Deactivation Load Group• Insert the data as an object |
| ... | ... | ... | *还有 3 个可选参数* |

**最简 JSON**：
```json
{
  "STAG": {
    "NAME": "<NAME>",
    "DURATION": 0,
    "INCRE_STEP": 0,
    "properties": {
      "ACT_ELEM": {
        "items": {
          "properties": {
            "GRUP_NAME": "<GRUP_NAME>"
          }
        }
      },
      "ACT_BNGR": {
        "items": {
          "properties": {
            "BNGR_NAME": "<BNGR_NAME>",
            "POS": "<POS>"
          }
        }
      },
      "ACT_LOAD": {
        "items": {
          "properties": {
            "LOAD_NAME": "<LOAD_NAME>"
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "NAME": "CS01",
      "DURATION": 10,
      "bSV_RSLT": true,
      "bSV_STEP": true,
      "bLOAD_STEP": true,
      "INCRE_STEP": 5,
      "ADD_STEP": [
        5,
        8
      ],
      "ACT_ELEM": [
        {
          "GRUP_NAME": "SG_01",
          "AGE": 10
        }
      ],
      "ACT_BNGR": [
        {
          "BNGR_NAME": "BG_01",
          "POS": "DEFORMED"
        }
      ],
      "ACT_LOAD": [
        {
          "LOAD_NAME": "LG_01",
          "DAY": "5.000000"
        }
      ]
    },
    "2": {
      "NAME": "CS2",
      "DURATION": 20,
      "bSV_RSLT": true,
      "bSV_STEP": false,
      "bLOAD_STEP": false,
      "ADD_STEP": [],
      "ACT_ELEM": [
        {
          "GRUP_NAME": "SG_02",
          "AGE": 20
        }
      ],
      "ACT_BNGR": [
        {
          "BNGR_NAME": "BG_02",
          "POS": "DEFORMED"
        }
      ],
      "ACT_LOAD": [
        {
          "LOAD_NAME": "LG_02",
          "DAY": "FIRST"
        }
      ]
    },
    "3": {
      "NAME": "CS03",
      "DURATION": 10,
      "bSV_RSLT": true,
      "bSV_STEP": false,
      "bLOAD_STEP": false,
      "ADD_STEP": [],
      "DACT_ELEM": [
        {
          "GRUP_NAME": "SG_02",
          "REDIST": 100
        }
      ],
      "DACT_BNGR": [
        "BG_02"
      ],
      "DACT_LOAD": [
        {
          "LOAD_NAME": "LG_02",
          "DAY": "FIRST"
        }
      ]
    }
  }
}
```


---

### Composite Section for Construction Stage — `/db/CSCS`

**方法**: POST, GET, PUT, DELETE | **参数**: 6 必填 + 15 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `SEC` | 整数 | **是** | Section ID |
| `ASTAGE` | 文字（字符串） | **是** | Active Stage |
| `TYPE` | 文字（字符串） | **是** | Composite Type• General: "GENERAL"• User: "USER" |
| `vPARTINFO` | Array[Object] | **是** | Part Information• Insert the data as an object |
| `PART` | 整数 | **是** | Composite Section Part |
| `MTYPE` | 文字（字符串） | **是** | Material Type• Element: "ELEM"• Material: "MATL" |
| `bTAP` | 是/否（布尔值） | 否 | Tapered Type |
| `OPT_UPDATE_ALL_H` | 是/否（布尔值） | 否 | AutoCalculationOptionNotationalsize,h |
| `MAT` | 文字（字符串） | 否 | Material ID• Element: Blank• Material: Material ID as String |
| `CSTAGE` | 文字（字符串） | 否 | Composite Stage• Active Stage: Blank• Target Stage: Construction Stage Name |
| `AGE` | 数字 | 否 | Material Age |
| `PARTINFO_H` | 数字 | 否 | Notional Size of Member |
| `PARTINFO_VS` | 数字 | 否 | Volume-surface ratio, v/s |
| `PARTINFO_M` | 数字 | 否 | Module of an exposed surface, M |
| `AREA` | 数字 | 否 | Area |
| `ASY` | 数字 | 否 | Effective Shear Area, y-axis |
| ... | ... | ... | *还有 5 个可选参数* |

**最简 JSON**：
```json
{
  "CSCS": {
    "SEC": 0,
    "ASTAGE": "<ASTAGE>",
    "TYPE": "<TYPE>",
    "vPARTINFO": [],
    "properties": {
      "vPARTINFO": {
        "items": {
          "properties": {
            "PART": 0,
            "MTYPE": "<MTYPE>"
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "SEC": 1,
      "ASTAGE": "CS1",
      "TYPE": "NORMAL",
      "bTAP": false,
      "vPARTINFO": [
        {
          "PART": 1,
          "MTYPE": "ELEM",
          "MAT": "",
          "CSTAGE": "",
          "AGE": 2,
          "PARTINFO_H": 1.5,
          "PARTINFO_VS": 1.5,
          "PARTINFO_M": 1.5,
          "AREA": 1,
          "ASY": 1,
          "ASZ": 1,
          "IXX": 1,
          "IYY": 1,
          "IZZ": 1,
          "WAREA": 1,
          "IW": 1
        },
        {
          "PART": 2,
          "MTYPE": "MATL",
          "MAT": "3",
          "CSTAGE": "CS2",
          "AGE": 5,
          "PARTINFO_H": 0.245,
          "PARTINFO_VS": 0,
          "PARTINFO_M": 0,
          "AREA": 1,
          "ASY": 1,
          "ASZ": 1,
          "IXX": 1,
          "IYY": 1,
          "IZZ": 1,
          "WAREA": 1,
          "IW": 1
        }
      ]
    }
  }
}
```


---

### Time Loads for Construction Stage — `/db/TMLD`

**方法**: POST, GET, PUT, DELETE | **参数**: 2 必填 + 2 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `ITEMS` | Array[Object] | **是** | Time Load for Construction Stage• Insert the data as an object |
| `DAY` | 数字 | **是** | Time Loads |
| `ID` | 整数 | 否 | Serial Number |
| `GROUP_NAME` | 文字（字符串） | 否 | Load Group Name |

**最简 JSON**：
```json
{
  "TMLD": {
    "ITEMS": [],
    "properties": {
      "ITEMS": {
        "items": {
          "properties": {
            "DAY": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "10": {
      "ITEMS": [
        {
          "ID": 1,
          "GROUP_NAME": "DL(BC)2",
          "DAY": 35
        }
      ]
    },
    "11": {
      "ITEMS": [
        {
          "ID": 1,
          "GROUP_NAME": "DL(BC)2",
          "DAY": 25
        }
      ]
    }
  }
}
```


---

### Set-Back Loads for Nonlinear Construction Stage — `/db/STBK`

**方法**: POST, GET, PUT, DELETE | **参数**: 3 必填 + 4 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NODE1` | 整数 | **是** | Node 1 |
| `NODE2` | 整数 | **是** | Node 2 |
| `LCNAME` | 文字（字符串） | **是** | Load Case Name |
| `DX` | 数字 | 否 | Dx |
| `DY` | 数字 | 否 | Dy |
| `DZ` | 数字 | 否 | Dz |
| `GROUP_NAME` | 文字（字符串） | 否 | Load Group Name |

**最简 JSON**：
```json
{
  "STBK": {
    "NODE1": 0,
    "NODE2": 0,
    "LCNAME": "<LCNAME>"
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "NODE1": 39,
      "NODE2": 22,
      "DX": 0.1,
      "DY": 0.2,
      "DZ": 0.3,
      "LCNAME": "LiveLoad",
      "GROUP_NAME": ""
    },
    "2": {
      "NODE1": 28,
      "NODE2": 21,
      "DX": 0.6,
      "DY": 0.1,
      "DZ": 0.1,
      "LCNAME": "DeadLoad",
      "GROUP_NAME": ""
    }
  }
}
```


---

### Camber for Construction Stage — `/db/CMCS`

**方法**: POST, GET, PUT, DELETE | **参数**: 2 必填 + 0 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `DEFORM` | 数字 | **是** | Deformation |
| `USER` | 数字 | **是** | User |

**最简 JSON**：
```json
{
  "CMCS": {
    "DEFORM": 0,
    "USER": 0
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "23": {
      "DEFORM": 0,
      "USER": 0
    },
    "25": {
      "DEFORM": 0.1,
      "USER": 0.17
    },
    "27": {
      "DEFORM": 0,
      "USER": 0.28
    },
    "28": {
      "DEFORM": 0,
      "USER": 0.34
    },
    "29": {
      "DEFORM": 0,
      "USER": 0.39
    },
    "31": {
      "DEFORM": 0,
      "USER": 0.46
    },
    "33": {
      "DEFORM": 0,
      "USER": 0.49
    }
  }
}
```


---

### Creep Coefficient for Construction Stage — `/db/CRPC`

**方法**: POST, GET, PUT, DELETE | **参数**: 2 必填 + 2 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `ITEMS` | Array[Object] | **是** | Creep Coefficient for Construction Stage• Insert the data as an object |
| `CREEP` | 数字 | **是** | Creep Coefficient |
| `ID` | 整数 | 否 | Serial Number |
| `GROUP_NAME` | 文字（字符串） | 否 | Load Group Name |

**最简 JSON**：
```json
{
  "CRPC": {
    "ITEMS": [],
    "properties": {
      "ITEMS": {
        "items": {
          "properties": {
            "CREEP": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "25": {
      "ITEMS": [
        {
          "ID": 1,
          "GROUP_NAME": "2ndDeadLoad",
          "CREEP": 1.2
        }
      ]
    },
    "26": {
      "ITEMS": [
        {
          "ID": 1,
          "GROUP_NAME": "Selfweight",
          "CREEP": 1.5
        }
      ]
    }
  }
}
```


---

### Ambient Temperature Functions — `/db/ETFC`

**方法**: POST, GET, PUT, DELETE | **参数**: 6 必填 + 4 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Function Name |
| `TYPE` | 文字（字符串） | **是** | Function Type• Constant: "CONST"• Sine Function: "SINE"• User: "USER" |
| `SCALE_FACTOR` | 数字 | **是** | Scale Factor |
| `ITEM` | Array[Object] | **是** | Function Data• Insert the data as an object |
| `TIME` | 数字 | **是** | Time |
| `VALUE` | 数字 | **是** | Temperature |
| `TEMP` | 数字 | 否 | Temperature |
| `MAX_TEMP` | 数字 | 否 | Max. Temperature (T) |
| `MEAN_TEMP` | 数字 | 否 | Temperature Mean (To) |
| `DELAY_TIME` | 数字 | 否 | Delay Time (to) |

**最简 JSON**：
```json
{
  "ETFC": {
    "NAME": "<NAME>",
    "TYPE": "<TYPE>",
    "SCALE_FACTOR": 0,
    "ITEM": [],
    "properties": {
      "ITEM": {
        "items": {
          "properties": {
            "TIME": 0,
            "VALUE": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "NAME": "AmbientTemperature",
      "TYPE": "CONST",
      "TEMP": 30
    },
    "2": {
      "NAME": "11",
      "TYPE": "USER",
      "SCALE_FACTOR": 1,
      "ITEM": [
        {
          "TIME": 0,
          "VALUE": 20
        },
        {
          "TIME": 1,
          "VALUE": 30
        },
        {
          "TIME": 2,
          "VALUE": 40
        }
      ]
    },
    "3": {
      "NAME": "22",
      "TYPE": "SINE",
      "MAX_TEMP": 20,
      "MEAN_TEMP": 0,
      "DELAY_TIME": 1
    }
  }
}
```


---

### Convection Coefficient Functions — `/db/CCFC`

**方法**: POST, GET, PUT, DELETE | **参数**: 7 必填 + 0 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Function Name |
| `TYPE` | 文字（字符串） | **是** | Function Type• Constant: "CONST"• User: "USER" |
| `COEF` | 数字 | **是** | Convection Coefficient |
| `SCALE_FACTOR` | 数字 | **是** | Scale Factor |
| `ITEM` | Array[Object] | **是** | Function Data• Insert the data as an object |
| `TIME` | 数字 | **是** | Time |
| `VALUE` | 数字 | **是** | Temperature |

**最简 JSON**：
```json
{
  "CCFC": {
    "NAME": "<NAME>",
    "TYPE": "<TYPE>",
    "COEF": 0,
    "SCALE_FACTOR": 0,
    "ITEM": [],
    "properties": {
      "ITEM": {
        "items": {
          "properties": {
            "TIME": 0,
            "VALUE": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "NAME": "ConvectionCoeff",
      "TYPE": "CONST",
      "COEF": 15
    },
    "2": {
      "NAME": "11",
      "TYPE": "USER",
      "SCALE_FACTOR": 1.2,
      "ITEM": [
        {
          "TIME": 0,
          "VALUE": 25
        },
        {
          "TIME": 1,
          "VALUE": 35
        }
      ]
    }
  }
}
```


---

### Element Convection Boundary — `/db/HECB`

**方法**: POST, GET, PUT, DELETE | **参数**: 4 必填 + 2 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `ITEMS` | Array[Object] | **是** | Element Convection Boundary• Insert the data as an object |
| `FACE_NO` | 整数 | **是** | Face#1 ~ Face#6 |
| `CCFC_NAME` | 文字（字符串） | **是** | Convection Coefficient Function |
| `ETFC_NAME` | 文字（字符串） | **是** | Ambient Temperature Function |
| `ID` | 整数 | 否 | Serial Number |
| `GROUP_NAME` | 文字（字符串） | 否 | Boundary Group Name |

**最简 JSON**：
```json
{
  "HECB": {
    "ITEMS": [],
    "properties": {
      "ITEMS": {
        "items": {
          "properties": {
            "FACE_NO": 0,
            "CCFC_NAME": "<CCFC_NAME>",
            "ETFC_NAME": "<ETFC_NAME>"
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "10": {
      "ITEMS": [
        {
          "ID": 1,
          "GROUP_NAME": "",
          "FACE_NO": 1,
          "CCFC_NAME": "ConvectionCoeff",
          "ETFC_NAME": "22"
        }
      ]
    },
    "11": {
      "ITEMS": [
        {
          "ID": 1,
          "GROUP_NAME": "",
          "FACE_NO": 2,
          "CCFC_NAME": "ConvectionCoeff",
          "ETFC_NAME": "AmbientTemperature"
        }
      ]
    }
  }
}
```


---

### Prescribed Temperature — `/db/HSPT`

**方法**: POST, GET, PUT, DELETE | **参数**: 2 必填 + 2 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `ITEMS` | Array[Object] | **是** | Prescribed Temperature• Insert the data as an object |
| `TEMPER` | 数字 | **是** | Temperature |
| `ID` | 整数 | 否 | Serial Number |
| `GROUP_NAME` | 文字（字符串） | 否 | Boundary Group Name |

**最简 JSON**：
```json
{
  "HSPT": {
    "ITEMS": [],
    "properties": {
      "ITEMS": {
        "items": {
          "properties": {
            "TEMPER": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "ITEMS": [
        {
          "ID": 1,
          "GROUP_NAME": "",
          "TEMPER": 25
        }
      ]
    },
    "2": {
      "ITEMS": [
        {
          "ID": 1,
          "GROUP_NAME": "",
          "TEMPER": 25
        }
      ]
    },
    "3": {
      "ITEMS": [
        {
          "ID": 1,
          "GROUP_NAME": "",
          "TEMPER": 20
        }
      ]
    }
  }
}
```


---

### Heat Source Functions — `/db/HSFC`

**方法**: POST, GET, PUT, DELETE | **参数**: 6 必填 + 8 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Function Name |
| `TYPE` | 文字（字符串） | **是** | Function Type• Constant: "CONST"• Code: "FUNC"• User: "USER" |
| `SCALE_FACTOR` | 数字 | **是** | Scale Factor |
| `ITEM` | Array[Object] | **是** | Define Functions• Insert data as object |
| `TIME` | 数字 | **是** | Time |
| `VALUE` | 数字 | **是** | Temperature |
| `TEMP_CONST` | 数字 | 否 | Heat Source |
| `OPT_USE_CONC_DATA` | 是/否（布尔值） | 否 | Use Concrete Data• true |
| `CEMENT_TYPE` | 整数 | 否 | Cement Type• Normal Portland Cement: 0• Moderate Heat Portland Cement: 1• High-e |
| `TEMP_FUNC` | 整数 | 否 | Temperature• 10: 0• 20: 1• 30: 2 |
| `CEMENT_CONT` | 数字 | 否 | Cement Content |
| `K` | 数字 | 否 | Maximize Adiabatic Temp. Rise (K) |
| `ALPHA` | 数字 | 否 | Reactive Velocity Coefficient (a) |
| `IS_ADIABATIC_TEMP` | 是/否（布尔值） | 否 | Data Type• Heat Source: false• Temperature: true |

**最简 JSON**：
```json
{
  "HSFC": {
    "NAME": "<NAME>",
    "TYPE": "<TYPE>",
    "SCALE_FACTOR": 0,
    "ITEM": [],
    "properties": {
      "ITEM": {
        "items": {
          "properties": {
            "TIME": 0,
            "VALUE": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "NAME": "F1",
      "TYPE": "USER",
      "IS_ADIABATIC_TEMP": false,
      "SCALE_FACTOR": 1,
      "ITEM": [
        {
          "TIME": 0,
          "VALUE": 0
        },
        {
          "TIME": 1,
          "VALUE": 5
        },
        {
          "TIME": 2,
          "VALUE": 10
        }
      ]
    },
    "2": {
      "NAME": "F2",
      "TYPE": "CONST",
      "TEMP_CONST": 10
    },
    "3": {
      "NAME": "F3",
      "TYPE": "FUNC",
      "OPT_USE_CONC_DATA": false,
      "K": 20,
      "ALPHA": 0
    },
    "4": {
      "NAME": "F4",
      "TYPE": "FUNC",
      "OPT_USE_CONC_DATA": true,
      "CEMENT_TYPE": 0,
      "TEMP_FUNC": 1,
      "CEMENT_CONT": 2400
    }
  }
}
```


---

### Assign Heat Source — `/db/HAHS`

**方法**: POST, GET, PUT, DELETE | **参数**: 1 必填 + 0 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `FUNC_NAME` | 文字（字符串） | **是** | Heat Source Function Name |

**最简 JSON**：
```json
{
  "HAHS": {
    "FUNC_NAME": "<FUNC_NAME>"
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "358": {
      "FUNC_NAME": "HSF1"
    },
    "359": {
      "FUNC_NAME": "HSF2"
    }
  }
}
```


---

### Pipe Cooling — `/db/HPCE`

**方法**: POST, GET, PUT, DELETE | **参数**: 2 必填 + 8 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Pipe Cooling Name |
| `ITEMS` | 整数数组 | **是** | Node List |
| `DIAMETER` | 数字 | 否 | Cooling Pipe Diameter |
| `COEF` | 数字 | 否 | Convection Coefficient |
| `HEAT` | 数字 | 否 | Specific Heat |
| `DENSITY` | 数字 | 否 | Weight Density |
| `TEMPER` | 数字 | 否 | Inlet Temperature |
| `FLOW_RATE` | 数字 | 否 | Flow Rate |
| `START_TIME` | 整数 | 否 | Inflow Start Time |
| `END_TIME` | 整数 | 否 | Inflow End Time |

**最简 JSON**：
```json
{
  "HPCE": {
    "NAME": "<NAME>",
    "ITEMS": 0
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "NAME": "PC1",
      "DIAMETER": 0,
      "COEF": 0,
      "HEAT": 0.1,
      "DENSITY": 10,
      "TEMPER": 20,
      "FLOW_RATE": 20,
      "START_TIME": 0,
      "END_TIME": 0,
      "ITEMS": [
        1,
        2
      ]
    }
  }
}
```


---

### Define Construction Stage for Hydration — `/db/HSTG`

**方法**: POST, GET, PUT, DELETE | **参数**: 5 必填 + 6 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Hydration Stage Name |
| `ADD_STEP` | 数字数组 | **是** | Additional Step |
| `ACT_ELEM` | 字符串数组 | **是** | Activation Structure Group List |
| `ACT_BNGR` | 字符串数组 | **是** | Activation Boundary Group List |
| `DACT_BNGR` | 字符串数组 | **是** | Deactivation Boundary Group List |
| `bINITAL_TEMP` | 是/否（布尔值） | 否 | Used Initial Temperature |
| `INITIAL_TEMP` | 数字 | 否 | Initial Temperature |
| `ACT_LOAD` | Array[Object] | 否 | Activation Load Group List• Insert the data as an object |
| `DACT_LOAD` | Array[Object] | 否 | Deactivation Load Group List• Insert the data as an object |
| `LOAD_NAME` | 文字（字符串） | 否 | Load Case Name |
| `DAY` | 文字（字符串） | 否 | Deactivation Day |

**最简 JSON**：
```json
{
  "HSTG": {
    "NAME": "<NAME>",
    "ADD_STEP": 0,
    "ACT_ELEM": "<ACT_ELEM>",
    "ACT_BNGR": "<ACT_BNGR>",
    "DACT_BNGR": "<DACT_BNGR>"
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "NAME": "CS01",
      "bINITAL_TEMP": true,
      "INITIAL_TEMP": 25,
      "ADD_STEP": [
        10,
        20,
        30,
        45,
        60,
        80,
        100,
        130,
        170,
        250,
        350,
        500,
        700,
        1000
      ],
      "ACT_ELEM": [
        "GR2",
        "GR1"
      ],
      "ACT_BNGR": [
        "BNGR3",
        "BNGR2",
        "BNGR1"
      ],
      "DACT_BNGR": [
        "BNGR4"
      ],
      "ACT_LOAD": [
        {
          "LOAD_NAME": "LG01",
          "DAY": "10.000000"
        }
      ],
      "DACT_LOAD": [
        {
          "LOAD_NAME": "LG02",
          "DAY": "80.000000"
        }
      ]
    }
  }
}
```


---

### Settlement Group — `/db/SMPT`

**方法**: POST, GET, PUT, DELETE | **参数**: 3 必填 + 0 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Settlement Group Name |
| `SETTLE` | 数字 | **是** | Settlement Displacement |
| `ITEMS` | 整数数组 | **是** | Node List |

**最简 JSON**：
```json
{
  "SMPT": {
    "NAME": "<NAME>",
    "SETTLE": 0,
    "ITEMS": 0
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "NAME": "SG1",
      "SETTLE": 25,
      "ITEMS": [
        100,
        101
      ]
    },
    "2": {
      "NAME": "SG2",
      "SETTLE": 15,
      "ITEMS": [
        102,
        103
      ]
    }
  }
}
```


---

### Settlement Load Cases — `/db/SMLC`

**方法**: POST, GET, PUT, DELETE | **参数**: 7 必填 + 0 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Settlement Load Case Name |
| `DESC` | 文字（字符串） | **是** | Description |
| `FACTOR` | 数字 | **是** | Settlement Scale Factor |
| `MIN` | 整数 | **是** | Settlement - Min. Group Nos. |
| `MAX` | 整数 | **是** | Settlement - Max. Group Nos. |
| `ST_GROUPS` | 字符串数组 | **是** | Selected Settlement Group Name |
| `KEY` | 整数 | **是** | Settlement Load Case No. |

**最简 JSON**：
```json
{
  "SMLC": {
    "NAME": "<NAME>",
    "DESC": "<DESC>",
    "FACTOR": 0,
    "MIN": 0,
    "MAX": 0,
    "ST_GROUPS": "<ST_GROUPS>"
  },
  "KEY": 0
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "NAME": "SMLC1",
      "DESC": "",
      "FACTOR": 1.2,
      "MIN": 1,
      "MAX": 1,
      "ST_GROUPS": [
        "SG1",
        "SG2"
      ]
    },
    "2": {
      "NAME": "SMLC2",
      "DESC": "",
      "FACTOR": 1,
      "MIN": 1,
      "MAX": 1,
      "ST_GROUPS": [
        "SG1",
        "SG2"
      ]
    }
  }
}
```


---

### Pre-composite Section — `/db/PLCB`

**方法**: POST, GET, PUT, DELETE | **参数**: 1 必填 + 0 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `LCNAME_ITEM` | 字符串数组 | **是** | Static Load Case Name |

**最简 JSON**：
```json
{
  "PLCB": {
    "LCNAME_ITEM": "<LCNAME_ITEM>"
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "LCNAME_ITEM": [
        "DL(BC)1",
        "DL(BC)3"
      ]
    }
  }
}
```


---

### Load Sequence for Nonlinear — `/db/LDSQ`

**方法**: POST, GET, PUT, DELETE | **参数**: 1 必填 + 0 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `LCNAME_ITEM` | 文字（字符串） | **是** | Load Case Name |

**最简 JSON**：
```json
{
  "LDSQ": {
    "LCNAME_ITEM": "<LCNAME_ITEM>"
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "LCNAME_ITEM": [
        "DL(BC)4",
        "DL(AC)"
      ]
    }
  }
}
```


---

### Wave Loads — `/db/WVLD`

**方法**: POST, GET, PUT, DELETE | **参数**: 1 必填 + 52 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Wave Load Name |
| `DESC` | 文字（字符串） | 否 | Description |
| `bSTLD` | 是/否（布尔值） | 否 | Use Static Load Generation |
| `bTHIS` | 是/否（布尔值） | 否 | Use Time History Load Generation |
| `NAME_THIS` | 文字（字符串） | 否 | Time History Load Case Name |
| `VERT_COORD` | 文字（字符串） | 否 | Vertical Coordinate• Global Y: "GLOBAL_Y"• Global Z: "GLOBAL_Z" |
| `DENSITY` | 数字 | 否 | Water Weight Density |
| `DEPTH` | 数字 | 否 | Water Depth |
| `COEF` | Array | 否 | Drag & Inertia Coefficients |
| `TYPE` | 文字（字符串） | 否 | Type• Constant• Linear Interpolation |
| `COEF_S` | Array[Object] | 否 | Coefficients S Array• Insert data as object |
| ... | ... | ... | *还有 42 个可选参数* |

**最简 JSON**：
```json
{
  "WVLD": {
    "NAME": "<NAME>"
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "NAME": "TEST1",
      "DESC": "",
      "bSTLD": true,
      "bTHIS": false,
      "NAME_THIS": "",
      "VERT_COORD": "GLOBAL_Z",
      "DENSITY": 10,
      "DEPTH": 10,
      "COEF": {
        "TYPE": "CONST",
        "COEF_S": [
          {
            "GRUP": "",
            "DIA": 0.013,
            "DRAG_COEF_X": 0,
            "DRAG_COEF_Y": 0.65,
            "DRAG_COEF_Z": 0.65,
            "INER_COEF_X": 0,
            "INER_COEF_Y": 1.65,
            "INER_COEF_Z": 1.65
          }
        ],
        "COEF_R": [
          {
            "GRUP": "",
            "DIA": 0.013,
            "DRAG_COEF_X": 0,
            "DRAG_COEF_Y": 0.65,
            "DRAG_COEF_Z": 0.65,
            "INER_COEF_X": 0,
            "INER_COEF_Y": 1.65,
            "INER_COEF_Z": 1.65
          }
        ],
        "bOVER": false,
        "OVER_S": [
          {
            "GRUP": "",
            "DIA": 0,
            "DRAG_COEF_X": 0,
            "DRAG_COEF_Y": 0.65,
            "DRAG_COEF_Z": 0.65,
            "INER_COEF_X": 0,
            "INER_COEF_Y": 1.65,
            "INER_COEF_Z": 1.65
          }
        ],
        "OVER_R": [
          {
            "GRUP": "",
            "DIA": 0,
            "DRAG_COEF_X": 0,
            "DRAG_COEF_Y": 0.65,
            "DRAG_COEF_Z": 0.65,
            "INER_COEF_X": 0,
            "INER_COEF_Y": 1.65,
            "INER_COEF_Z": 1.65
          }
        ]
      },
      "CHAR": {
        "THEORY": "AIRY",
        "FUNC": 1,
        "DIR": 0,
        "HEIGHT": 2,
        "CHAR_TYPE": "PERIOD",
        "LENGTH": 36.58115359112376,
        "PERIOD": 5,
        "K_FACTOR": 0.85,
        "SURFACE_V": 1,
        "BOTTOM_Y": 0
      },
      "PROF": {
        "CUR_DIR": 0,
        "CUR_FACTOR": 1,
        "GRID_DATA": [
          {
            "D": 0,
            "V": 2
          },
          {
            "D": 10,
            "V": 2
          }
        ]
      },
      "FLOOD_GRUP": [],
      "GROWTH": [],
      "GRID_X": 73,
      "GRID_Z": 20,
      "USERGRID": [
        [
          {
            "X": 0,
            "Z": 0,
            "ELEV": 10.999999999999998,
            "VX": 0.46611591251822093,
            "VCX": 1.9999999999999998,
            "VT": 2.466115912518221,
            "VZ": 0,
            "AX": 0,
            "AZ": 0
          },
          {
            "X": 0.5080563698912746,
            "Z": 0,
            "ELEV": 10.996194698091744,
            "VX": 0.4643422007468476,
            "VCX": 1.9999999999999998,
            "VT": 2.4643422007468474,
            "VZ": 0,
            "AX": 0.04781033826731333,
            "AZ": 0
          }
        ],
        [
          {
            "X": 0,
            "Z": 0.6315789473684209,
            "ELEV": 0,
            "VX": 0.46886137836547037,
            "VCX": 1.9999999999999998,
            "VT": 2.46886137836547,
            "VZ": 0,
            "AX": 0,
            "AZ": -0.059587324982965595
          },
          {
            "X": 0.5080563698912746,
            "Z": 0.6315789473684209,
            "ELEV": 0,
            "VX": 0.4670772192676694,
            "VCX": 1.9999999999999998,
            "VT": 2.467077219267669,
            "VZ": 0.00441575086277806,
            "AX": 0.048111030297930554,
            "AZ": -0.059345050577191534
          }
        ],
        [
          {
            "X": 0,
            "Z": 1.2631578947368418,
            "ELEV": 0,
            "VX": 0.47713011800289007,
            "VCX": 1.9999999999999998,
            "VT": 2.47713011800289,
            "VZ": 0,
            "AX": 0,
            "AZ": -0.11973183458159217
          },
          {
            "X": 0.5080563698912746,
            "Z": 1.2631578947368418,
            "ELEV": 0,
            "VX": 0.47531449385436797,
            "VCX": 1.9999999999999998,
            "VT": 2.4753144938543676,
            "VZ": 0.008883520087762302,
            "AX": 0.049016648597539646,
            "AZ": -0.11924443173271622
          }
        ],
        [
          {
            "X": 0,
            "Z": 1.8947368421052626,
            "ELEV": 0,
            "VX": 0.491019538713367,
            "VCX": 1.9999999999999998,
            "VT": 2.491019538713367,
            "VZ": 0,
            "AX": 0,
            "AZ": -0.18099043562139414
          },
          {
            "X": 0.5080563698912746,
            "Z": 1.8947368421052626,
            "ELEV": 0,
            "VX": 0.48915106112571083,
            "VCX": 1.9999999999999998,
            "VT": 2.489151061125711,
            "VZ": 0.013455938823090603,
            "AX": 0.050537861517275816,
            "AZ": -0.18025216263367277
          }
        ],
        [
          {
            "X": 0,
            "Z": 2.5263157894736836,
            "ELEV": 0,
            "VX": 0.5106932604428185,
            "VCX": 1.9999999999999998,
            "VT": 2.5106932604428187,
            "VZ": 0,
            "AX": 0,
            "AZ": -0.24391915274789258
          },
          {
            "X": 0.5080563698912746,
            "Z": 2.5263157894736836,
            "ELEV": 0,
            "VX": 0.5087499184043227,
            "VCX": 1.9999999999999998,
            "VT": 2.5087499184043227,
            "VZ": 0.01818687100749593,
            "AX": 0.05269258922680228,
            "AZ": -0.2429213126289284
          }
        ]
      ],
      "bSELFW": true,
      "bBUOYANT": true,
      "CREST": "MXM",
      "UNIT": "PHASE",
      "INITAL_POS": 0,
      "STEP": 10,
      "POS": 3
    }
  }
}
```


---

### Ignore Elements for Load Cases — `/db/IELC`

**方法**: POST, GET, PUT, DELETE | **参数**: 3 必填 + 0 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `ELEMENT` | 整数 | **是** | Element |
| `LCNAME` | 文字（字符串） | **是** | Load Case Name |
| `OPT_IGNORE` | 是/否（布尔值） | **是** | Ignore Option |

**最简 JSON**：
```json
{
  "IELC": {
    "ELEMENT": 0,
    "LCNAME": "<LCNAME>",
    "OPT_IGNORE": true
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "ELEMENT": 5,
      "LCNAME": "DL",
      "OPT_IGNORE": true
    },
    "2": {
      "ELEMENT": 5,
      "LCNAME": "LL",
      "OPT_IGNORE": true
    },
    "3": {
      "ELEMENT": 18,
      "LCNAME": "DL",
      "OPT_IGNORE": false
    }
  }
}
```


---

### Large Displacement - Initial Forces for Geometric Stiffness — `/db/IFGS`

**方法**: POST, GET, PUT | **参数**: 2 必填 + 0 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `DIR` | 文字（字符串） | **是** | Direction |
| `INIT_FORCE` | 数字 | **是** | Initial Force |

**最简 JSON**：
```json
{
  "IFGS": {
    "DIR": "<DIR>",
    "INIT_FORCE": 0
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "9": {
      "DIR": "GY",
      "INIT_FORCE": 200
    },
    "16": {
      "DIR": "AXIAL",
      "INIT_FORCE": 10
    }
  }
}
```


---

### Small Displacement - Initial Force Control Data — `/db/EFCT`

**方法**: POST, GET, PUT, DELETE | **参数**: 3 必填 + 3 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `LCNAME` | 文字（字符串） | **是** | Load Case Name |
| `COMB_LIST` | Array[Object] | **是** | Load Cases• Insert the data as an object |
| `FACTOR` | 数字 | **是** | Scale Factor |
| `bADDLC` | 是/否（布尔值） | 否 | Use Add Initial Force to Element Force |
| `bUSECOMB` | 是/否（布尔值） | 否 | Use Initial Force Combination |
| `bCHECK_GEOM_STIFF` | 是/否（布尔值） | 否 | Check to Reflect Initial Axial Forces into Geometric Stiffness |

**最简 JSON**：
```json
{
  "EFCT": {
    "LCNAME": "<LCNAME>",
    "COMB_LIST": [],
    "properties": {
      "COMB_LIST": {
        "items": {
          "properties": {
            "FACTOR": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "bADDLC": false,
      "LCNAME": "DL",
      "bUSECOMB": true,
      "COMB_LIST": [
        {
          "LCNAME": "DL",
          "FACTOR": 1.2
        },
        {
          "LCNAME": "LL",
          "FACTOR": 1
        }
      ],
      "bCHECK_GEOM_STIFF": false
    }
  }
}
```


---

### Small Displacement - Initial Element Force — `/db/INMF`

**方法**: POST, GET, PUT, DELETE | **参数**: 3 必填 + 1 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `ELEM_TYPE` | 文字（字符串） | **是** | Element Type• Beam: "BEAM"• Truss: "TRUSS"• Elastic Link: "E-LINK"• General Link |
| `ELEM_KEY` | 整数 | **是** | Element ID |
| `ELEM_FORCES` | Array[Number, 12] | **是** | Element Forces• [Axial-i, Shear(y)-i, Shear(z)-i, Torsion-i, Moment(y)-i, Moment |
| `ELEMENT_FORCES` | Array | 否 | ElementForces |

**最简 JSON**：
```json
{
  "INMF": {
    "ELEM_TYPE": "<ELEM_TYPE>",
    "ELEM_KEY": 0
  },
  "ELEM_FORCES": 0
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "ELEM_TYPE": "BEAM",
      "ELEM_KEY": 15,
      "ELEMENT_FORCES": [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12
      ]
    },
    "2": {
      "ELEM_TYPE": "TRUSS",
      "ELEM_KEY": 112,
      "ELEMENT_FORCES": [
        1,
        2
      ]
    },
    "3": {
      "ELEM_TYPE": "E-LINK",
      "ELEM_KEY": 1,
      "ELEMENT_FORCES": [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12
      ]
    },
    "4": {
      "ELEM_TYPE": "G-LINK",
      "ELEM_KEY": 1,
      "ELEMENT_FORCES": [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12
      ]
    }
  }
}
```


---

### Grid Analysis Load — `/db/GALDᴶ⁾`

**方法**: POST, GET, PUT, DELETE | **参数**: 17 必填 + 1 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `LCNAME` | 文字（字符串） | **是** | Load Case Name |
| `LCTYPE` | 文字（字符串） | **是** | Load Case Type• Dead Load : "DL"• Vehicles Live Load : "VLL"• Crowd Live Load :  |
| `SUBTYPE` | 文字（字符串） | **是** | Sub Load Type<strong>• </strong>When Load Case Type = "VLL"◦ L-Load Type-A (Load |
| `LOAD` | Array[Object] | **是** | Define Dead Load• Insert data as object |
| `LTYPE` | 文字（字符串） | **是** | Dead Load Type• Point : "POINT"• Line : "LINE"• Area : "AREA" |
| `CLINE` | 文字（字符串） | **是** | Center Line |
| `SMLTYPE` | 文字（字符串） | **是** | Main Line Type - Start• Main Girder : "G"• Load Line : "L" |
| `EMLTYPE` | 文字（字符串） | **是** | Main Line Type - End• Main Girder : "G"• Load Line : "L" |
| `SMLINE` | 文字（字符串） | **是** | Main Line - Start |
| `EMLINE` | 文字（字符串） | **是** | Main Line - End |
| `SCROSS` | 文字（字符串） | **是** | Cross Beam - Start |
| `ECROSS` | 文字（字符串） | **是** | Cross Line - End |
| `SLOAD` | 数字 | **是** | Load Value - Start |
| `ELOAD` | 数字 | **是** | Load Value - End |
| `SMEDIAN` | 文字（字符串） | **是** | Median - Start• None : "None"• Load Line : Load Line Name |
| `EMEDIAN` | 文字（字符串） | **是** | Median - End• None : "None"• Load Line : Load Line Name |
| `LLOAD` | 数字 | **是** | Load Value |
| `MLRANGE` | 数字 | 否 | Main Load Width• When Sub Load Type is L-Load Type-A (Load Range 6m) or L-Load T |

**最简 JSON**：
```json
{
  "GALD": {
    "LCNAME": "<LCNAME>",
    "LCTYPE": "<LCTYPE>",
    "SUBTYPE": "<SUBTYPE>",
    "LOAD": [],
    "properties": {
      "LOAD": {
        "items": {
          "properties": {
            "LTYPE": "<LTYPE>",
            "CLINE": "<CLINE>",
            "SMLTYPE": "<SMLTYPE>",
            "EMLTYPE": "<EMLTYPE>",
            "SMLINE": "<SMLINE>",
            "EMLINE": "<EMLINE>",
            "SCROSS": "<SCROSS>",
            "ECROSS": "<ECROSS>",
            "SLOAD": 0,
            "ELOAD": 0,
            "SMEDIAN": "<SMEDIAN>",
            "EMEDIAN": "<EMEDIAN>",
            "LLOAD": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "LCNAME": "DL",
      "LCTYPE": "DL",
      "LOAD": [
        {
          "LTYPE": "POINT",
          "CLINE": "L1",
          "SMLTYPE": "G",
          "EMLTYPE": "G",
          "SMLINE": "G1",
          "EMLINE": "G1",
          "SCROSS": "C1",
          "ECROSS": "C1",
          "SLOAD": 12,
          "ELOAD": 0
        },
        {
          "LTYPE": "LINE",
          "CLINE": "L1",
          "SMLTYPE": "G",
          "EMLTYPE": "G",
          "SMLINE": "G1",
          "EMLINE": "G2",
          "SCROSS": "C1",
          "ECROSS": "C1",
          "SLOAD": 13,
          "ELOAD": 11
        },
        {
          "LTYPE": "AREA",
          "CLINE": "L1",
          "SMLTYPE": "L",
          "EMLTYPE": "L",
          "SMLINE": "L1",
          "EMLINE": "L3",
          "SCROSS": "C14",
          "ECROSS": "C18",
          "SLOAD": 21,
          "ELOAD": 24
        }
      ]
    }
  }
}
```


---

### Main Control Data — `/db/ACTL`

**方法**: POST, GET, PUT, DELETE | **参数**: 2 必填 + 7 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `ITER` | 数字 | **是** | Number of Iterations / Load Case |
| `TOL` | 数字 | **是** | Convergence Tolerance |
| `ARDC` | 是/否（布尔值） | 否 | Auto Rotational DOF Constraint for Truss / Plane Stress / Solid Elements |
| `ANRC` | 是/否（布尔值） | 否 | Auto Normal Rotation Constraint for Plate Elements |
| `CSECF` | 是/否（布尔值） | 否 | Consider Section Stiffness Scale Factor for Stress Calculation |
| `TRS` | 是/否（布尔值） | 否 | Transfer Reactions of Slave Node to the Master Node |
| `CRBAR` | 是/否（布尔值） | 否 | Consider Reinforcement for Section Stiffness Calculation |
| `BMSTRESS` | 是/否（布尔值） | 否 | Calculate Equivalent Beam Stresses (Von-Mises and Max-Shear) |
| `CLATS` | 是/否（布尔值） | 否 | Change Local Axis of Tapered Section for Force / Stress Calculation |

**最简 JSON**：
```json
{
  "ACTL": {
    "ITER": 0,
    "TOL": 0
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "ARDC": true,
      "ANRC": true,
      "ITER": 20,
      "TOL": 0.001,
      "CSECF": false,
      "TRS": true,
      "CRBAR": false,
      "BMSTRESS": false,
      "CLATS": false
    }
  }
}
```


---

### Main Control Data — `/db/ACTL-M1ᴴˢ⁾`

**方法**: GET, PUT, DELETE | **参数**: 0 必填 + 11 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `ARCD` | 是/否（布尔值） | 否 | Auto Rotational DOF Constraint |
| `ANRC` | 是/否（布尔值） | 否 | Auto Normal Rotation Constraint |
| `CSECF` | 是/否（布尔值） | 否 | Consider Section Stiffness Scale Factor |
| `CRBAR` | 是/否（布尔值） | 否 | Consider Reinforcement for Section Stiffness |
| `TRS` | 是/否（布尔值） | 否 | Transfer Reactions to Master Node |
| `CLATS` | 是/否（布尔值） | 否 | Change Local Axis of Tapered Section |
| `BMSTRESS` | 是/否（布尔值） | 否 | Calculate Equivalent Beam Stresses |
| `CLFORM` | 是/否（布尔值） | 否 | Classical Formula for Solid Element |
| `BSCHG` | string (enum) | 否 | Beam Section Property Changes• Constant: CONSTANT• Change: CHANGE |
| `CABINIT` | 是/否（布尔值） | 否 | Consider Initial Tension for Cable Element |
| ... | ... | ... | *还有 1 个可选参数* |


---

### P-Delta Analysis Control — `/db/PDEL`

**方法**: POST, GET, PUT, DELETE | **参数**: 4 必填 + 1 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `ITER` | 数字 | **是** | Number of Iterations |
| `PDEL_CASES` | Array[Object] | **是** | Load Cases• Insert the data as an object |
| `LCNAME` | 文字（字符串） | **是** | Load Case Name |
| `FACTOR` | 数字 | **是** | Scale Factor |
| `TOL` | 数字 | 否 | Convergence Tolerance |

**最简 JSON**：
```json
{
  "PDEL": {
    "ITER": 0,
    "PDEL_CASES": [],
    "properties": {
      "PDEL_CASES": {
        "items": {
          "properties": {
            "LCNAME": "<LCNAME>",
            "FACTOR": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "ITER": 5,
      "TOL": 1e-05,
      "PDEL_CASES": [
        {
          "LCNAME": "A",
          "FACTOR": 1
        },
        {
          "LCNAME": "B",
          "FACTOR": 1
        }
      ]
    }
  }
}
```


---

### Buckling Analysis Control — `/db/BUCK`

**方法**: POST, GET, PUT, DELETE | **参数**: 3 必填 + 7 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `MODE_NUM` | 整数 | **是** | Number of Modes |
| `ITEMS` | Array[Object] | **是** | Load Cases• Insert the data as an object |
| `LCNAME` | 文字（字符串） | **是** | Load Case Name |
| `OPT_POSITIVE` | 是/否（布尔值） | 否 | Load Factor Range Type• Positive Value Only: true• Search: false |
| `OPT_CONSIDER_AXIAL_ONLY` | 是/否（布尔值） | 否 | Frame Geometric Stiffness Option• Consider Axial Only |
| `LOAD_FACTOR_FROM` | 数字 | 否 | Search From• When the "OPT_POSITIVE" is false |
| `LOAD_FACTOR_TO` | 数字 | 否 | Search To• When the "OPT_POSITIVE" is false |
| `OPT_STURM_SEQ` | 是/否（布尔值） | 否 | Check Sturm Sequence |
| `FACTOR` | 数字 | 否 | Scale Factor |
| `LOAD_TYPE` | 整数 | 否 | Load Type• Variable: 0• Constant: 1 |

**最简 JSON**：
```json
{
  "BUCK": {
    "MODE_NUM": 0,
    "ITEMS": [],
    "properties": {
      "ITEMS": {
        "items": {
          "properties": {
            "LCNAME": "<LCNAME>"
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "MODE_NUM": 12,
      "OPT_POSITIVE": true,
      "OPT_CONSIDER_AXIAL_ONLY": true,
      "LOAD_FACTOR_FROM": 0,
      "LOAD_FACTOR_TO": 0,
      "OPT_STURM_SEQ": true,
      "ITEMS": [
        {
          "LCNAME": "A",
          "FACTOR": 1,
          "LOAD_TYPE": 0
        },
        {
          "LCNAME": "B",
          "FACTOR": 1,
          "LOAD_TYPE": 1
        }
      ]
    }
  }
}
```


---

### Eigenvalue Analysis Control — `/db/EIGV`

**方法**: POST, GET, PUT, DELETE | **参数**: 9 必填 + 6 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TYPE` | 文字（字符串） | **是** | Type of Analysis• Subspace Iteration: "EIGEN"• Lanczos: "LANCZOS"• Ritz Vectors: |
| `iFREQ` | 整数 | **是** | Number of Frequencies |
| `iITER` | 整数 | **是** | Number of Iterations |
| `FRMIN` | 数字 | **是** | Seach From [cps]• When the "bMINMAX" is true• "FRMIN" < "FRMAX" |
| `FRMAX` | 数字 | **是** | Seach to [cps]• When the "bMINMAX" is true• "FRMIN" < "FRMAX" |
| `iGNUM` | 整数 | **是** | Number of Generations for Each GL-link Force |
| `vRITZ` | Array[Object] | **是** | Load Cases• Insert the data as an object |
| `KIND` | 文字（字符串） | **是** | Load Case Type• Ground Acc.: "GROUND"• General: "CASE" |
| `CASE` | 文字（字符串） | **是** | Load Case Name• General: Defined Load Case Name• Ground Acc. X: "ACCX"• Ground A |
| `iDIM` | 整数 | 否 | Subspace Dimension |
| `TOL` | 数字 | 否 | Convergence Tolerance |
| `bMINMAX` | 是/否（布尔值） | 否 | Frequency Range of Interest |
| `bSTRUM` | 是/否（布尔值） | 否 | Sturm Sequence Check |
| `bINCNL` | 是/否（布尔值） | 否 | Include GL-link Force Vectors |
| `iNOG` | 整数 | 否 | Number of Generations |

**最简 JSON**：
```json
{
  "EIGV": {
    "TYPE": "<TYPE>",
    "iFREQ": 0,
    "iITER": 0,
    "FRMIN": 0,
    "FRMAX": 0,
    "iGNUM": 0,
    "vRITZ": [],
    "properties": {
      "vRITZ": {
        "items": {
          "properties": {
            "KIND": "<KIND>",
            "CASE": "<CASE>"
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "TYPE": "EIGEN",
      "iFREQ": 100,
      "iITER": 20,
      "iDIM": 1,
      "TOL": 1e-10,
      "bMINMAX": false,
      "FRMIN": 0,
      "FRMAX": 1600,
      "bSTRUM": false
    }
  }
}
```


---

### Eigenvalue Analysis Control — `/db/EIGV-M1ᴴˢ⁾`

**方法**: GET, PUT, DELETE | **参数**: 7 必填 + 6 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `ANAL_TYPE` | string (enum) | **是** | Eigen Vectors• Eigen Vectors (Lanczos): LANCZOS• Ritz Vectors: RITZ |
| `FREQ_NO` | 整数 | **是** | Number of Frequencies |
| `OPT_USE` | 是/否（布尔值） | **是** | Include GL-link Force Vectors |
| `RITZ_LOAD` | array [object] | **是** | Load Case / Number of Generations / Starting Load Vectors |
| `TYPE` | string (enum) | **是** | Load Case Type• Static Load Case : LOAD• Ground Acceleration : GROUND |
| `NUM_OF_GEN` | 整数 | **是** | Number of Generations |
| `LOAD_NAME` | 文字（字符串） | **是** | Load Case Name |
| `FREQ_RANGE` | 对象（一组键值对） | 否 | Frequency range of interest |
| `FREQ_MIN` | 数字 | 否 | Search FromWhen OPT_USE = true |
| `FREQ_MAX` | 数字 | 否 | Search ToWhen OPT_USE = true |
| `STURM_SEQ` | 是/否（布尔值） | 否 | Sturm Sequence Check |
| `GLINK_VECTOR` | 对象（一组键值对） | 否 | Include GL-link Force Vectors |
| `GLINK_NUMBER` | 整数 | 否 | Number of Generations for Each GL-link Force VectorsWhen OPT_USE = true |

**最简 JSON**：
```json
{
  "ANAL_TYPE": {},
  "FREQ_NO": 0,
  "OPT_USE": true,
  "RITZ_LOAD": [],
  "TYPE": {},
  "NUM_OF_GEN": 0,
  "LOAD_NAME": "<LOAD_NAME>"
}
```


---

### Heat of Hydration Analysis Control — `/db/HHCT`

**方法**: POST, GET, PUT, DELETE | **参数**: 2 必填 + 13 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `STAGE_NAME` | 文字（字符串） | **是** | Construction Stage for Hydration• When the "FINAL_STAGE" is false |
| `M_EFF_MOD` | 对象（一组键值对） | **是** | Effective Modulus Data |
| `FINAL_STAGE` | 是/否（布尔值） | 否 | Final Stage• Last Stage: true• Other Stage: false |
| `THETA` | 数字 | 否 | Integration Factor |
| `INIT_TEMP` | 数字 | 否 | Initial Temperature |
| `EVAL` | 文字（字符串） | 否 | Element Stress Evaluation• Center: "CENTER"• Gauss: "GAUSS"• Nodal Point: "NODAL |
| `OPT_USE_EQUI_AGE` | 是/否（布尔值） | 否 | Use Equivalent Age by Time & Temperature |
| `OPT_INCL_SELF_WEIGHT` | 是/否（布尔值） | 否 | Include Self-weight Load |
| `SELF_WEIGHT_FACTOR` | 数字 | 否 | Self-weight Factor |
| `OPT_IS_CREEP_SHRINKAGE` | 是/否（布尔值） | 否 | Creep & Shrinkage Option |
| `ITEM` | 对象（一组键值对） | 否 | Creep & Shrinkage• Insert the data as an object |
| `OPT_USE_CREEP_SHRINKAGE` | 是/否（布尔值） | 否 | UseCreep&Shrinkage |
| ... | ... | ... | *还有 3 个可选参数* |

**最简 JSON**：
```json
{
  "HHCT": {
    "STAGE_NAME": "<STAGE_NAME>",
    "ITEM": {
      "M_EFF_MOD": {}
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "FINAL_STAGE": true,
      "STAGE_NAME": "",
      "THETA": 1,
      "INIT_TEMP": 20,
      "EVAL": "GAUSS",
      "OPT_USE_EQUI_AGE": true,
      "OPT_INCL_SELF_WEIGHT": false,
      "SELF_WEIGHT_FACTOR": -1,
      "OPT_IS_CREEP_SHRINKAGE": true,
      "ITEM": {
        "TYPE": "BOTH",
        "CREEP_CALC_METHOD": 0,
        "M_GENERAL": {
          "ITER": 20,
          "TOL": 0.001
        }
      }
    }
  }
}
```


---

### Heat of Hydration Analysis Control — `db/HHCT-M1ᴴˢ⁾`

**方法**: GET, PUT, DELETE | **参数**: 10 必填 + 13 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `STAGE_NAME` | 文字（字符串） | **是** | Stage Name |
| `ITEM` | 对象（一组键值对） | **是** | Creep & Shrinkage Settings |
| `M_EFF_MOD` | 对象（一组键值对） | **是** | Effective Modulus Input ParametersWhen CREEP_CALC_METHOD = 1 |
| `PHI1` | 数字 | **是** | phi 1 |
| `DAY1` | 整数 | **是** | day 1 |
| `PHI2` | 数字 | **是** | phi 2 |
| `DAY2` | 整数 | **是** | day 2 |
| `SELF_WEIGHT_FACTOR` | 数字 | **是** | Self Weight Factor |
| `OPT_CHECK` | 是/否（布尔值） | **是** | Use Option |
| `VALUE` | 数字 | **是** | Tolerance |
| `FINAL_STAGE` | boolean (enum) | 否 | Final Stage• Last Stage: true• Other Stage: false |
| `INIT_TEMP` | 数字 | 否 | Initial Temperature |
| `EVAL` | string (enum) | 否 | Element Stress Evaluation• Center: CENTER• Gauss: GAUSS• Nodal Point: NODAL |
| `OPT_IS_CREEP_SHRINKAGE` | 是/否（布尔值） | 否 | Creep & Shrinkage |
| `TYPE` | string (enum) | 否 | Creep & Shrinkage Type• Creep: CREEP• Shrinkage: SHRINKAGE• Creep && Shrinkage:  |
| `CREEP_CALC_METHOD` | integer (enum) | 否 | Creep Calculation Method• General: 0• Effective Modulus: 1 |
| `OPT_USE_EQUI_AGE` | 是/否（布尔值） | 否 | Use Equivalent Age by Time & Temperature |
| `OPT_INCL_SELF_WEIGHT` | 是/否（布尔值） | 否 | Include Selfweight Load |
| `ITER` | 整数 | 否 | Max. No. of Iterations per Increment |
| `CONVERGENCE` | 对象（一组键值对） | 否 | Convergence Criteria / Error ToleranceAt least one of DISP, LOAD, or WORK is req |
| ... | ... | ... | *还有 3 个可选参数* |

**最简 JSON**：
```json
{
  "STAGE_NAME": "<STAGE_NAME>",
  "ITEM": {},
  "M_EFF_MOD": {},
  "PHI1": 0,
  "DAY1": 0,
  "PHI2": 0,
  "DAY2": 0,
  "SELF_WEIGHT_FACTOR": 0,
  "OPT_CHECK": true,
  "VALUE": 0
}
```


---

### Moving Load Analysis Control — `/db/MVCT`

**方法**: POST, GET, PUT, DELETE | **参数**: 12 必填 + 19 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `POINT` | 文字（字符串） | **是** | Load Point Selection¹⁾• Influence Line Dependent Point: "INF"• All Points: "ALL" |
| `iIGPN` | 整数 | **是** | Number/Line Element• When "iIGP" is 0 |
| `DIST` | 数字 | **是** | Distance between Points• When "iIGP" is 1 |
| `PLATE` | 文字（字符串） | **是** | Options• Center: "CENTER"• Center + Nodal: "NODAL" |
| `FRAME` | 文字（字符串） | **是** | Options• Normal: "NORMAL"• Normal + Concurrent Force/Stress: "AXIAL" |
| `RGN` | 文字（字符串） | **是** | Structure Group Name• When the "bRG" is true |
| `DGN` | 文字（字符串） | **是** | Structure Group Name• When the "bDG" is true |
| `FGN` | 文字（字符串） | **是** | Structure Group Name• When the "bFG" is true |
| `LGN` | 文字（字符串） | **是** | Boundary Group Name• When the "bLG" is true |
| `MINFACTS2` | 数字 | **是** | Minimum Limit of Lane Factor (s2) |
| `MAXV` | 整数 | **是** | Maximum No. of Cars |
| `INCV` | 整数 | **是** | Increment of Moving Vehicle at Variable Spacing |
| `METHOD` | 文字（字符串） | 否 | Analysis Method¹⁾• Exact: "EXACT"• Pivot: "PIVOT"• Quick: "QUICK" |
| `iIGP` | 整数 | 否 | Influence Generating Points• Number/Line Element: 0• Distance between Points: 1 |
| `bSTRCALC` | 是/否（布尔值） | 否 | Stress• Active/Inactive |
| `bCONCURRENT` | 是/否（布尔值） | 否 | Concurrent Force• Active/Inactive |
| `bCONCLINK` | 是/否（布尔值） | 否 | Link Options• Concurrent Force of Elastic/General Links |
| `bCSTRCALC` | 是/否（布尔值） | 否 | Combined Stress• Active/Inactive |
| `bREAC` | 是/否（布尔值） | 否 | Reactions• Active/Inactive |
| `bRG` | 是/否（布尔值） | 否 | Option• All: false• Structure Group: true |
| `bDISP` | 是/否（布尔值） | 否 | Displacements• Active/Inactive |
| `bDG` | 是/否（布尔值） | 否 | Option• All: false• Structure Group: true |
| ... | ... | ... | *还有 9 个可选参数* |

**最简 JSON**：
```json
{
  "MVCT": {
    "POINT": "<POINT>",
    "iIGPN": 0,
    "DIST": 0,
    "PLATE": "<PLATE>",
    "FRAME": "<FRAME>",
    "RGN": "<RGN>",
    "DGN": "<DGN>",
    "FGN": "<FGN>",
    "LGN": "<LGN>",
    "MINFACTS2": 0,
    "MAXV": 0,
    "INCV": 0
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "METHOD": "EXACT",
      "POINT": "INF",
      "iIGP": 0,
      "iIGPN": 3,
      "PLATE": "NODAL",
      "bSTRCALC": true,
      "bCONCURRENT": true,
      "bCONCLINK": true,
      "FRAME": "AXIAL",
      "bCSTRCALC": true,
      "bREAC": true,
      "bRG": false,
      "RGN": "",
      "bDISP": true,
      "bDG": false,
      "DGN": "",
      "bFM": true,
      "bFG": false,
      "FGN": "",
      "bL": true,
      "bLG": false,
      "LGN": ""
    }
  }
}
```


---

## Moving Load Analysis Control - China — `/db/MVCTch`

**HTTP 方法**: POST, GET, PUT, DELETE | **参数总数**: 111（91 必填 + 20 可选）

### 1. 这是什么？（工程含义）

**Moving Load Analysis Control - China** — 这是模型数据库的创建和查询操作，属于 Analysis 类别。

Load Point Selection• Influence Line Dependent Point: "INF"• All Points: "ALL"

> 简单说：这个接口用来**Moving Load Analysis Control - China**。

### 2. JSON 结构（逐层解释）

下面按照从外到内的顺序解释每一层的 JSON 结构：

```json
{
  "MVCTCH": {
    "POINT": "<POINT>",
    "iIGP (可选)": "0",
    "bSTRCALC (可选)": "false",
    "bCSTRCALC (可选)": "false",
    "bREAC (可选)": "false",
    "bRG (可选)": "false",
    "bDISP (可选)": "false",
    "bDG (可选)": "false",
    "bFM (可选)": "false",
    "bFG (可选)": "false",
    "bL (可选)": "false",
    "bLG (可选)": "false",
    "bIF (可选)": "false",
    "bBC (可选)": "false",
    "UNUMT": 0,
    "DIST": 0,
    "PLATE": "<PLATE>",
    "FRAME": "<FRAME>",
    "RGN": "<RGN>",
    "DGN": "<DGN>",
    "FGN": "<FGN>",
    "LGN": "<LGN>",
    "iCODETYPE": 0,
    "iNFM": 0,
    "iSLCM": 0,
    "iBC": "0",
    "FREQ": {
      "USER_F": "<USER_F>",
      "SBEM_L": 0,
      "SBEM_E": 0,
      "SBEM_IC": 0,
      "SBEM_MC": 0,
      "CBEM_A": 0,
      "CBEM_B": 0,
      "CBEM_L": 0,
      "CBEM_E": 0,
      "CBEM_IC": 0,
      "CBEM_MC": 0,
      "iARCH_TYPE": 0,
      "ARCH_N": 0,
      "ARCH_E": 0,
      "ARCH_IC": 0,
      "ARCH_MC": 0,
      "CABL_A": 0,
      "CABL_L": 0,
      "SUSP_L": 0,
      "SUSP_E": 0,
      "SUSP_I": 0,
      "SUSP_HG": 0,
      "SUSP_M": 0
    },
    "BRIDGE2": {
      "METHOD": "<METHOD>",
      "SIMPLE_U": 0,
      "SIMPLE_L": 0,
      "COMPO_U": 0,
      "COMPO_L": 0,
      "CONC_U": 0,
      "CONC_L": 0,
      "CONC_H": 0,
      "ARCH_U": 0,
      "ARCH_LAMBDA": 0,
      "bCHECK (可选)": "false",
      "bLFAI (可选)": "false",
      "bLENGTH (可选)": "false",
      "MU1": 0,
      "MU2": 0,
      "MU3": 0,
      "LFAI": 0,
      "MUR1": 0,
      "MUR2": 0,
      "MUR3": 0,
      "HC": 0,
      "GROUP": "<GROUP>"
    },
    "BRIDGE1": {
      "RC_C1L1": 0,
      "RC_C1F1": 0,
      "RC_C1L2": 0,
      "RC_C1F2": 0,
      "RC_bCASE2 (可选)": "false",
      "RC_GROUP (可选)": "Blank",
      "STL_bCASE2 (可选)": "false",
      "STL_GROUP (可选)": "<STL_GROUP>",
      "RC_C2L1": 0,
      "RC_C2F1": 0,
      "RC_C2L2": 0,
      "RC_C2F2": 0,
      "STL_C1V1": 0,
      "STL_C1V2": 0,
      "STL_C2V1": 0,
      "STL_C2V2": 0,
      "MBRG_RL1": 0,
      "MBRG_RF1": 0,
      "MBRG_RL2": 0,
      "MBRG_RF2": 0,
      "MBRG_RF3": 0,
      "MBRG_RF4": 0,
      "MBRG_CF1": 0,
      "MBRG_CF2": 0,
      "MBRG_CF3": 0,
      "TRAIN_SUB_TYPE": "<TRAIN_SUB_TYPE>",
      "TRAIN_NUMERATOR": 0,
      "TRAIN_DENOMINATOR": 0,
      "TRAIN_H": 0,
      "TRAIN_bCLSL": 0,
      "TRAIN_bALSL": 0,
      "TRAIN_LAMBDA": 0,
      "TRAIN_F": 0,
      "TRAIN_GROUP": "<TRAIN_GROUP>"
    }
  }
}
```

**第 1 层：`MVCTCH`** — 29 个参数在这一层

- `"POINT"`: 文字（字符串） — Load Point Selection• Influence Line Dependent Point: "INF"• All Points: "ALL"
- `"iIGP"`: 整数 — Influence Generating Points• Number/Line Element: 0• Distance between Points: 1
- `"UNUMT"`: 整数 — Number/Line Element• When "iIGP" is 0
- `"DIST"`: 数字 — Distance between Points• When "iIGP" is 1
- `"PLATE"`: 文字（字符串） — Options• Center: "CENTER"• Center + Nodal: "NODAL"
- `"bSTRCALC"`: 是/否（布尔值） — Stress• Active/Inactive
- `"FRAME"`: 文字（字符串） — Options• Normal: "NORMAL"• Normal + Concurrent Force/Stress: "AXIAL"
- `"bCSTRCALC"`: 是/否（布尔值） — Combined Stress• Active/Inactive
- ... *还有 21 个参数*

**第 2 层：`MVCTCH.BRIDGE1`** — 34 个参数在这一层

- `"RC_C1L1"`: 数字 — Case 1: L1
- `"RC_C1F1"`: 数字 — Case 1: F1
- `"RC_C1L2"`: 数字 — Case 1: L2
- `"RC_C1F2"`: 数字 — Case 1: F2
- `"RC_bCASE2"`: 是/否（布尔值） — Case II• Active/Inactive
- `"RC_C2L1"`: 数字 — Case 2: L1
- `"RC_C2F1"`: 数字 — Case 2: F1
- `"RC_C2L2"`: 数字 — Case 2: L2
- ... *还有 26 个参数*

**第 3 层：`MVCTCH.BRIDGE2`** — 25 个参数在这一层

- `"ARCH_F"`: 数字 — f
- `"ARCH_L"`: 数字 — Value 2
- `"BTYPE"`: 文字（字符串） — Bridge Type• Passenger-Freight Mixed Line or Heavy Haul Railway Bridge: "RAILWAY"• High Speed or Int
- `"METHOD"`: 文字（字符串） — Sub-Type• Simply Supported or Continous Steel Bridge: "SIMPLE"• Composite Bridge (Steel & Concrete):
- `"SIMPLE_U"`: 数字 — Value 1
- `"SIMPLE_L"`: 数字 — Value 2
- `"COMPO_U"`: 数字 — Value 1
- `"COMPO_L"`: 数字 — Value 2
- ... *还有 17 个参数*

**第 4 层：`MVCTCH.FREQ`** — 23 个参数在这一层

- `"USER_F"`: 文字（字符串） — Frequency
- `"SBEM_L"`: 数字 — Length, L
- `"SBEM_E"`: 数字 — Elastic Modulus, E
- `"SBEM_IC"`: 数字 — Moment Inertia, I
- `"SBEM_MC"`: 数字 — Mass, mc
- `"CBEM_A"`: 数字 — Factor, a
- `"CBEM_B"`: 数字 — Factor, b
- `"CBEM_L"`: 数字 — Length, L
- ... *还有 15 个参数*


### 3. 必填 vs 可选参数

**必填参数**（不填会报错）：

| 参数名 | 类型 | JSON 路径 | 说明 |
|--------|------|-----------|------|
| `POINT` | 文字（字符串） | `MVCTCH.POINT` | Load Point Selection• Influence Line Dependent Point: "INF"• |
| `UNUMT` | 整数 | `MVCTCH.UNUMT` | Number/Line Element• When "iIGP" is 0 |
| `DIST` | 数字 | `MVCTCH.DIST` | Distance between Points• When "iIGP" is 1 |
| `PLATE` | 文字（字符串） | `MVCTCH.PLATE` | Options• Center: "CENTER"• Center + Nodal: "NODAL" |
| `FRAME` | 文字（字符串） | `MVCTCH.FRAME` | Options• Normal: "NORMAL"• Normal + Concurrent Force/Stress: |
| `RGN` | 文字（字符串） | `MVCTCH.RGN` | Structure Group Name• When the "bRG" is true |
| `DGN` | 文字（字符串） | `MVCTCH.DGN` | Structure Group Name• When the "bDG" is true |
| `FGN` | 文字（字符串） | `MVCTCH.FGN` | Boundary Group Name• When the "bLG" is true |
| `LGN` | 文字（字符串） | `MVCTCH.LGN` | Boundary Group Name• When the "bLG" is true |
| `iCODETYPE` | 整数 | `MVCTCH.iCODETYPE` | Code Type• JTG D60-2015/JTG04: 0• Other Codes: 1• TB 10002-2 |
| `iNFM` | 整数 | `MVCTCH.iNFM` | Natural Frequency Method• User Input: 0• Simple Beam: 1• Con |
| `iSLCM` | 整数 | `MVCTCH.iSLCM` | Span Length• Span Length by Lane Input: 0• Loaded Length by  |
| `iBC` | 整数 | `MVCTCH.iBC` | Vehicle Load Class• Class I: 0• Class II: 1 |
| `FREQ` | 对象（一组键值对） | `MVCTCH.FREQ` | Natural Frequency Data |
| `USER_F` | 文字（字符串） | `MVCTCH.FREQ.USER_F` | Frequency |
| `SBEM_L` | 数字 | `MVCTCH.FREQ.SBEM_L` | Length, L |
| `SBEM_E` | 数字 | `MVCTCH.FREQ.SBEM_E` | Elastic Modulus, E |
| `SBEM_IC` | 数字 | `MVCTCH.FREQ.SBEM_IC` | Moment Inertia, I |
| `SBEM_MC` | 数字 | `MVCTCH.FREQ.SBEM_MC` | Mass, mc |
| `CBEM_A` | 数字 | `MVCTCH.FREQ.CBEM_A` | Factor, a |
| `CBEM_B` | 数字 | `MVCTCH.FREQ.CBEM_B` | Factor, b |
| `CBEM_L` | 数字 | `MVCTCH.FREQ.CBEM_L` | Length, L |
| `CBEM_E` | 数字 | `MVCTCH.FREQ.CBEM_E` | Elastic Modulus, E |
| `CBEM_IC` | 数字 | `MVCTCH.FREQ.CBEM_IC` | Moment Inertia, I |
| `CBEM_MC` | 数字 | `MVCTCH.FREQ.CBEM_MC` | Mass, mc |
| `iARCH_TYPE` | 整数 | `MVCTCH.FREQ.iARCH_TYPE` | Arch Bridge• Arch with Uniform Section Rib/General Arch: 0•  |
| `ARCH_N` | 数字 | `MVCTCH.FREQ.ARCH_N` | Factor, n |
| `ARCH_F` | 数字 | `MVCTCH.BRIDGE2.ARCH_F` | f |
| `ARCH_L` | 数字 | `MVCTCH.BRIDGE2.ARCH_L` | Value 2 |
| `ARCH_E` | 数字 | `MVCTCH.FREQ.ARCH_E` | Elastic Modulus, E |
| `ARCH_IC` | 数字 | `MVCTCH.FREQ.ARCH_IC` | Moment Inertia, I |
| `ARCH_MC` | 数字 | `MVCTCH.FREQ.ARCH_MC` | Mass, mc |
| `CABL_A` | 数字 | `MVCTCH.FREQ.CABL_A` | Factor, a |
| `CABL_L` | 数字 | `MVCTCH.FREQ.CABL_L` | Length, L |
| `SUSP_L` | 数字 | `MVCTCH.FREQ.SUSP_L` | Length, L |
| `SUSP_E` | 数字 | `MVCTCH.FREQ.SUSP_E` | Elastic Modulus, E |
| `SUSP_I` | 数字 | `MVCTCH.FREQ.SUSP_I` | Moment Inertia, I |
| `SUSP_HG` | 数字 | `MVCTCH.FREQ.SUSP_HG` | Force, Hg |
| `SUSP_M` | 数字 | `MVCTCH.FREQ.SUSP_M` | Mass, m |
| `BRIDGE1` | 对象（一组键值对） | `MVCTCH.BRIDGE1` | Bridge Data |
| `BTYPE` | 文字（字符串） | `MVCTCH.BRIDGE2.BTYPE` | Bridge Type• Passenger-Freight Mixed Line or Heavy Haul Rail |
| `RC_C1L1` | 数字 | `MVCTCH.BRIDGE1.RC_C1L1` | Case 1: L1 |
| `RC_C1F1` | 数字 | `MVCTCH.BRIDGE1.RC_C1F1` | Case 1: F1 |
| `RC_C1L2` | 数字 | `MVCTCH.BRIDGE1.RC_C1L2` | Case 1: L2 |
| `RC_C1F2` | 数字 | `MVCTCH.BRIDGE1.RC_C1F2` | Case 1: F2 |
| `RC_C2L1` | 数字 | `MVCTCH.BRIDGE1.RC_C2L1` | Case 2: L1 |
| `RC_C2F1` | 数字 | `MVCTCH.BRIDGE1.RC_C2F1` | Case 2: F1 |
| `RC_C2L2` | 数字 | `MVCTCH.BRIDGE1.RC_C2L2` | Case 2: L2 |
| `RC_C2F2` | 数字 | `MVCTCH.BRIDGE1.RC_C2F2` | Case 2: F2 |
| `STL_C1V1` | 数字 | `MVCTCH.BRIDGE1.STL_C1V1` | Case 1: V1 |
| `STL_C1V2` | 数字 | `MVCTCH.BRIDGE1.STL_C1V2` | Case 1: V2 |
| `STL_C2V1` | 数字 | `MVCTCH.BRIDGE1.STL_C2V1` | Case 2: V1 |
| `STL_C2V2` | 数字 | `MVCTCH.BRIDGE1.STL_C2V2` | Case 2: V2 |
| `MBRG_RL1` | 数字 | `MVCTCH.BRIDGE1.MBRG_RL1` | Impact Factor of Lane Loads: L1 |
| `MBRG_RF1` | 数字 | `MVCTCH.BRIDGE1.MBRG_RF1` | Impact Factor of Lane Loads: F1 |
| `MBRG_RL2` | 数字 | `MVCTCH.BRIDGE1.MBRG_RL2` | Impact Factor of Lane Loads: L2 |
| `MBRG_RF2` | 数字 | `MVCTCH.BRIDGE1.MBRG_RF2` | Impact Factor of Lane Loads: F2 |
| `MBRG_RF3` | 数字 | `MVCTCH.BRIDGE1.MBRG_RF3` | Impact Factor of Lane Loads: F3 |
| `MBRG_RF4` | 数字 | `MVCTCH.BRIDGE1.MBRG_RF4` | Impact Factor of Lane Loads: F4 |
| `MBRG_CF1` | 数字 | `MVCTCH.BRIDGE1.MBRG_CF1` | Impact Factor of Vehicle Loads: F1 |
| `MBRG_CF2` | 数字 | `MVCTCH.BRIDGE1.MBRG_CF2` | Impact Factor of Vehicle Loads: F2 |
| `MBRG_CF3` | 数字 | `MVCTCH.BRIDGE1.MBRG_CF3` | Impact Factor of Vehicle Loads: F3 |
| `TRAIN_SUB_TYPE` | 文字（字符串） | `MVCTCH.BRIDGE1.TRAIN_SUB_TYPE` | Sub-Type• Simply Supported or Continuous Steel Bridge: "SIMP |
| `TRAIN_NUMERATOR` | 数字 | `MVCTCH.BRIDGE1.TRAIN_NUMERATOR` | Value 1 |
| `TRAIN_DENOMINATOR` | 数字 | `MVCTCH.BRIDGE1.TRAIN_DENOMINATOR` | Value 2 |
| `TRAIN_H` | 数字 | `MVCTCH.BRIDGE1.TRAIN_H` | Surcharge Thickness |
| `TRAIN_bCLSL` | 整数 | `MVCTCH.BRIDGE1.TRAIN_bCLSL` | Apply Loaded Span Length• Not Consider: 0• Consider: 1 |
| `TRAIN_bALSL` | 整数 | `MVCTCH.BRIDGE1.TRAIN_bALSL` | Apply Loaded Span Length• Not Consider: 0• Consider: 1 |
| `TRAIN_LAMBDA` | 数字 | `MVCTCH.BRIDGE1.TRAIN_LAMBDA` | Lambda |
| `TRAIN_F` | 数字 | `MVCTCH.BRIDGE1.TRAIN_F` | f |
| `TRAIN_GROUP` | 文字（字符串） | `MVCTCH.BRIDGE1.TRAIN_GROUP` | Structure Group Name |
| `BRIDGE2` | 对象（一组键值对） | `MVCTCH.BRIDGE2` | Bridge Data |
| `METHOD` | 文字（字符串） | `MVCTCH.BRIDGE2.METHOD` | Sub-Type• Simply Supported or Continous Steel Bridge: "SIMPL |
| `SIMPLE_U` | 数字 | `MVCTCH.BRIDGE2.SIMPLE_U` | Value 1 |
| `SIMPLE_L` | 数字 | `MVCTCH.BRIDGE2.SIMPLE_L` | Value 2 |
| `COMPO_U` | 数字 | `MVCTCH.BRIDGE2.COMPO_U` | Value 1 |
| `COMPO_L` | 数字 | `MVCTCH.BRIDGE2.COMPO_L` | Value 2 |
| `CONC_U` | 数字 | `MVCTCH.BRIDGE2.CONC_U` | Value 1 |
| `CONC_L` | 数字 | `MVCTCH.BRIDGE2.CONC_L` | Value 2 |
| `CONC_H` | 数字 | `MVCTCH.BRIDGE2.CONC_H` | Surcharge Thickness |
| `ARCH_U` | 数字 | `MVCTCH.BRIDGE2.ARCH_U` | Value 1 |
| `ARCH_LAMBDA` | 数字 | `MVCTCH.BRIDGE2.ARCH_LAMBDA` | Lambda |
| `MU1` | 数字 | `MVCTCH.BRIDGE2.MU1` | Value 1 to Calculate mu |
| `MU2` | 数字 | `MVCTCH.BRIDGE2.MU2` | Value 2 to Calculate mu |
| `MU3` | 数字 | `MVCTCH.BRIDGE2.MU3` | Value 3 to Calculate mu |
| `LFAI` | 数字 | `MVCTCH.BRIDGE2.LFAI` | Lfai• When the "bLFAI" is false |
| `MUR1` | 数字 | `MVCTCH.BRIDGE2.MUR1` | Value 1 to Calculate mu Reduction |
| `MUR2` | 数字 | `MVCTCH.BRIDGE2.MUR2` | Value 2 to Calculate mu Reduction |
| `MUR3` | 数字 | `MVCTCH.BRIDGE2.MUR3` | Value 3 to Calculate mu Reduction |
| `HC` | 数字 | `MVCTCH.BRIDGE2.HC` | Surcharge Thickness |
| `GROUP` | 文字（字符串） | `MVCTCH.BRIDGE2.GROUP` | Structure Group Name |

**可选参数**（填不填都行）：

| 参数名 | 类型 | 默认值 | 说明 |
|--------|------|--------|------|
| `iIGP` | 整数 | `0` | Influence Generating Points• Number/Line Element: 0• Distanc |
| `bSTRCALC` | 是/否（布尔值） | `false` | Stress• Active/Inactive |
| `bCSTRCALC` | 是/否（布尔值） | `false` | Combined Stress• Active/Inactive |
| `bREAC` | 是/否（布尔值） | `false` | Reactions• Active/Inactive |
| `bRG` | 是/否（布尔值） | `false` | Option• All: false• Structure Group: true |
| `bDISP` | 是/否（布尔值） | `false` | Displacements• Active/Inactive |
| `bDG` | 是/否（布尔值） | `false` | Option• All: false• Structure Group: true |
| `bFM` | 是/否（布尔值） | `false` | Elastic/General Links• Active/Inactive |
| `bFG` | 是/否（布尔值） | `false` | Option• All: false• Boundary Group: true |
| `bL` | 是/否（布尔值） | `false` | Elastic/General Links• Active/Inactive |
| `bLG` | 是/否（布尔值） | `false` | Option• All: false• Boundary Group: true |
| `bIF` | 是/否（布尔值） | `false` | Impact Factor• Active/Inactive |
| `bBC` | 是/否（布尔值） | `false` | Vehicle Load Class• Active/Inactive |
| `RC_bCASE2` | 是/否（布尔值） | `false` | Case II• Active/Inactive |
| `RC_GROUP` | 文字（字符串） | `Blank` | Structure Group Name |


### 4. 可选参数放在哪里？

可选参数必须放在正确的 JSON 层级中。以下是每个可选参数的具体位置：

- `iIGP` 的路径：**"MVCTCH" → "iIGP"**
  意思是：在 JSON 中依次打开 MVCTCH, iIGP，最后填入 `iIGP` 的值
- `bSTRCALC` 的路径：**"MVCTCH" → "bSTRCALC"**
  意思是：在 JSON 中依次打开 MVCTCH, bSTRCALC，最后填入 `bSTRCALC` 的值
- `bCSTRCALC` 的路径：**"MVCTCH" → "bCSTRCALC"**
  意思是：在 JSON 中依次打开 MVCTCH, bCSTRCALC，最后填入 `bCSTRCALC` 的值
- `bREAC` 的路径：**"MVCTCH" → "bREAC"**
  意思是：在 JSON 中依次打开 MVCTCH, bREAC，最后填入 `bREAC` 的值
- `bRG` 的路径：**"MVCTCH" → "bRG"**
  意思是：在 JSON 中依次打开 MVCTCH, bRG，最后填入 `bRG` 的值
- `bDISP` 的路径：**"MVCTCH" → "bDISP"**
  意思是：在 JSON 中依次打开 MVCTCH, bDISP，最后填入 `bDISP` 的值
- `bDG` 的路径：**"MVCTCH" → "bDG"**
  意思是：在 JSON 中依次打开 MVCTCH, bDG，最后填入 `bDG` 的值
- `bFM` 的路径：**"MVCTCH" → "bFM"**
  意思是：在 JSON 中依次打开 MVCTCH, bFM，最后填入 `bFM` 的值
- `bFG` 的路径：**"MVCTCH" → "bFG"**
  意思是：在 JSON 中依次打开 MVCTCH, bFG，最后填入 `bFG` 的值
- `bL` 的路径：**"MVCTCH" → "bL"**
  意思是：在 JSON 中依次打开 MVCTCH, bL，最后填入 `bL` 的值

**理解 JSON 路径**：想象你在文件夹里找文件——`A.B.C` 就像 `A文件夹/B文件夹/C文件`。


### 5. 参数之间的关系

以下参数之间存在关联关系：

- `POINT` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `iIGP` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `PLATE` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `FRAME` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `bRG` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `bDG` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `bFG` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `bLG` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `iCODETYPE` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `iNFM` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `iSLCM` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `iBC` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `iARCH_TYPE` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `BTYPE` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `RC_C1L1` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `RC_C1F1` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `RC_C1L2` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `RC_C1F2` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `RC_C2L1` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `RC_C2F1` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `RC_C2L2` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `RC_C2F2` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `STL_C1V1` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `STL_C1V2` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `STL_C2V1` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `STL_C2V2` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `MBRG_RL1` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `MBRG_RF1` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `MBRG_RL2` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `MBRG_RF2` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `MBRG_RF3` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `MBRG_RF4` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `MBRG_CF1` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `MBRG_CF2` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `MBRG_CF3` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `TRAIN_SUB_TYPE` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `TRAIN_bCLSL` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `TRAIN_bALSL` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `METHOD` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `bCHECK` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `bLFAI` 有多个可选值（见参数表），不同取值会影响后续参数的需求
- `bLENGTH` 有多个可选值（见参数表），不同取值会影响后续参数的需求

**一般规律**：`TYPE` 类参数决定结构类型，然后 `PARAM` 类参数的格式由 `TYPE` 决定。


### 6. 最小可运行代码

以下是能跑起来的最简代码：

```python
import requests
import urllib3
urllib3.disable_warnings()  # 关闭 SSL 警告

# MIDAS 服务地址（根据你的产品修改端口）
BASE = "https://127.0.0.1:1102"

url = f"{BASE}/db/MVCTch"

# JSON 数据 — 这是你要发给 MIDAS 的内容
data = {
#     "MVCTCH": {
#         "POINT": "<POINT>",
#         "UNUMT": 0,
#         "DIST": 0,
#         "PLATE": "<PLATE>",
#         "FRAME": "<FRAME>",
#         "RGN": "<RGN>",
#         "DGN": "<DGN>",
#         "FGN": "<FGN>",
#         "LGN": "<LGN>",
#         "iCODETYPE": 0,
#         "iNFM": 0,
#         "iSLCM": 0,
#         "iBC": 0,
#         "FREQ": {
#             "USER_F": "<USER_F>",
#             "SBEM_L": 0,
#             "SBEM_E": 0,
#             "SBEM_IC": 0,
#             "SBEM_MC": 0,
#             "CBEM_A": 0,
#             "CBEM_B": 0,
#             "CBEM_L": 0,
#             "CBEM_E": 0,
#             "CBEM_IC": 0,
#             "CBEM_MC": 0,
#             "iARCH_TYPE": 0,
#             "ARCH_N": 0,
#             "ARCH_E": 0,
#             "ARCH_IC": 0,
#             "ARCH_MC": 0,
#             "CABL_A": 0,
#             "CABL_L": 0,
#             "SUSP_L": 0,
#             "SUSP_E": 0,
#             "SUSP_I": 0,
#             "SUSP_HG": 0,
#             "SUSP_M": 0
#         },
#         "BRIDGE2": {
#             "METHOD": "<METHOD>",
#             "SIMPLE_U": 0,
#             "SIMPLE_L": 0,
#             "COMPO_U": 0,
#             "COMPO_L": 0,
#             "CONC_U": 0,
#             "CONC_L": 0,
#             "CONC_H": 0,
#             "ARCH_U": 0,
#             "ARCH_LAMBDA": 0,
#             "MU1": 0,
#             "MU2": 0,
#             "MU3": 0,
#             "LFAI": 0,
#             "MUR1": 0,
#             "MUR2": 0,
#             "MUR3": 0,
#             "HC": 0,
#             "GROUP": "<GROUP>"
#         },
#         "BRIDGE1": {
#             "RC_C1L1": 0,
#             "RC_C1F1": 0,
#             "RC_C1L2": 0,
#             "RC_C1F2": 0,
#             "RC_C2L1": 0,
#             "RC_C2F1": 0,
#             "RC_C2L2": 0,
#             "RC_C2F2": 0,
#             "STL_C1V1": 0,
#             "STL_C1V2": 0,
#             "STL_C2V1": 0,
#             "STL_C2V2": 0,
#             "MBRG_RL1": 0,
#             "MBRG_RF1": 0,
#             "MBRG_RL2": 0,
#             "MBRG_RF2": 0,
#             "MBRG_RF3": 0,
#             "MBRG_RF4": 0,
#             "MBRG_CF1": 0,
#             "MBRG_CF2": 0,
#             "MBRG_CF3": 0,
#             "TRAIN_SUB_TYPE": "<TRAIN_SUB_TYPE>",
#             "TRAIN_NUMERATOR": 0,
#             "TRAIN_DENOMINATOR": 0,
#             "TRAIN_H": 0,
#             "TRAIN_bCLSL": 0,
#             "TRAIN_bALSL": 0,
#             "TRAIN_LAMBDA": 0,
#             "TRAIN_F": 0,
#             "TRAIN_GROUP": "<TRAIN_GROUP>"
#         }
#     }
# }

# 发送请求
r = requests.post(url, json=data, verify=False)

# 检查结果
if r.status_code == 200:
    print("成功！")
    print(r.json())
else:
    print(f"失败，错误码：{r.status_code}")
```

**运行前确认**：MIDAS Civil 已经打开，并且加载了一个项目。


### 7. 工程意义

参数化建模的核心。一旦掌握，你可以用几十行代码代替几小时的点鼠标操作。参数变化时，重新生成模型只需要几秒钟。

### 8. 常见错误

使用这个接口时最容易犯的错误：

1. **忘记填必填参数**：POINT、UNUMT、DIST、PLATE、FRAME、RGN、DGN、FGN、LGN、iCODETYPE、iNFM、iSLCM、iBC、FREQ、USER_F、SBEM_L、SBEM_E、SBEM_IC、SBEM_MC、CBEM_A、CBEM_B、CBEM_L、CBEM_E、CBEM_IC、CBEM_MC、iARCH_TYPE、ARCH_N、ARCH_F、ARCH_L、ARCH_E、ARCH_IC、ARCH_MC、CABL_A、CABL_L、SUSP_L、SUSP_E、SUSP_I、SUSP_HG、SUSP_M、BRIDGE1、BTYPE、RC_C1L1、RC_C1F1、RC_C1L2、RC_C1F2、RC_C2L1、RC_C2F1、RC_C2L2、RC_C2F2、STL_C1V1、STL_C1V2、STL_C2V1、STL_C2V2、MBRG_RL1、MBRG_RF1、MBRG_RL2、MBRG_RF2、MBRG_RF3、MBRG_RF4、MBRG_CF1、MBRG_CF2、MBRG_CF3、TRAIN_SUB_TYPE、TRAIN_NUMERATOR、TRAIN_DENOMINATOR、TRAIN_H、TRAIN_bCLSL、TRAIN_bALSL、TRAIN_LAMBDA、TRAIN_F、TRAIN_GROUP、BRIDGE2、METHOD、SIMPLE_U、SIMPLE_L、COMPO_U、COMPO_L、CONC_U、CONC_L、CONC_H、ARCH_U、ARCH_LAMBDA、MU1、MU2、MU3、LFAI、MUR1、MUR2、MUR3、HC、GROUP 是必填的，漏掉任何一个都会报错。
2. **JSON 层级放错**：这个接口有 4 个层级，参数放错层级就不会生效。注意看每个参数的 `json_path`。
4. **URL 写错**：确认路径是 `/db/MVCTch`——多一个斜杠或少一个都会导致 404 错误。


### 9. Python 批量生成案例

如果你需要创建多个类似的调用（例如创建 100 个节点），可以用列表+循环来生成：

```python
import requests
import urllib3
urllib3.disable_warnings()

BASE = "https://127.0.0.1:1102"

# 定义基础数据模板
def make_data(**kwargs):
    """根据参数生成 Moving Load Analysis Control - China 的 JSON 数据。"""
    data = {"MVCTCH": {"POINT": "<POINT>", "UNUMT": 0, "DIST": 0, "PLATE": "<PLATE>", "FRAME": "<FRAME>", "RGN": "<RGN>", "DGN": "<DGN>", "FGN": "<FGN>", "LGN": "<LGN>", "iCODETYPE": 0, "iNFM": 0, "iSLCM": 0, "iBC": 0, "FREQ": {"USER_F": "<USER_F>", "SBEM_L": 0, "SBEM_E": 0, "SBEM_IC": 0, "SBEM_MC": 0, "CBEM_A": 0, "CBEM_B": 0, "CBEM_L": 0, "CBEM_E": 0, "CBEM_IC": 0, "CBEM_MC": 0, "iARCH_TYPE": 0, "ARCH_N": 0, "ARCH_E": 0, "ARCH_IC": 0, "ARCH_MC": 0, "CABL_A": 0, "CABL_L": 0, "SUSP_L": 0, "SUSP_E": 0, "SUSP_I": 0, "SUSP_HG": 0, "SUSP_M": 0}, "BRIDGE2": {"METHOD": "<METHOD>", "SIMPLE_U": 0, "SIMPLE_L": 0, "COMPO_U": 0, "COMPO_L": 0, "CONC_U": 0, "CONC_L": 0, "CONC_H": 0, "ARCH_U": 0, "ARCH_LAMBDA": 0, "MU1": 0, "MU2": 0, "MU3": 0, "LFAI": 0, "MUR1": 0, "MUR2": 0, "MUR3": 0, "HC": 0, "GROUP": "<GROUP>"}, "BRIDGE1": {"RC_C1L1": 0, "RC_C1F1": 0, "RC_C1L2": 0, "RC_C1F2": 0, "RC_C2L1": 0, "RC_C2F1": 0, "RC_C2L2": 0, "RC_C2F2": 0, "STL_C1V1": 0, "STL_C1V2": 0, "STL_C2V1": 0, "STL_C2V2": 0, "MBRG_RL1": 0, "MBRG_RF1": 0, "MBRG_RL2": 0, "MBRG_RF2": 0, "MBRG_RF3": 0, "MBRG_RF4": 0, "MBRG_CF1": 0, "MBRG_CF2": 0, "MBRG_CF3": 0, "TRAIN_SUB_TYPE": "<TRAIN_SUB_TYPE>", "TRAIN_NUMERATOR": 0, "TRAIN_DENOMINATOR": 0, "TRAIN_H": 0, "TRAIN_bCLSL": 0, "TRAIN_bALSL": 0, "TRAIN_LAMBDA": 0, "TRAIN_F": 0, "TRAIN_GROUP": "<TRAIN_GROUP>"}}}
    # 在这里修改需要变化的值
    for key, value in kwargs.items():
        # 根据 json_path 更新对应位置的值
        pass  # 具体逻辑见下面的 for 循环例子
    return data

# 批量调用
results = []
for i in range(1, 11):  # 生成 10 个
    data = make_data()    # 在这里修改参数
    r = requests.post(f"{BASE}/db/MVCTch", json=data, verify=False)
    results.append(r.json())
    print(f'第 {i} 个完成')
```


### 10. for 循环优化案例

对于批量操作，直接写 for 循环每次发一个请求效率不够高。以下是优化技巧：

**技巧 1：利用 Assign 结构一次发送多个对象**

很多 DB 接口支持在一次请求中发送多个对象，通过 `Assign` 下的编号 `"1"`, `"2"`, ... 区分。

```python
# ❌ 慢：循环 100 次，每次发一个节点
for i in range(100):
    data = {"Assign": {"1": {"X": i, "Y": 0, "Z": 0}}}
    requests.post(url, json=data, verify=False)

# ✅ 快：一次发 100 个节点
nodes = {}
for i in range(100):
    nodes[str(i+1)] = {"X": i, "Y": 0, "Z": 0}
data = {"Assign": nodes}
requests.post(url, json=data, verify=False)
```

**技巧 2：使用列表推导式预生成数据**（在 Moving Load Analysis Control - China 中适用）

```python
# 列表推导式 — 一行代码生成所有节点的坐标
nodes = {str(i+1): {"X": i*5.0, "Y": 0, "Z": 0} for i in range(100)}
data = {"Assign": nodes}
requests.post(url, json=data, verify=False)
```

**通用优化原则**：

1. 能一次发多个就不要循环发单个
2. 用 `requests.Session()` 代替 `requests.post()` 做批量请求
3. 先生成所有数据，再统一发送，不要在循环里逐个生成+发送



---

### Moving Load Analysis Control - India — `/db/MVCTid`

**方法**: POST, GET, PUT, DELETE | **参数**: 9 必填 + 20 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `UNUMT` | 整数 | **是** | Number/Line Element• When "iIGP" is 0 |
| `DIST` | 数字 | **是** | Distance between Points• When "iIGP" is 1 |
| `PLATE` | 文字（字符串） | **是** | Options• Center: "CENTER"• Center + Nodal: "NODAL" |
| `FRAME` | 文字（字符串） | **是** | Options• Normal: "NORMAL"• Normal + Concurrent Force/Stress: "AXIAL" |
| `FGP` | 文字（字符串） | **是** | Structure Group Name• When the "bFG" is true |
| `LGP` | 文字（字符串） | **是** | Boundary Group Name• When the "bLG" is true |
| `VHMAX` | 整数 | **是** | Maximum Successive Vehicles |
| `RGN` | 文字（字符串） | **是** | Structure Group Name• When the "bRG" is true |
| `DGN` | 文字（字符串） | **是** | Structure Group Name• When the "bDG" is true |
| `iIGP` | 整数 | 否 | Influence Generating Points• Number/Line Element: 0• Distance between Points: 1 |
| `bSTRCALC` | 是/否（布尔值） | 否 | Stress• Active/Inactive |
| `bCSTRCALC` | 是/否（布尔值） | 否 | Combined Stress• Active/Inactive |
| `bREAC` | 是/否（布尔值） | 否 | Reactions• Active/Inactive |
| `bRGP` | 是/否（布尔值） | 否 | AllorGroup |
| `RGP` | 文字（字符串） | 否 | Groupname |
| `bDISP` | 是/否（布尔值） | 否 | Displacements• Active/Inactive |
| `bDGP` | 是/否（布尔值） | 否 | AllorGroup |
| `DGP` | 文字（字符串） | 否 | Groupname |
| `bFM` | 是/否（布尔值） | 否 | Forces/Moments• Active/Inactive |
| ... | ... | ... | *还有 10 个可选参数* |

**最简 JSON**：
```json
{
  "MVCTID": {
    "UNUMT": 0,
    "DIST": 0,
    "PLATE": "<PLATE>",
    "FRAME": "<FRAME>",
    "FGP": "<FGP>",
    "LGP": "<LGP>",
    "VHMAX": 0
  },
  "RGN": "<RGN>",
  "DGN": "<DGN>"
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "iIGP": 0,
      "UNUMT": 3,
      "PLATE": "NODAL",
      "bSTRCALC": true,
      "FRAME": "AXIAL",
      "bCSTRCALC": true,
      "bREAC": true,
      "bRGP": false,
      "RGP": "",
      "bDISP": true,
      "bDGP": false,
      "DGP": "",
      "bFM": true,
      "bFGP": false,
      "FGP": "",
      "bL": true,
      "bLG": false,
      "LGP": "",
      "BRIDGE": 0,
      "TRACKS": 0,
      "WIDTHTYPE": 0,
      "WIDTH": 0,
      "DEPTH": 10,
      "VHMAX": 10
    }
  }
}
```


---

### Moving Load Analysis Control - BS — `/db/MVCTbs`

**方法**: POST, GET, PUT, DELETE | **参数**: 8 必填 + 14 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `UNUMT` | 整数 | **是** | Number/Line Element• When "iIGP" is 0 |
| `DIST` | 数字 | **是** | Distance between Points• When "iIGP" is 1 |
| `PLATE` | 文字（字符串） | **是** | Options• Center: "CENTER"• Center + Nodal: "NODAL" |
| `FRAME` | 文字（字符串） | **是** | Options• Normal: "NORMAL"• Normal + Concurrent Force/Stress: "AXIAL" |
| `RGP` | 文字（字符串） | **是** | Structure Group Name• When the "bRG" is true |
| `DGP` | 文字（字符串） | **是** | Structure Group Name• When the "bDP" is true |
| `FGP` | 文字（字符串） | **是** | Structure Group Name• When the "bFG" is true |
| `LGP` | 文字（字符串） | **是** | Boundary Group Name• When the "bLG" is true |
| `iIGP` | 整数 | 否 | Influence Generating Points• Number/Line Element: 0• Distance between Points: 1 |
| `bSTRCALC` | 是/否（布尔值） | 否 | Stress• Active/Inactive |
| `bCONCURRENT` | 是/否（布尔值） | 否 | Concurrent Force• Active/Inactive |
| `bCSTRCALC` | 是/否（布尔值） | 否 | Combined Stress• Active/Inactive |
| `bREAC` | 是/否（布尔值） | 否 | Reactions• Active/Inactive |
| `bRGP` | 是/否（布尔值） | 否 | Option• All: false• Structure Group: true |
| `bDISP` | 是/否（布尔值） | 否 | Displacements• Active/Inactive |
| `bDGP` | 是/否（布尔值） | 否 | AllorGroup |
| `bFM` | 是/否（布尔值） | 否 | Forces/Moments• Active/Inactive |
| `bFGP` | 是/否（布尔值） | 否 | Option• All: false• Structure Group: true |
| ... | ... | ... | *还有 4 个可选参数* |

**最简 JSON**：
```json
{
  "MVCTBS": {
    "UNUMT": 0,
    "DIST": 0,
    "PLATE": "<PLATE>",
    "FRAME": "<FRAME>",
    "RGP": "<RGP>",
    "DGP": "<DGP>",
    "FGP": "<FGP>",
    "LGP": "<LGP>"
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "iIGP": 0,
      "UNUMT": 3,
      "PLATE": "NODAL",
      "bSTRCALC": true,
      "bCONCURRENT": true,
      "FRAME": "AXIAL",
      "bCSTRCALC": true,
      "bREAC": true,
      "bRGP": false,
      "RGP": "",
      "bDISP": true,
      "bDGP": false,
      "DGP": "",
      "bFM": true,
      "bFGP": false,
      "FGP": "",
      "bL": true,
      "bLG": false,
      "LGP": "",
      "NUMLANE": 0
    }
  }
}
```


---

### Moving Load Analysis Control - Transverse — `/db/MVCTtr`

**方法**: POST, GET, PUT, DELETE | **参数**: 4 必填 + 5 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `LOAD_POINT_SEL` | 整数 | **是** | Load Point Selection• Influence Line Dependent Point: 1• All Point: 2 |
| `NUM_UNIT_LOAD` | 整数 | **是** | Number/Line Element• When "INFL_GEN_POINT" is 0 |
| `DISTANCE` | 数字 | **是** | Distance between Points• When "INFL_GEN_POINT" is 1 |
| `ANALYSIS_RESULT` | 整数 | **是** | Analysis Results Type• Normal: 1• Normal + Concurrent Force/Stress: 2 |
| `INFL_GEN_POINT` | 整数 | 否 | Influence Generation Method• Number/Line Element: 0• Distance between Points: 1 |
| `OPT_COMBINED_STR` | 是/否（布尔值） | 否 | Combined Stress• Active/Inactive |
| `OPT_REACTIONS` | 是/否（布尔值） | 否 | Reactions• Active/Inactive |
| `OPT_DISPLACEMENTS` | 是/否（布尔值） | 否 | Displacement• Active/Inactive |
| `OPT_FORCE` | 是/否（布尔值） | 否 | Forces/Moments• Active/Inactive |

**最简 JSON**：
```json
{
  "MVCTTR": {
    "LOAD_POINT_SEL": 0,
    "NUM_UNIT_LOAD": 0,
    "DISTANCE": 0,
    "ANALYSIS_RESULT": 0
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "LOAD_POINT_SEL": 1,
      "INFL_GEN_POINT": 0,
      "NUM_UNIT_LOAD": 3,
      "ANALYSIS_RESULT": 2,
      "OPT_COMBINED_STR": true,
      "OPT_REACTIONS": true,
      "OPT_DISPLACEMENTS": true,
      "OPT_FORCE": false
    }
  }
}
```


---

### Settlement Analysis Control Data — `/db/SMCT`

**方法**: POST, GET, PUT, DELETE | **参数**: 0 必填 + 2 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `CONCURRENT_CALC` | 是/否（布尔值） | 否 | Plate Concurrent Force• Active: true• Inactive: false |
| `CONCURRENT_LINK` | 是/否（布尔值） | 否 | Elastic / General Links Concurrent Force• Active: true• Inactive: false |

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "CONCURRENT_CALC": true,
      "CONCURRENT_LINK": false
    }
  }
}
```


---

### Nonlinear Analysis Control Data — `/db/NLCT`

**方法**: POST, GET, PUT, DELETE | **参数**: 11 必填 + 8 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NUMBER_STEPS` | 整数 | **是** | Number of Displacement Steps |
| `MAX_ITERATIONS` | 数字 | **是** | Maximum Number of Iterations/Load Step |
| `MASTER_NODE` | 整数 | **是** | Master Node ID Number |
| `MAXIMUM_DISPLACEMENT` | 数字 | **是** | Maximum Displacement |
| `ENERGY_NORM` | 数字 | **是** | Energy Norm |
| `DISPLACEMENT_NORM` | 数字 | **是** | Displacement Norm |
| `FORCE_NORM` | 数字 | **是** | Force Norm |
| `NEWTON_ITEMS` | Array[Object] | **是** | Load Case Specific Nonlinear Analysis Control Data - Newton-Raphson• Insert the  |
| `ARCLEN_ITEMS` | Array[Object] | **是** | Load Case Specific Nonlinear Analysis Control Data - Arc-Length• Insert the data |
| `DISPCT_ITEMS` | Array[Object] | **是** | Load Case Specific Nonlinear Analysis Control Data - Displacement-Control• Inser |
| `LCNAME` | 文字（字符串） | **是** | Load Case Name |
| `NONLINEAR_TYPE` | 文字（字符串） | 否 | Nonlinear Type• Geometry Nonlinear: "GEOM"• Material Nonlinear: "MATL"• Geometry |
| `ITERATION_METHOD` | 文字（字符串） | 否 | Iteration Method• Newton-Raphson: "DISP" |
| `INITIAL_FORCE_RATIO_ARC_LEN` | 数字 | 否 | Initial Force Ratio for Unit Arc-Length |
| `DIRECTION` | 整数 | 否 | Direction• Dx: 0• Dy: 1• Dz: 2 |
| `OPT_ENERGY_NORM` | 是/否（布尔值） | 否 | Energy Norm• Active/Inactive |
| `OPT_DISPLACEMENT_NORM` | 是/否（布尔值） | 否 | Displacement Norm• Active/Inactive |
| `OPT_FORCE_NORM` | 是/否（布尔值） | 否 | Force Norm• Active/Inactive |
| `LOAD_FACTORS` | 数字数组 | 否 | Master Node Displacement• Index: Step |

**最简 JSON**：
```json
{
  "NLCT": {
    "NUMBER_STEPS": 0,
    "MAX_ITERATIONS": 0,
    "MASTER_NODE": 0,
    "MAXIMUM_DISPLACEMENT": 0,
    "ENERGY_NORM": 0,
    "DISPLACEMENT_NORM": 0,
    "FORCE_NORM": 0,
    "NEWTON_ITEMS": [],
    "ARCLEN_ITEMS": [],
    "DISPCT_ITEMS": [],
    "properties": {
      "NEWTON_ITEMS": {
        "items": {
          "properties": {
            "LCNAME": "<LCNAME>"
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "NONLINEAR_TYPE": "GEOM+MATL",
      "ITERATION_METHOD": "NEWTON",
      "NUMBER_STEPS": 1,
      "MAX_ITERATIONS": 30,
      "OPT_ENERGY_NORM": true,
      "ENERGY_NORM": 0.001,
      "OPT_DISPLACEMENT_NORM": true,
      "DISPLACEMENT_NORM": 0.001,
      "OPT_FORCE_NORM": true,
      "FORCE_NORM": 0.001,
      "NEWTON_ITEMS": [
        {
          "ITERATION_METHOD": "NEWTON",
          "LCNAME": "A",
          "NUMBER_STEPS": 1,
          "MAX_ITERATIONS": 30,
          "LOAD_FACTORS": [
            1
          ]
        }
      ],
      "DISPCT_ITEMS": [
        {
          "ITERATION_METHOD": "DISP",
          "LCNAME": "B",
          "NUMBER_STEPS": 1,
          "MAX_ITERATIONS": 10,
          "MASTER_NODE": 1,
          "DIRECTION": 0,
          "MAXIMUM_DISPLACEMENT": 0.1,
          "LOAD_FACTORS": [
            1
          ]
        }
      ]
    }
  }
}
```


---

### Nonlinear Analysis Control — `/db/NLCT-M1ᴴˢ⁾`

**方法**: GET, PUT, DELETE | **参数**: 11 必填 + 13 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `LOAD_CASE` | 文字（字符串） | **是** | Load Case Name |
| `NONLINEAR_TYPE` | string (enum) | **是** | Geometry Nonlinear• Geometry: GEOM• Material: MATL• Geometry + Material: GEOM_MA |
| `ITER_METHOD` | string (enum) | **是** | Iteration Method• Force Control: FORCE• Arc-Length: ARC• Displacement Control: D |
| `LOAD_STEPS` | 对象（一组键值对） | **是** | Load step configuration |
| `STEP_MODE` | string (enum) | **是** | Load Steps• Number of Increments: AUTO• User Defined Step: MANUAL |
| `NUMBER_STEPS` | 整数 | **是** | Number of Increments |
| `MANUAL_STEPS` | Array | **是** | Load Step |
| `MIN_ARC_RATIO` | 数字 | **是** | Min Arc-Length Adjustment Ratio |
| `MASTER_NODE` | 整数 | **是** | Master Node |
| `OPT_USE` | 是/否（布尔值） | **是** | Use Work Convergence |
| `CONV_CRITERIA` | 对象（一组键值对） | **是** | Convergence criteria |
| `LC_SCOPE` | string (enum) | 否 | Nonlinear Analysis Type• Global: ALL• Load Case: SELECT |
| `OUTPUT` | string (enum) | 否 | Intermediate Output Request• Every Increment: EVERY• Last Increment: LAST |
| `MAX_ARC_RATIO` | 数字 | 否 | Max Arc-Length Adjustment Ratio |
| `MAX_ARC_INCREMENTS` | 整数 | 否 | Max Arc-Length Increments |
| `MAX_DISP` | 数字 | 否 | Maximum Displacement |
| `DIRECTION` | string (enum) | 否 | Direction• DX: DX• DY: DY• DZ: DZ |
| `REF_NODE` | 对象（一组键值对） | 否 | Reference Node |
| `NODE` | 整数 | 否 | Reference Node Number |
| `DISP` | 对象（一组键值对） | 否 | Displacement Convergence |
| `VALUE` | 数字 | 否 | Work ToleranceWhen OPT_USE=true |
| ... | ... | ... | *还有 3 个可选参数* |

**最简 JSON**：
```json
{
  "LOAD_CASE": "<LOAD_CASE>",
  "NONLINEAR_TYPE": {},
  "ITER_METHOD": {},
  "LOAD_STEPS": {},
  "STEP_MODE": {},
  "NUMBER_STEPS": 0,
  "MANUAL_STEPS": [],
  "MIN_ARC_RATIO": 0,
  "MASTER_NODE": 0,
  "OPT_USE": true,
  "CONV_CRITERIA": {}
}
```


---

### Construction Stage Analysis Control Data — `/db/STCT`

**方法**: POST, GET, PUT, DELETE | **参数**: 7 必填 + 59 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `FINAL_STAGE` | 文字（字符串） | **是** | Construction Stage Name• When "bLAST_FINAL" is false |
| `GROUP` | 文字（字符串） | **是** | Structure Group Name for Initial Tangent Displacement• When the "ITD" is "GROUP" |
| `LFFGR` | 文字（字符串） | **是** | Structure Group Name• When the "bLFFC" is True |
| `vSDLE` | 字符串数组 | **是** | Load Case Name List(Grid Analysis Load) |
| `LTYPECC` | 文字（字符串） | **是** | Erection Load Case Name |
| `EREC` | 文字（字符串） | **是** | Load Type for C.S.⁴⁾ |
| `vLCNAME` | 字符串数组 | **是** | Load Case Name List |
| `bLAST_FINAL` | 是/否（布尔值） | 否 | Final Stage Option• Last Stage: true• Other Stage: false |
| `CPFC` | 文字（字符串） | 否 | Cable-Pretensions Force Type• Internal Force: "INTERNAL"• External Force: "EXTER |
| `bEXT_REPL` | 是/否（布尔值） | 否 | External Force Type• Add: false• Replace: true |
| `bCALC_CFF` | 是/否（布尔值） | 否 | Calculate Concurrent Forces of Frame |
| `bCALC_CSP` | 是/否（布尔值） | 否 | Calculate Output of Each Part of Composite Section |
| `bAPPLY_IMF` | 是/否（布尔值） | 否 | Apply Initial Member Force to C.S. |
| `bCONV` | 是/否（布尔值） | 否 | Convert Final Stage Member Forces to Initial Forces for Post C.S. |
| `bTRUSS` | 是/否（布尔值） | 否 | Truss• When the "bCONV" is true |
| `bBEAM` | 是/否（布尔值） | 否 | Beam• When the "bCONV" is true |
| `bITD` | 是/否（布尔值） | 否 | Initial Tangent Displacement for Erected Structures |
| ... | ... | ... | *还有 49 个可选参数* |

**最简 JSON**：
```json
{
  "STCT": {
    "FINAL_STAGE": "<FINAL_STAGE>",
    "GROUP": "<GROUP>",
    "LFFGR": "<LFFGR>",
    "vSDLE": "<vSDLE>",
    "properties": {
      "vEREC": {
        "items": {
          "properties": {
            "LTYPECC": "<LTYPECC>",
            "EREC": "<EREC>",
            "vLCNAME": "<vLCNAME>"
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "bLAST_FINAL": false,
      "FINAL_STAGE": "CS1",
      "iINC_NLA": 0,
      "iNLA_TYPE": 0,
      "bINC_PDL": true,
      "iITER": 30,
      "TOL": 0.01,
      "vEREC": [
        {
          "LTYPECC": "Erection Load 1",
          "EREC": "D",
          "vLCNAME": [
            "A",
            "B"
          ]
        },
        {
          "LTYPECC": "Erection Load 2",
          "EREC": "DC",
          "vLCNAME": [
            "C"
          ]
        }
      ],
      "CPFC": "EXTERNAL",
      "bCONV": true,
      "bTRUSS": true,
      "bBEAM": true,
      "bCHANGE_CABLE": true,
      "bAPPLY_IMF": true,
      "bCAMBER": true,
      "bSD": true,
      "iSDOPT": 1,
      "SDCONST": 1,
      "iBSC": 0
    }
  }
}
```


---

### Construction Stage Analysis Control Data — `/db/STCT-M1ᴴˢ⁾`

**方法**: GET, PUT, DELETE | **参数**: 9 必填 + 36 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `bLAST_FINAL` | 是/否（布尔值） | **是** | Final Stage |
| `FINAL_STAGE` | 文字（字符串） | **是** | Stage Name |
| `RESTART_STAGE` | Array | **是** | Array of construction stage names to restart |
| `LTYPECC` | 文字（字符串） | **是** | Erection Load Case Name |
| `EREC` | string (enum) | **是** | Erection Load Type for C.S.• Dead: D• Dead Component: DC• Dead Wearing: DW• Erec |
| `vLCNAME` | Array | **是** | Load Case Name List |
| `vSDLE` | Array | **是** | Load Case Name List |
| `iSDOPT` | integer (enum) | **是** | Stress decrease method• Linear Interpolation: 0• Constant: 1 |
| `SDCONST` | 数字 | **是** | Ratio Value for Constant Type |
| `RESTART_CS_ANAL` | 对象（一组键值对） | 否 | Restart Construction Stage Analysis |
| `OPT_USE` | 是/否（布尔值） | 否 | Use Option |
| `ERECTION_LOAD` | array[object] | 否 | Load Cases to be Distinguished from Dead Load for C.S. Output |
| `iBSC` | integer (enum) | 否 | Beam Section Property Changes• Constant: 0• Change: 1 |
| `ANAL_TYPE` | 对象（一组键值对） | 否 | Analysis Type Object |
| `iINC_NLA` | integer (enum) | 否 | Analysis type• No NL: 0• Geometric NL: 1• Material NL: 2• Geo + Mat NL: 3 |
| `iNLA_TYPE` | integer (enum) | 否 | Stage option• Independent Stage: 0• Accumulative Stage: 1When iINC_NLA is 2 or 3 |
| `bIEMF` | 是/否（布尔值） | 否 | Include Equilibrium Element Nodal Forces |
| `bINC_PDL` | 是/否（布尔值） | 否 | Include P-Delta Effect |
| `bINC_TDE` | 是/否（布尔值） | 否 | Include Time Dependent Effect |
| ... | ... | ... | *还有 26 个可选参数* |

**最简 JSON**：
```json
{
  "bLAST_FINAL": true,
  "FINAL_STAGE": "<FINAL_STAGE>",
  "RESTART_STAGE": [],
  "LTYPECC": "<LTYPECC>",
  "EREC": {},
  "vLCNAME": [],
  "vSDLE": [],
  "iSDOPT": {},
  "SDCONST": 0
}
```


---

### Boundary Change Assignment — `/db/BCCT`

**方法**: POST, GET, PUT, DELETE | **参数**: 5 必填 + 11 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `vBOUNDARY` | Array[Object] | **是** | Boundary List• Insert the data as an object |
| `BGCNAME` | 文字（字符串） | **是** | Boundary Group Combination name |
| `vBG` | 文字（字符串） | **是** | Boundary Group List |
| `TYPE` | 文字（字符串） | **是** | Load Cases & Analysis• Static load Case: "ST"• Unlisted Analysis Types: "ULAT"•  |
| `LCNAME` | 文字（字符串） | **是** | Static Load Case |
| `bSPT` | 是/否（布尔值） | 否 | Support |
| `bSPR` | 是/否（布尔值） | 否 | Point Spring Support |
| `bGSPR` | 是/否（布尔值） | 否 | General Spring Support |
| `bCGLINK` | 是/否（布尔值） | 否 | Change General Link Property |
| `bSSSF` | 是/否（布尔值） | 否 | Section Stiffness Scale Factor |
| `bWSSF` | 是/否（布尔值） | 否 | Wall Stiffness Scale Factor |
| `bPSSF` | 是/否（布尔值） | 否 | Plate Stiffness Scale Factor |
| `bRLS` | 是/否（布尔值） | 否 | Beam End Release |
| `bESSF` | 是/否（布尔值） | 否 | Element Stiffness Scale Factor |
| `bCDOF` | 是/否（布尔值） | 否 | Constrain DOF associated with specified displacements / Settlements by boundary  |
| ... | ... | ... | *还有 1 个可选参数* |

**最简 JSON**：
```json
{
  "BCCT": {
    "vBOUNDARY": [],
    "properties": {
      "vBOUNDARY": {
        "items": {
          "properties": {
            "BGCNAME": "<BGCNAME>",
            "vBG": "<vBG>"
          }
        }
      },
      "vLOADANAL": {
        "items": {
          "properties": {
            "TYPE": "<TYPE>",
            "LCNAME": "<LCNAME>"
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "bSPT": true,
      "bSPR": true,
      "bGSPR": false,
      "bCGLINK": false,
      "bSSSF": true,
      "bPSSF": false,
      "bRLS": true,
      "bCDOF": false,
      "vBOUNDARY": [
        {
          "BGCNAME": "BGL1",
          "vBG": [
            "BG1",
            "BG2"
          ]
        }
      ],
      "vLOADANAL": [
        {
          "TYPE": "ST",
          "BGCNAME": "BGL1",
          "LCNAME": "LC1"
        },
        {
          "TYPE": "ST",
          "BGCNAME": "BGL1",
          "LCNAME": "LC2"
        },
        {
          "TYPE": "ST",
          "BGCNAME": "BGL1",
          "LCNAME": "LC3"
        },
        {
          "TYPE": "ST",
          "BGCNAME": "BGL1",
          "LCNAME": "LC4"
        }
      ]
    }
  }
}
```


---

### Define Boundary Combination — `/db/BCGD-M1ᴴˢ⁾`

**方法**: POST, GET, PUT, DELETE | **参数**: 2 必填 + 0 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `BCG_NAME` | 文字（字符串） | **是** | Boundary Combination Name |
| `GROUP_LIST` | Array | **是** | Boundary Group List |

**最简 JSON**：
```json
{
  "BCG_NAME": "<BCG_NAME>",
  "GROUP_LIST": []
}
```


---

### Assign Boundary Combination — `/db/BCGA-M1ᴴˢ⁾`

**方法**: POST, GET, PUT, DELETE | **参数**: 4 必填 + 1 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `BC_ASSIGN` | array [object] | **是** | Assign Boundary Combination to Analyses & Load Cases |
| `ANAL_TYPE` | string (enum) | **是** | ANAL_TYPE• Static Load Case: ST• Moving Load (): MV• Static Modal (): SM• Eigenv |
| `LCNAME` | 文字（字符串） | **是** | Load Case Name |
| `BC_SELECT` | Array | **是** | Select Boundary Conditions for Boundary Change |
| `BGCNAME` | 文字（字符串） | 否 | Boundary Combination Name |

**最简 JSON**：
```json
{
  "BC_ASSIGN": [],
  "ANAL_TYPE": {},
  "LCNAME": "<LCNAME>",
  "BC_SELECT": []
}
```


---

### Load Combinations - General — `/db/LCOM-GEN`

**方法**: POST, GET, PUT, DELETE | **参数**: 5 必填 + 5 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Combination Name |
| `vCOMB` | Array[Object] | **是** | Combinations List |
| `ANAL` | 文字（字符串） | **是** | • Static Load Case: "ST"• Construction Stage Case: "CS"• Moving Load Case: "MV"• |
| `LCNAME` | 文字（字符串） | **是** | Load Case Name |
| `FACTOR` | 数字 | **是** | Factor |
| `NO` | 整数 | 否 | Combination Number |
| `ACTIVE` | 文字（字符串） | 否 | Active Type• Inactive: "INACTIVE"• Active: "ACTIVE" |
| `iTYPE` | 整数 | 否 | Summation method• Add: 0• Envelope: 1• ABS: 2• SRSS: 3 |
| `DESC` | 文字（字符串） | 否 | Description |
| `bCB` | 是/否（布尔值） | 否 | Result Type• General: false• Min/Max/All: true |

**最简 JSON**：
```json
{
  "NAME": "<NAME>",
  "vCOMB": [],
  "ANAL": "<ANAL>",
  "LCNAME": "<LCNAME>",
  "FACTOR": 0
}
```

**官方示例**：
```json
"{\n    \"Assign\": {\n        \"1\": {"
```


---

### Load Combinations - Concrete Design — `/db/LCOM-CONC`

**方法**: POST, GET, PUT, DELETE | **参数**: 5 必填 + 6 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Combination Name |
| `vCOMB` | Array[Object] | **是** | Combinations List |
| `ANAL` | 文字（字符串） | **是** | • Static Load Case: "ST"• Construction Stage Case: "CS"• Moving Load Case: "MV"• |
| `LCNAME` | 文字（字符串） | **是** | Load Case Name |
| `FACTOR` | 数字 | **是** | Factor |
| `NO` | 整数 | 否 | Combination Number |
| `ACTIVE` | 文字（字符串） | 否 | Active Type• Inactive: "INACTIVE"• Active: "ACTIVE" |
| `iTYPE` | 整数 | 否 | Summation method• Add: 0• Envelope: 1• ABS: 2• SRSS: 3 |
| `bES` | 是/否（布尔值） | 否 | Concrete Design Option |
| `DESC` | 文字（字符串） | 否 | Description |
| `bCB` | 是/否（布尔值） | 否 | Result Type• General: false• Min/Max/All: true |

**最简 JSON**：
```json
{
  "NAME": "<NAME>",
  "vCOMB": [],
  "ANAL": "<ANAL>",
  "LCNAME": "<LCNAME>",
  "FACTOR": 0
}
```

**官方示例**：
```json
"{\n    \"Assign\": {\n        \"1\": {"
```


---

### Load Combinations - Steel Design — `/db/LCOM-STEEL`

**方法**: POST, GET, PUT, DELETE | **参数**: 5 必填 + 5 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Combination Name |
| `vCOMB` | Array[Object] | **是** | Combinations List |
| `ANAL` | 文字（字符串） | **是** | • Static Load Case: "ST"• Construction Stage Case: "CS"• Moving Load Case: "MV"• |
| `LCNAME` | 文字（字符串） | **是** | Load Case Name |
| `FACTOR` | 数字 | **是** | Factor |
| `NO` | 整数 | 否 | Combination Number |
| `ACTIVE` | 文字（字符串） | 否 | Active Type• Inactive: "INACTIVE"• Strength/Stress: "STRENGTH"• Serviceability:  |
| `iTYPE` | 整数 | 否 | Summation method• Add: 0• Envelope: 1• SRSS: 3 |
| `DESC` | 文字（字符串） | 否 | Description |
| `bCB` | 是/否（布尔值） | 否 | Result Type• General: false• Min/Max/All: true |

**最简 JSON**：
```json
{
  "NAME": "<NAME>",
  "vCOMB": [],
  "ANAL": "<ANAL>",
  "LCNAME": "<LCNAME>",
  "FACTOR": 0
}
```

**官方示例**：
```json
"{\n    \"Assign\": {\n        \"1\": {"
```


---

### Load Combinations - SRC Design — `/db/LCOM-SRC`

**方法**: POST, GET, PUT, DELETE | **参数**: 5 必填 + 5 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Combination Name |
| `vCOMB` | Array[Object] | **是** | Combinations List |
| `ANAL` | 文字（字符串） | **是** | • Static Load Case: "ST"• Construction Stage Case: "CS"• Moving Load Case: "MV"• |
| `LCNAME` | 文字（字符串） | **是** | Load Case Name |
| `FACTOR` | 数字 | **是** | Factor |
| `NO` | 整数 | 否 | Combination Number |
| `ACTIVE` | 文字（字符串） | 否 | Active Type• Inactive: "INACTIVE"• Strength/Stress: "STRENGTH"• Serviceability:  |
| `iTYPE` | 整数 | 否 | Summation method• Add: 0• Envelope: 1• SRSS: 3 |
| `DESC` | 文字（字符串） | 否 | Description |
| `bCB` | 是/否（布尔值） | 否 | Result Type• General: false• Min/Max/All: true |

**最简 JSON**：
```json
{
  "NAME": "<NAME>",
  "vCOMB": [],
  "ANAL": "<ANAL>",
  "LCNAME": "<LCNAME>",
  "FACTOR": 0
}
```

**官方示例**：
```json
"{\n    \"Assign\": {\n        \"1\": {"
```


---

### Load Combinations - Composite Steel Girder Design — `/db/LCOM-STLCOMP`

**方法**: POST, GET, PUT, DELETE | **参数**: 5 必填 + 5 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Combination Name |
| `vCOMB` | Array[Object] | **是** | Combinations List |
| `ANAL` | 文字（字符串） | **是** | • Static Load Case: "ST"• Construction Stage Case: "CS"• Moving Load Case: "MV"• |
| `LCNAME` | 文字（字符串） | **是** | Load Case Name |
| `FACTOR` | 数字 | **是** | Factor |
| `NO` | 整数 | 否 | Combination Number |
| `ACTIVE` | 文字（字符串） | 否 | Active Type• Inactive: "INACTIVE"• Strength/Stress: "STRENGTH"• Serviceability:  |
| `iTYPE` | 整数 | 否 | Summation method• Add: 0• Envelope: 1• SRSS: 3 |
| `DESC` | 文字（字符串） | 否 | Description |
| `bCB` | 是/否（布尔值） | 否 | Result Type• General: false• Min/Max/All: true |

**最简 JSON**：
```json
{
  "NAME": "<NAME>",
  "vCOMB": [],
  "ANAL": "<ANAL>",
  "LCNAME": "<LCNAME>",
  "FACTOR": 0
}
```

**官方示例**：
```json
"{\n    \"Assign\": {\n        \"1\": {"
```


---

### Load Combinations - Seismic Design — `/db/LCOM-SEISMIC`

**方法**: POST, GET, PUT, DELETE | **参数**: 5 必填 + 5 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Combination Name |
| `vCOMB` | Array[Object] | **是** | Combinations List |
| `ANAL` | 文字（字符串） | **是** | • Static Load Case: "ST"• Construction Stage Case: "CS"• Moving Load Case: "MV"• |
| `LCNAME` | 文字（字符串） | **是** | Load Case Name |
| `FACTOR` | 数字 | **是** | Factor |
| `NO` | 整数 | 否 | Combination Number |
| `ACTIVE` | 文字（字符串） | 否 | Active Type• Inactive: "INACTIVE"• Active: "ACTIVE" |
| `iTYPE` | 整数 | 否 | Summation method• Add: 0• Envelope: 1• SRSS: 3 |
| `DESC` | 文字（字符串） | 否 | Description |
| `bCB` | 是/否（布尔值） | 否 | Result Type• General: false• Min/Max/All: true |

**最简 JSON**：
```json
{
  "NAME": "<NAME>",
  "vCOMB": [],
  "ANAL": "<ANAL>",
  "LCNAME": "<LCNAME>",
  "FACTOR": 0
}
```

**官方示例**：
```json
"{\n    \"Assign\": {\n        \"1\": {"
```


---

### Cutting Line — `/db/CUTL`

**方法**: POST, GET, PUT, DELETE | **参数**: 8 必填 + 4 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Name of Cutting Line |
| `DIR` | 文字（字符串） | **是** | Direction• Normal: "NORMAL"• In Plane: "DIR" |
| `PT1X` | 数字 | **是** | Point 1 - X |
| `PT1Y` | 数字 | **是** | Point 1 - Y |
| `PT1Z` | 数字 | **是** | Point 1 - Z |
| `PT2X` | 数字 | **是** | Point 2 - X |
| `PT2Y` | 数字 | **是** | Point 2 - Y |
| `PT2Z` | 数字 | **是** | Point 2 - Z |
| `R` | 整数 | 否 | Line Color• Red |
| `G` | 整数 | 否 | Line Color• Green |
| `B` | 整数 | 否 | Line Color• Blue |
| `TYPE` | 整数 | 否 | Type |

**最简 JSON**：
```json
{
  "CUTL": {
    "NAME": "<NAME>",
    "DIR": "<DIR>",
    "PT1X": 0,
    "PT1Y": 0,
    "PT1Z": 0,
    "PT2X": 0,
    "PT2Y": 0,
    "PT2Z": 0
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "NAME": "Cut-Line#1",
      "DIR": "NORMAL",
      "PT1X": 8.95,
      "PT1Y": 11.0725,
      "PT1Z": 1.205,
      "PT2X": 8.95,
      "PT2Y": -1.0725,
      "PT2Z": 1.205,
      "R": 255,
      "G": 0,
      "B": 0,
      "TYPE": 0
    }
  }
}
```


---

### Plate Cutting Line Diagram — `/db/CLWP`

**方法**: POST, GET, PUT, DELETE | **参数**: 11 必填 + 3 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Name of Cutting Line |
| `DIR` | 文字（字符串） | **是** | Direction• Normal: "NORMAL"• In Plane: "DIR" |
| `PT1X` | 数字 | **是** | Point 1 - X |
| `PT1Y` | 数字 | **是** | Point 1 - Y |
| `PT1Z` | 数字 | **是** | Point 1 - Z |
| `PT2X` | 数字 | **是** | Point 2 - X |
| `PT2Y` | 数字 | **是** | Point 2 - Y |
| `PT2Z` | 数字 | **是** | Point 2 - Z |
| `PT3X` | 数字 | **是** | Point 3 - X |
| `PT3Y` | 数字 | **是** | Point 3 - Y |
| `PT3Z` | 数字 | **是** | Point 3 - Z |
| `R` | 整数 | 否 | Line Color• Red |
| `G` | 整数 | 否 | Line Color• Green |
| `B` | 整数 | 否 | Line Color• Blue |

**最简 JSON**：
```json
{
  "CLWP": {
    "NAME": "<NAME>",
    "DIR": "<DIR>",
    "PT1X": 0,
    "PT1Y": 0,
    "PT1Z": 0,
    "PT2X": 0,
    "PT2Y": 0,
    "PT2Z": 0,
    "PT3X": 0,
    "PT3Y": 0,
    "PT3Z": 0
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "NAME": "CL1",
      "DIR": "PLANE",
      "PT1X": 0,
      "PT1Y": 10710,
      "PT1Z": -1000,
      "PT2X": 0,
      "PT2Y": 10710,
      "PT2Z": 0,
      "PT3X": 0,
      "PT3Y": 9945,
      "PT3Z": 0,
      "R": 0,
      "G": 0,
      "B": 0
    }
  }
}
```


---

### Bridge Girder Diagrams — `/db/GSBG`

**方法**: POST, GET, PUT, DELETE | **参数**: 3 必填 + 7 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Group Name |
| `BATCH` | 是/否（布尔值） | **是** | Batch |
| `BODY_ELEM_GRUP_K` | 整数 | **是** | Bridge Girder Element Group |
| `ALLSTAGE` | 是/否（布尔值） | 否 | Generation Option• Current Stage-Step: false• Stages(Last Step): true |
| `BSTRSCOMP` | 整数 | 否 | Beam Stresses Components• Sax: 0• +Sby: 1• -Sby: 2• +Sbz: 3• -Sbz: 4• Combined:  |
| `BSTRSCOMP_SUB` | 整数 | 否 | Location for the Display of Stress• When Beam Stresses Components is 7th DOF• Ma |
| `MOMENT_COMP` | 整数 | 否 | Beam Forces/Moments Components• Fx: 0• Fy: 1• Fz: 2• Mx: 3• My: 4• Mz: 5• Mb: 6• |
| `_7TH_DOF_TYPE` | 整数 | 否 | 7th DOF Type• When Beam Stresses Components is 7th DOF• Sax(Warping): 0• Ssy(Mt) |
| `DGRM_TYPE` | 整数 | 否 | Type of Result• Beam Stresses: 0• Beam Forces/Moments: 1 |
| `SCALEFACTOR` | 数字 | 否 | Scale |

**最简 JSON**：
```json
{
  "GSBG": {
    "NAME": "<NAME>",
    "BATCH": true,
    "BODY_ELEM_GRUP_K": 0
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "NAME": "Dgrm Group1",
      "BATCH": true,
      "BODY_ELEM_GRUP_K": 1,
      "ALLSTAGE": false,
      "DGRM_TYPE": 0,
      "BSTRSCOMP": 6,
      "BSTRSCOMP_SUB": 3,
      "_7TH_DOF_TYPE": 0,
      "SCALEFACTOR": 1
    }
  }
}
```


---

### General Camber Control — `/db/GCMB`

**方法**: POST, GET, PUT, DELETE | **参数**: 3 必填 + 1 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `GCMB_BASE_ITEMS` | Array[Object] | **是** | General Camber Base Items• Insert data as object |
| `GRUP_NAME` | 文字（字符串） | **是** | Structure Group Name |
| `DIRECTION` | 文字（字符串） | **是** | Direction• "+DX"• "-DX"• "+DY"• "-DY" |
| `bSTART_PT_ZERO` | 是/否（布尔值） | 否 | Set Start Point Zero |

**最简 JSON**：
```json
{
  "GCMB": {
    "GCMB_BASE_ITEMS": [],
    "properties": {
      "GCMB_BASE_ITEMS": {
        "items": {
          "properties": {
            "GRUP_NAME": "<GRUP_NAME>",
            "DIRECTION": "<DIRECTION>"
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "bSTART_PT_ZERO": true,
      "GCMB_BASE_ITEMS": [
        {
          "GRUP_NAME": "CS_0",
          "DIRECTION": "+DX"
        },
        {
          "GRUP_NAME": "CS_1",
          "DIRECTION": "+DX"
        },
        {
          "GRUP_NAME": "CS_2",
          "DIRECTION": "+DX"
        },
        {
          "GRUP_NAME": "CS_3",
          "DIRECTION": "+DX"
        },
        {
          "GRUP_NAME": "CS_4",
          "DIRECTION": "+DX"
        },
        {
          "GRUP_NAME": "CS_5",
          "DIRECTION": "+DX"
        },
        {
          "GRUP_NAME": "CS_6",
          "DIRECTION": "+DX"
        },
        {
          "GRUP_NAME": "CS_7",
          "DIRECTION": "+DX"
        },
        {
          "GRUP_NAME": "CS_8",
          "DIRECTION": "+DX"
        },
        {
          "GRUP_NAME": "CS_9",
          "DIRECTION": "+DX"
        },
        {
          "GRUP_NAME": "CS_10",
          "DIRECTION": "+DX"
        },
        {
          "GRUP_NAME": "CS_11",
          "DIRECTION": "+DX"
        },
        {
          "GRUP_NAME": "CS_12",
          "DIRECTION": "+DX"
        },
        {
          "GRUP_NAME": "CS_14",
          "DIRECTION": "+DX"
        },
        {
          "GRUP_NAME": "CS_15",
          "DIRECTION": "+DX"
        },
        {
          "GRUP_NAME": "CS_16",
          "DIRECTION": "+DX"
        },
        {
          "GRUP_NAME": "CS_17",
          "DIRECTION": "+DX"
        },
        {
          "GRUP_NAME": "CS_18",
          "DIRECTION": "+DX"
        },
        {
          "GRUP_NAME": "CS_13",
          "DIRECTION": "+DX"
        }
      ]
    }
  }
}
```


---

### FCM Camber Control — `/db/CAMB`

**方法**: POST, GET, PUT, DELETE | **参数**: 3 必填 + 0 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `BODY_GROUP_NAME` | 文字（字符串） | **是** | Bridge Girder Element Group |
| `SUPP_GROUP_NAME` | 文字（字符串） | **是** | Support Node Group |
| `KEYSEG_GROUP_NAME` | 文字（字符串） | **是** | Key Segment Element Group |

**最简 JSON**：
```json
{
  "CAMB": {
    "BODY_GROUP_NAME": "<BODY_GROUP_NAME>",
    "SUPP_GROUP_NAME": "<SUPP_GROUP_NAME>",
    "KEYSEG_GROUP_NAME": "<KEYSEG_GROUP_NAME>"
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "BODY_GROUP_NAME": "FSM",
      "SUPP_GROUP_NAME": "PSC-BN",
      "KEYSEG_GROUP_NAME": "Key-SegK1~K5"
    }
  }
}
```


---

### Cable Control - Unknown Load Factor Constraints — `/db/ULFC`

**方法**: POST, GET, PUT, DELETE | **参数**: 8 必填 + 5 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Constraint Name |
| `TYPE` | 文字（字符串） | **是** | Constraint Type• Reaction: "REAC"• Displacement: "DISP"• Truss Force: "TRUSS"• B |
| `OBJ_ID` | 整数 | **是** | Element/Node ID |
| `POINT` | 整数 | **是** | Point• When "TYPE" is Beam Force◦ I-end: 0◦ 1/4: 1◦ 2/4: 2◦ 3/4: 3◦ J-end: 4 |
| `COMP` | 整数 | **是** | Component• Reaction & Beam Force/Displacement/Truss◦ FX/DX/I-end: 0◦ FY/DY/J-end |
| `VALUE` | 数字 | **是** | Value Double |
| `UB_VALUE` | 数字 | **是** | Upper Bound Value |
| `LB_VALUE` | 数字 | **是** | Lower Bound Value |
| `EQ` | 是/否（布尔值） | 否 | Equality/Inequality Condition• Equality: true• Inequality: false |
| `bVALUE` | 是/否（布尔值） | 否 | Check Value |
| `OtherObject` | 整数 | 否 | Other Object• When "bValue" is False |
| `bUB` | 是/否（布尔值） | 否 | Check Upper Bound |
| `bLB` | 是/否（布尔值） | 否 | Check Lower Bound |

**最简 JSON**：
```json
{
  "ULFC": {
    "NAME": "<NAME>",
    "TYPE": "<TYPE>",
    "OBJ_ID": 0,
    "POINT": 0,
    "COMP": 0,
    "VALUE": 0,
    "UB_VALUE": 0,
    "LB_VALUE": 0
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "2": {
      "NAME": "Ele-03",
      "TYPE": "BEAM",
      "OBJ_ID": 3,
      "POINT": 1,
      "COMP": 4,
      "EQ": false,
      "bUB": true,
      "UB_VALUE": -220,
      "bLB": true,
      "LB_VALUE": -230
    },
    "3": {
      "NAME": "Node-07",
      "TYPE": "REAC",
      "OBJ_ID": 7,
      "POINT": 4,
      "COMP": 1,
      "EQ": true,
      "bVALUE": true,
      "VALUE": 500,
      "OtherObject": 0
    },
    "4": {
      "NAME": "Ele-11",
      "TYPE": "DISP",
      "OBJ_ID": 11,
      "POINT": 4,
      "COMP": 2,
      "EQ": false,
      "bUB": true,
      "UB_VALUE": -0.05,
      "bLB": true,
      "LB_VALUE": 0.05
    },
    "5": {
      "NAME": "Ele-15",
      "TYPE": "BEAM",
      "OBJ_ID": 15,
      "POINT": 4,
      "COMP": 0,
      "EQ": false,
      "bUB": true,
      "UB_VALUE": -240,
      "bLB": true,
      "LB_VALUE": -250
    },
    "6": {
      "NAME": "Ele-19",
      "TYPE": "BEAM",
      "OBJ_ID": 19,
      "POINT": 4,
      "COMP": 4,
      "EQ": false,
      "bUB": true,
      "UB_VALUE": -170,
      "bLB": true,
      "LB_VALUE": -180
    },
    "7": {
      "NAME": "Node106",
      "TYPE": "DISP",
      "OBJ_ID": 106,
      "POINT": 0,
      "COMP": 0,
      "EQ": false,
      "bUB": true,
      "UB_VALUE": 0.0001,
      "bLB": true,
      "LB_VALUE": -0.0001
    }
  }
}
```


---

### Time History Graph - Element Force Smart Graph — `/db/THRE`

**方法**: POST, GET, PUT, DELETE | **参数**: 3 必填 + 5 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `THIS_NAME` | 文字（字符串） | **是** | Time History Load Cases |
| `PROPERTY_KEY` | 整数 | **是** | Element No. |
| `THIS_ELEMENT` | 整数 | **是** | Type of Element• Beam: 0• Truss: 1• Wall: 2 |
| `TYPE_ELEMENT` | 整数 | 否 | Type of Element |
| `STORY_NAME` | 文字（字符串） | 否 | Name of Story• When "THIS_ELEMENT" is 2 (Wall) |
| `TYPE_RES` | 整数 | 否 | Type of Result• Force: 0 |
| `LOCATION` | 整数 | 否 | Location• I-end/Top: 0• J-end/Bottom : 1 |
| `COMP` | 整数 | 否 | Component• Axial: 0• Shear-y: 1• Shear-z: 2• Torsion: 3• Moment-y: 4• Moment-z:  |

**最简 JSON**：
```json
{
  "THRE": {
    "THIS_NAME": "<THIS_NAME>",
    "PROPERTY_KEY": 0
  },
  "THIS_ELEMENT": 0
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "THIS_NAME": "HIST1",
      "TYPE_ELEMENT": 0,
      "PROPERTY_KEY": 102,
      "STORY_NAME": "",
      "TYPE_RES": 0,
      "LOCATION": 0,
      "COMP": 0
    }
  }
}
```


---

### Time History Graph - General Link Smart Graph — `/db/THRG`

**方法**: POST, GET, PUT, DELETE | **参数**: 2 必填 + 3 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `THIS_NAME` | 文字（字符串） | **是** | Name |
| `GENERAL_LINK` | 整数 | **是** | General Link Number |
| `TYPE_RES` | 整数 | 否 | Type of Result• Force-Deformation: 0• Force: 1• Deformation: 2 |
| `LOCATION` | 整数 | 否 | Location• i-end: 0• j-end: 1 |
| `COMP` | 整数 | 否 | Component• Force-Deformation/Force/Deformation◦ Fx-Dx / Fx / Dx: 0◦ Fy-Dy / Fy / |

**最简 JSON**：
```json
{
  "THRG": {
    "THIS_NAME": "<THIS_NAME>",
    "GENERAL_LINK": 0
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "THIS_NAME": "HIST1",
      "TYPE_RES": 0,
      "LOCATION": 0,
      "COMP": 0,
      "GENERAL_LINK": 1
    },
    "2": {
      "THIS_NAME": "HIST1",
      "TYPE_RES": 0,
      "LOCATION": 0,
      "COMP": 0,
      "GENERAL_LINK": 4
    }
  }
}
```


---

### Time History Graph - Inelastic Hinge Smart Graph — `/db/THRI`

**方法**: POST, GET, PUT, DELETE | **参数**: 2 必填 + 5 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `THIS_NAME` | 文字（字符串） | **是** | Name |
| `PROPERTY_KEY` | 整数 | **是** | Select Element |
| `TYPE_ELEMENT` | 整数 | 否 | Type of Element• Beam: 0• Truss: 1• General Link: 3 |
| `STORY_NAME` | 文字（字符串） | 否 | Name of Story |
| `TYPE_RES` | 整数 | 否 | Type of Result• Force-Deformation: 0• Force: 1• Deformation: 2 |
| `LOCATION` | 整数 | 否 | Location• 1-Pos: 0• 2-Pos: 1• 3-Pos: 2 |
| `COMP` | 整数 | 否 | Component• Force-Deformation/Force/Deformation◦ Fx-Dx / Fx / Dx: 0◦ Fy-Dy / Fy / |

**最简 JSON**：
```json
{
  "THRI": {
    "THIS_NAME": "<THIS_NAME>",
    "PROPERTY_KEY": 0
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "THIS_NAME": "HIST1",
      "TYPE_ELEMENT": 0,
      "PROPERTY_KEY": 2101,
      "STORY_NAME": "",
      "TYPE_RES": 0,
      "LOCATION": 0,
      "COMP": 0
    },
    "2": {
      "THIS_NAME": "HIST1",
      "TYPE_ELEMENT": 0,
      "PROPERTY_KEY": 2137,
      "STORY_NAME": "",
      "TYPE_RES": 1,
      "LOCATION": 1,
      "COMP": 0
    },
    "3": {
      "THIS_NAME": "HIST1",
      "TYPE_ELEMENT": 0,
      "PROPERTY_KEY": 2184,
      "STORY_NAME": "",
      "TYPE_RES": 2,
      "LOCATION": 1,
      "COMP": 4
    }
  }
}
```


---

### Time History Graph - Seismic Devices Smart Graph — `/db/THRS`

**方法**: POST, GET, PUT, DELETE | **参数**: 2 必填 + 2 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `THIS_NAME` | 文字（字符串） | **是** | Name |
| `GENERAL_LINK` | 整数 | **是** | General Link Number |
| `TYPE_RES` | 整数 | 否 | Type of Result• Force-Deformation: 0• Force: 2• Deformation: 3• Ductility Factor |
| `COMP` | 整数 | 否 | Component |

**最简 JSON**：
```json
{
  "THRS": {
    "THIS_NAME": "<THIS_NAME>",
    "GENERAL_LINK": 0
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "THIS_NAME": "HIST1",
      "TYPE_RES": 0,
      "COMP": 0,
      "GENERAL_LINK": 1
    },
    "2": {
      "THIS_NAME": "HIST1",
      "TYPE_RES": 2,
      "COMP": 1,
      "GENERAL_LINK": 4
    },
    "3": {
      "THIS_NAME": "HIST1",
      "TYPE_RES": 4,
      "COMP": 2,
      "GENERAL_LINK": 4
    }
  }
}
```


---

### Heat of Hydaration Result Graph — `/db/HHND`

**方法**: POST, GET, PUT, DELETE | **参数**: 3 必填 + 2 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NAME` | 文字（字符串） | **是** | Name |
| `NODE_KEY` | 整数 | **是** | Node Number |
| `ELEM_KEY` | 整数 | **是** | Element Number |
| `COMP` | 整数 | 否 | Stress Component• Sig-xx: 0• Sig-yy: 1• Sig-zz: 2• Max(P1,P2,P3): 3• Sig-P1: 4•  |
| `TYPE` | 整数 | 否 | Type• Select Node: 0• Select Element: 1 |

**最简 JSON**：
```json
{
  "HHND": {
    "NAME": "<NAME>",
    "NODE_KEY": 0,
    "ELEM_KEY": 0
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "NAME": "N1476-X",
      "NODE_KEY": 1476,
      "COMP": 100,
      "TYPE": 0,
      "ELEM_KEY": 0
    },
    "2": {
      "NAME": "N1988-X",
      "NODE_KEY": 1988,
      "COMP": 0,
      "TYPE": 0,
      "ELEM_KEY": 0
    },
    "3": {
      "NAME": "N2308-X",
      "NODE_KEY": 2308,
      "COMP": 0,
      "TYPE": 0,
      "ELEM_KEY": 0
    },
    "4": {
      "NAME": "N2818-X",
      "NODE_KEY": 2818,
      "COMP": 0,
      "TYPE": 0,
      "ELEM_KEY": 0
    }
  }
}
```


---

### Pushover Analysis Control Data — `/db/POGD`

**方法**: POST, GET, PUT, DELETE | **参数**: 51 必填 + 22 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `NONL_OPT` | 对象（一组键值对） | **是** | Nonlinear Analysis Option |
| `SUBSTEP` | 整数 | **是** | Max Num. of Substeps |
| `MAXITER` | 整数 | **是** | Maximum Iteration |
| `bCONSREBARAREA1D` | 是/否（布尔值） | **是** | Reinforcement Area• Active/Inactive |
| `BEAM_CORE_SIZE` | 文字（字符串） | **是** | Core Areas Size Type• Auto Size: "AUTO"• Equal Size: "EQUAL" |
| `BEAM_CORE_DIV_Y` | 整数 | **是** | Core Division (y-dir) |
| `BEAM_CORE_DIV_Z` | 整数 | **是** | Core Division (z-dir) |
| `BEAM_COVER_SIZE` | 文字（字符串） | **是** | Cover Areas Size Type• Auto Size: "AUTO"• Equal Size: "EQUAL" |
| `BEAM_COVER_DIV_Y` | 整数 | **是** | Cover Division (y-dir) |
| `BEAM_COVER_DIV_Z` | 整数 | **是** | Cover Division (z-dir) |
| `bCONSREBARAREAWALL` | 是/否（布尔值） | **是** | Reinforcement Area• Active/Inactive |
| `bWALLCONSOUT` | 是/否（布尔值） | **是** | Consider Out-of-plane Nonlinearity of Plate Type |
| `WALL_CORE_SIZE` | 文字（字符串） | **是** | Core Fiber Areas Size Type• Auto Size: "AUTO"• Equal Size: "EQUAL" |
| `WALL_CORE_DIV_Z` | 整数 | **是** | Core Division (z-dir) |
| `WALL_CORE_DIV_Y` | 整数 | **是** | Core Division (y-dir) |
| `WALL_COVER_SIZE` | 文字（字符串） | **是** | Cover Areas Size Type• Auto Size: "AUTO"• Equal Size: "EQUAL" |
| `WALL_COVER_DIV_Z` | 整数 | **是** | Cover Division (z-dir) |
| `WALL_COVER_DIV_Y` | 整数 | **是** | Cover Division (y-dir) |
| `SHEAR_R` | 整数 | **是** | Spring Shear |
| `bASSIGNBYMEMBER` | 是/否（布尔值） | **是** | Assign Hinge Properties to Member only for Moment-Rotation Beam/Column• Active/I |
| `bTRI_SYM` | 是/否（布尔值） | **是** | Trilinear Default Stiffness Reduction Symmetrical• Active/Inactive |
| `TRI_TENS_A1` | 数字 | **是** | Trilinear Default Stiffness Reduction - Tens. α1 |
| `TRI_TENS_A2` | 数字 | **是** | Trilinear Default Stiffness Reduction - Tens. α2 |
| `TRI_COMP_A1` | 数字 | **是** | Trilinear Default Stiffness Reduction - Comp. α1 |
| `TRI_COMP_A2` | 数字 | **是** | Trilinear Default Stiffness Reduction - Comp. α2 |
| `bBI_SYM` | 是/否（布尔值） | **是** | Bilinear Default Stiffness Reduction Symmetrical• Active/Inactive |
| `BI_TENS_A1` | 数字 | **是** | Bilinear Default Stiffness Reduction - Tens. α1 |
| `BI_COMP_A1` | 数字 | **是** | Bilinear Default Stiffness Reduction - Comp. α1 |
| `PSPR_APPLY_TYPE` | 文字（字符串） | **是** | Point Spring Support Apply Type• "APPLY"• "ASSUME" |
| `ELNK_APPLY_TYPE` | 文字（字符串） | **是** | Elastic Link Apply Type• "APPLY"• "ASSUME" |
| `bUSEAUTOCALCREFERENCE` | 是/否（布尔值） | **是** | Reference Code/Manual for Auto-Calculation• Active/Inactive |
| `RCDGNCODE` | 文字（字符串） | **是** | RC Reference Design Code• "KISTEC2019"• "KISTEC2013"• "MOE2019"• "MOE2018"• "AIK |
| `LOC_BEAM` | 文字（字符串） | **是** | Reference Location of Beam/Distributed Hinges• I-End: "I"• J-End: "J"• Center: " |
| `LOC_COLUMN` | 文字（字符串） | **是** | Reference Location of Column |
| `SF_WALL` | 数字 | **是** | Scale Factor for Ultimate Rotation - Wall Scale Factor |
| `bSF_BRITTLE` | 是/否（布尔值） | **是** | Scale Factor for Ultimate Rotation - Use Brittle Scale Factor |
| `SF_BRITTLE` | 数字 | **是** | Scale Factor for Ultimate Rotation - Brittle Scale Factor |
| `bSF_EARTHQUAKE` | 是/否（布尔值） | **是** | Scale Factor for Ultimate Rotation - Use Earthquake Scale Factor |
| `SF_EARTHQUAKE` | 数字 | **是** | Scale Factor for Ultimate Rotation - Earthquake Scale Factor |
| `bSF_SMOOTH_BAR` | 是/否（布尔值） | **是** | Scale Factor for Ultimate Rotation - Use Smooth bar Scale Factor |
| `SF_SMOOTH_BAR` | 文字（字符串） | **是** | Scale Factor for Ultimate Rotation - Smooth bar Scale Factor |
| `SND_SEIS_GRUP` | 文字（字符串） | **是** | Secondary Seismic Elements Group Name |
| `CONFIDENCE` | 数字 | **是** | Confidence Factor |
| `bBUCKLING` | 是/否（布尔值） | **是** | Calculation Yield Surface of Beam considering Buckling |
| `bCALCAXIALFORCE` | 是/否（布尔值） | **是** | Calc Mc Considering Axial Force (AIJ) |
| `NODECONNECTIVITY` | 文字（字符串） | **是** | Wall Node Connectivity• Pinned: "PINNED"• Fixed: "FIXED" |
| `bSHOWGRAPHAFTER` | 是/否（布尔值） | **是** | Show Pushover Curve Result After Analysis• Active/Inactive |
| `bSHOWGRAPGHDURING` | 是/否（布尔值） | **是** | Show Pushover Curve during Analysis• Active/Inactive |
| `LC_NAME` | 文字（字符串） | **是** | Load Case Name |
| `LC_TYPE` | 文字（字符串） | **是** | Load Case Type |
| `SF` | 数字 | **是** | Scale Factor |
| `GEOMNONLINEAR_TYPE` | 文字（字符串） | 否 | Geometric Nonlinearity Type• None: "NONE"• Large Displacements: "LARGE_DISP" |
| `INITLOADMETHOD` | 文字（字符串） | 否 | Initial Load• Perform Nonlinear Static Analysis: "PERFORM_ANAL"• Import Static/C |
| `INITLOAD` | Array[Object] | 否 | Initial Load Case List• Insert the data as an object |
| `bCONSIGNOREELEM` | 是/否（布尔值） | 否 | Consider Ignore Elements for NL. Analysis Initial Load• When Initial Load is Per |
| `bPERMITFAIL` | 是/否（布尔值） | 否 | Permit Convergence Failure |
| `bDISPLNORM` | 是/否（布尔值） | 否 | Displacement Norm• Active/Inactive |
| `bFORCENORM` | 是/否（布尔值） | 否 | Force Norm• Active/Inactive |
| `bENERGYNORM` | 是/否（布尔值） | 否 | Energy Norm• Active/Inactive |
| `DISPLNORM` | 数字 | 否 | Displacement Norm |
| `FORCENORM` | 数字 | 否 | Force Norm |
| ... | ... | ... | *还有 12 个可选参数* |

**最简 JSON**：
```json
{
  "POGD": {
    "NONL_OPT": {
      "SUBSTEP": 0,
      "MAXITER": 0
    },
    "PHOP_OPT": {
      "bCONSREBARAREA1D": true,
      "BEAM_CORE_SIZE": "<BEAM_CORE_SIZE>",
      "BEAM_CORE_DIV_Y": 0,
      "BEAM_CORE_DIV_Z": 0,
      "BEAM_COVER_SIZE": "<BEAM_COVER_SIZE>",
      "BEAM_COVER_DIV_Y": 0,
      "BEAM_COVER_DIV_Z": 0,
      "bCONSREBARAREAWALL": true,
      "bWALLCONSOUT": true,
      "WALL_CORE_SIZE": "<WALL_CORE_SIZE>",
      "WALL_CORE_DIV_Z": 0,
      "WALL_CORE_DIV_Y": 0,
      "WALL_COVER_SIZE": "<WALL_COVER_SIZE>",
      "WALL_COVER_DIV_Z": 0,
      "WALL_COVER_DIV_Y": 0,
      "SHEAR_R": 0,
      "bASSIGNBYMEMBER": true,
      "bTRI_SYM": true,
      "TRI_TENS_A1": 0,
      "TRI_TENS_A2": 0,
      "TRI_COMP_A1": 0,
      "TRI_COMP_A2": 0,
      "bBI_SYM": true,
      "BI_TENS_A1": 0,
      "BI_COMP_A1": 0,
      "PSPR_APPLY_TYPE": "<PSPR_APPLY_TYPE>",
      "ELNK_APPLY_TYPE": "<ELNK_APPLY_TYPE>",
      "bUSEAUTOCALCREFERENCE": true,
      "RCDGNCODE": "<RCDGNCODE>",
      "LOC_BEAM": "<LOC_BEAM>",
      "LOC_COLUMN": "<LOC_COLUMN>",
      "SF_WALL": 0,
      "bSF_BRITTLE": true,
      "SF_BRITTLE": 0,
      "bSF_EARTHQUAKE": true,
      "SF_EARTHQUAKE": 0,
      "bSF_SMOOTH_BAR": true,
      "SF_SMOOTH_BAR": "<SF_SMOOTH_BAR>",
      "SND_SEIS_GRUP": "<SND_SEIS_GRUP>",
      "CONFIDENCE": 0,
      "bBUCKLING": true,
      "bCALCAXIALFORCE": true
    },
    "NODECONNECTIVITY": "<NODECONNECTIVITY>",
    "bSHOWGRAPHAFTER": true,
    "bSHOWGRAPGHDURING": true,
    "properties": {
      "INITLOAD": {
        "items": {
          "properties": {
            "LC_NAME": "<LC_NAME>",
            "LC_TYPE": "<LC_TYPE>",
            "SF": 0
          }
        }
      }
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "GEOMNONLINEAR_TYPE": "NONE",
      "INITLOADMETHOD": "PERFORM_ANAL",
      "INITLOAD": [],
      "bCONSIGNOREELEM": true,
      "NONL_OPT": {
        "bPERMITFAIL": true,
        "SUBSTEP": 10,
        "MAXITER": 10,
        "bDISPLNORM": true,
        "bFORCENORM": false,
        "bENERGYNORM": false,
        "DISPLNORM": 0.001,
        "FORCENORM": 0.001,
        "ENERGYNORM": 0.001,
        "bSHEARYIELDSTOP": false,
        "BSHEARYIELDSTOPBEAM": true,
        "bSHEARYIELDSTOPWALL": false,
        "bAXIALYIELDSTOP": false,
        "bAXIALYIELDSTOPBEAM": true,
        "bAXIALYIELDSTOPWALL": false,
        "bAXIALYIELDSTOPTRUSS": false,
        "bSUPPORTDZDIRSTOP": false,
        "bSUPPORTSTOPUPLIFTING": false,
        "bSUPPORTSTOPCOLLAPSE": false
      },
      "PHOP_OPT": {
        "bCONSREBARAREA1D": false,
        "BEAM_CORE_SIZE": "AUTO",
        "BEAM_CORE_DIV_Y": 15,
        "BEAM_CORE_DIV_Z": 15,
        "BEAM_COVER_SIZE": "EQUAL",
        "BEAM_COVER_DIV_Y": 15,
        "BEAM_COVER_DIV_Z": 15,
        "bCONSREBARAREAWALL": false,
        "bWALLCONSOUT": true,
        "WALL_CORE_SIZE": "AUTO",
        "WALL_CORE_DIV_Z": 8,
        "WALL_CORE_DIV_Y": 8,
        "WALL_COVER_SIZE": "AUTO",
        "WALL_COVER_DIV_Z": 8,
        "WALL_COVER_DIV_Y": 1,
        "SHEAR_R": 0.4,
        "bASSIGNBYMEMBER": true,
        "bTRI_SYM": true,
        "TRI_TENS_A1": 0.1,
        "TRI_TENS_A2": 0.05,
        "TRI_COMP_A1": 0.1,
        "TRI_COMP_A2": 0.05,
        "bBI_SYM": true,
        "BI_TENS_A1": 0.05,
        "BI_COMP_A1": 0.05,
        "PSPR_APPLY_TYPE": "ASSUME",
        "ELNK_APPLY_TYPE": "APPLY",
        "bUSEAUTOCALCREFERENCE": true,
        "RCDGNCODE": "KISTEC2019",
        "LOC_BEAM": "M",
        "LOC_COLUMN": "I",
        "SF_WALL": 1.6,
        "bSF_BRITTLE": false,
        "SF_BRITTLE": 1.6,
        "bSF_EARTHQUAKE": false,
        "SF_EARTHQUAKE": 0.85,
        "bSF_SMOOTH_BAR": false,
        "SF_SMOOTH_BAR": 0.575,
        "CONFIDENCE": 1,
        "bBUCKLING": true,
        "bCALCAXIALFORCE": true
      },
      "NODECONNECTIVITY": "PINNED",
      "bSHOWGRAPHAFTER": true,
      "bSHOWGRAPGHDURING": false
    }
  }
}
```


---

### Pushover Global Control — `/db/POGD-M1ᴴˢ⁾`

**方法**: GET, PUT, DELETE | **参数**: 18 必填 + 13 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `GEO_NONL_TYPE` | integer (enum) | **是** | Geometric Nonlinearity Type• None: 0• Large Displacements: 1• P-Delta: 2 |
| `INIT_LOAD_TYPE` | integer (enum) | **是** | Initial Load• Perform Nonlinear Static Analysis for Initial Load: 0• Import Stat |
| `LC_NAME` | 文字（字符串） | **是** | Load Case Name |
| `LC_TYPE` | string (enum) | **是** | Load Case Type |
| `SF` | 数字 | **是** | Scale Factor |
| `OPT_USE` | 是/否（布尔值） | **是** | Use Opition |
| `ITER_CTRL"¹⁾` | 对象（一组键值对） | **是** | Iteration Controls |
| `ASSIGN_BY_MEMBER` | 是/否（布尔值） | **是** | Assign Hinge Properties to Member only |
| `TRILINEAR` | 对象（一组键值对） | **是** | Default Stiffness Reduction Ratio of Skeleton Curve |
| `TENS_A1` | 数字 | **是** | α1 (+) |
| `TENS_A2` | 数字 | **是** | α2 (+) |
| `COMP_A1` | 数字 | **是** | α1 (-) |
| `COMP_A2` | 数字 | **是** | α2 (-) |
| `BILINEAR` | 对象（一组键值对） | **是** | Hinge Property |
| `SYMMETRIC` | 是/否（布尔值） | **是** | Bilinear default stiffness reduction |
| `NONL_TYPE"²⁾` | 对象（一组键值对） | **是** | Point Spring Support & Elastic Link : Nonlinear Type |
| `LOC_BEAM` | integer (enum) | **是** | Reference Location only for Distributed Hinges• I-End: 0• Mid-span: 1• J-End: 2 |
| `CALC_YIELDS` | 是/否（布尔值） | **是** | Calculate Yield Surface of Beam considering Buckling |
| `INIT_LOAD_LIST` | array [object] | 否 | Initial Load Case List |
| `IGNORE_ELEM` | 是/否（布尔值） | 否 | Consider 'Ignore Elements for Initial Load' |
| `ANALYSIS_STOP` | 对象（一组键值对） | 否 | Analysis Stop |
| `SHEAR_YIELD` | 对象（一组键值对） | 否 | Shear Component Yield |
| `BEAM_COLUMN` | 是/否（布尔值） | 否 | Beam/Column |
| `AXIAL_YIELD` | 对象（一组键值对） | 否 | Axial Component Collapse/Buckling |
| `BEAM` | 是/否（布尔值） | 否 | Beam/Column |
| `TRUSS` | 是/否（布尔值） | 否 | Truss |
| `SUPPORT_DZ_DIR` | 对象（一组键值对） | 否 | Support Uplifting/Collapse : Dz-Direction |
| `UPLIFT` | 是/否（布尔值） | 否 | Uplift |
| ... | ... | ... | *还有 3 个可选参数* |

**最简 JSON**：
```json
{
  "GEO_NONL_TYPE": {},
  "INIT_LOAD_TYPE": {},
  "LC_NAME": "<LC_NAME>",
  "LC_TYPE": {},
  "SF": 0,
  "OPT_USE": true,
  "ITER_CTRL\"¹⁾": {},
  "ASSIGN_BY_MEMBER": true,
  "TRILINEAR": {},
  "TENS_A1": 0,
  "TENS_A2": 0,
  "COMP_A1": 0,
  "COMP_A2": 0,
  "BILINEAR": {},
  "SYMMETRIC": true,
  "NONL_TYPE\"²⁾": {},
  "LOC_BEAM": {},
  "CALC_YIELDS": true
}
```


---

### Ignore Elements for Pushover Intial Load — `/db/IEPI`

**方法**: POST, GET, PUT, DELETE | **参数**: 0 必填 + 1 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `B_IGNORE` | 是/否（布尔值） | 否 | Ignore Elements for NL. Analysis Initial Load |

**官方示例**：
```json
{
  "Assign": {
    "59": {
      "B_IGNORE": true
    },
    "60": {
      "B_IGNORE": true
    },
    "61": {
      "B_IGNORE": true
    },
    "62": {
      "B_IGNORE": true
    },
    "63": {
      "B_IGNORE": true
    },
    "64": {
      "B_IGNORE": true
    },
    "65": {
      "B_IGNORE": true
    },
    "66": {
      "B_IGNORE": true
    },
    "67": {
      "B_IGNORE": true
    },
    "68": {
      "B_IGNORE": true
    },
    "69": {
      "B_IGNORE": true
    },
    "70": {
      "B_IGNORE": true
    }
  }
}
```


---

### Assign Pushover Hinge Properties — `/db/PHGE`

**方法**: POST, GET, PUT, DELETE | **参数**: 4 必填 + 0 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `ID` | 整数 | **是** | ID |
| `TYPE` | 文字（字符串） | **是** | Element Type |
| `HINGE_TYPE` | 文字（字符串） | **是** | Pushover Hinge Type |
| `FIBER_KEY` | 整数 | **是** | Fiber Key |

**最简 JSON**：
```json
{
  "PHGE": {
    "ID": 0,
    "TYPE": "<TYPE>",
    "HINGE_TYPE": "<HINGE_TYPE>",
    "FIBER_KEY": 0
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "15": {
      "ID": 1,
      "TYPE": "BEAM",
      "HINGE_TYPE": "Myz_15",
      "FIBER_KEY": 0
    }
  }
}
```


---

### Pushover Load Cases — `/db/POLC`

**方法**: POST, GET, PUT, DELETE | **参数**: 19 必填 + 7 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `LCNAME` | 文字（字符串） | **是** | Load Case Name |
| `INCRE_STEP` | 整数 | **是** | Increment Steps |
| `bCONS_PDELTA` | 是/否（布尔值） | **是** | Consider P-Delta Effect |
| `INCRE_METHOD` | 文字（字符串） | **是** | Increment Method• Load Control: "LOAD"• Displacement Control: "DISP" |
| `STEPCTRLOPTION` | 文字（字符串） | **是** | Stepping Control Option• Auto-Stepping Control: "AUTO"• Equal Step (1/nstep): "E |
| `INCFUNC_KEY` | 整数 | **是** | Incremental Control Function Key• When "STEPCTRLOPTION" is "INC_FUNC" |
| `STIFF_RATIO` | 数字 | **是** | Analysis Stopping Condition• Current Stiffness Ratio (Cs) |
| `LIMITDEFORMANGLE` | 数字 | **是** | Limit Inter-Story Deformation Angle (1/[rad]) |
| `DISPCTRLOPTION` | 文字（字符串） | **是** | Displacement Control Option• Global: "GLOBAL"• Master Node: "NODE" |
| `GLOBAL_MAX_DISP` | 数字 | **是** | Max Translational Displacement |
| `MASTERNODE` | 整数 | **是** | Node ID Number |
| `MASTERDIRECTION` | 文字（字符串） | **是** | Node Direction• "DX"• "DY"• "DZ" |
| `MASTERMAXDISP` | 数字 | **是** | Maximum Displacement |
| `LOADPATTERNTYPE` | 文字（字符串） | **是** | Load Pattern Type• Static Load Cases: "LOAD"• Uniform Acceleration: "ACC"• Mode  |
| `LOADPATTERN` | Array[Object] | **是** | Load Pattern Data List• Insert the data as an object |
| `FIBER_KEY` | 整数 | **是** | Fiber Key |
| `SF` | 数字 | **是** | Scale Factor |
| `DIR` | 文字（字符串） | **是** | Direction• "DX"• "DY"• "DZ" |
| `MODE` | 整数 | **是** | Mode Number |
| `DESC` | 文字（字符串） | 否 | Description |
| `bUSEINITIAL` | 是/否（布尔值） | 否 | Use Initial Load |
| `bREACOUTPUT` | 是/否（布尔值） | 否 | Cumulative Reaction / Story Shear by Initial Load |
| `bLIMITDEFORMANGLE` | 是/否（布尔值） | 否 | Use Limit Inter-Story Deformation Angle |
| `bDRIFTMAX` | 是/否（布尔值） | 否 | Maximum Drift of All Vertical Elements |
| `bDRIFTCENTER` | 是/否（布尔值） | 否 | Drift at the Center of Floor Diaphragm (Story Center) |
| `bDRIFTAVER` | 是/否（布尔值） | 否 | Drift calculated by Average Displacement of Story |

**最简 JSON**：
```json
{
  "POLC": {
    "LCNAME": "<LCNAME>",
    "INCRE_STEP": 0,
    "bCONS_PDELTA": true,
    "INCRE_METHOD": "<INCRE_METHOD>",
    "STEPCTRLOPTION": "<STEPCTRLOPTION>",
    "INCFUNC_KEY": 0,
    "STIFF_RATIO": 0,
    "LIMITDEFORMANGLE": 0,
    "DISPCTRLOPTION": "<DISPCTRLOPTION>",
    "GLOBAL_MAX_DISP": 0,
    "MASTERNODE": 0,
    "MASTERDIRECTION": "<MASTERDIRECTION>",
    "MASTERMAXDISP": 0,
    "LOADPATTERNTYPE": "<LOADPATTERNTYPE>",
    "LOADPATTERN": [],
    "properties": {
      "LOADPATTERN": {
        "items": {
          "properties": {
            "SF": 0,
            "DIR": "<DIR>",
            "MODE": 0
          }
        }
      }
    }
  },
  "FIBER_KEY": 0
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "LCNAME": "Mode_X",
      "DESC": "",
      "INCRE_STEP": 10,
      "bCONS_PDELTA": true,
      "bUSEINITIAL": false,
      "bREACOUTPUT": false,
      "INCRE_METHOD": "DISP",
      "STEPCTRLOPTION": "AUTO",
      "INCFUNC_KEY": 0,
      "STIFF_RATIO": 0,
      "bLIMITDEFORMANGLE": true,
      "LIMITDEFORMANGLE": 10,
      "bDRIFTMAX": true,
      "bDRIFTCENTER": false,
      "bDRIFTAVER": false,
      "DISPCTRLOPTION": "NODE",
      "GLOBAL_MAX_DISP": 0,
      "MASTERNODE": 134,
      "MASTERDIRECTION": "DX",
      "MASTERMAXDISP": 1,
      "LOADPATTERNTYPE": "MODE",
      "LOADPATTERN": [
        {
          "MODE": 1,
          "SF": 1
        }
      ]
    },
    "2": {
      "LCNAME": "Mode_Y",
      "DESC": "",
      "INCRE_STEP": 10,
      "bCONS_PDELTA": false,
      "bUSEINITIAL": false,
      "bREACOUTPUT": false,
      "INCRE_METHOD": "LOAD",
      "STEPCTRLOPTION": "AUTO",
      "INCFUNC_KEY": 0,
      "STIFF_RATIO": 0,
      "bLIMITDEFORMANGLE": true,
      "LIMITDEFORMANGLE": 10,
      "bDRIFTMAX": true,
      "bDRIFTCENTER": false,
      "bDRIFTAVER": false,
      "DISPCTRLOPTION": "GLOBAL",
      "GLOBAL_MAX_DISP": 0,
      "MASTERNODE": 0,
      "MASTERDIRECTION": "",
      "MASTERMAXDISP": 0,
      "LOADPATTERNTYPE": "LOAD",
      "LOADPATTERN": [
        {
          "LCNAME": "LOAD1",
          "SF": 1
        }
      ]
    },
    "3": {
      "LCNAME": "Uni_X",
      "DESC": "",
      "INCRE_STEP": 10,
      "bCONS_PDELTA": false,
      "bUSEINITIAL": false,
      "bREACOUTPUT": false,
      "INCRE_METHOD": "LOAD",
      "STEPCTRLOPTION": "EQUAL",
      "INCFUNC_KEY": 0,
      "STIFF_RATIO": 0,
      "bLIMITDEFORMANGLE": true,
      "LIMITDEFORMANGLE": 10,
      "bDRIFTMAX": true,
      "bDRIFTCENTER": false,
      "bDRIFTAVER": false,
      "DISPCTRLOPTION": "GLOBAL",
      "GLOBAL_MAX_DISP": 0,
      "MASTERNODE": 0,
      "MASTERDIRECTION": "",
      "MASTERMAXDISP": 0,
      "LOADPATTERNTYPE": "ACC",
      "LOADPATTERN": [
        {
          "DIR": "DX",
          "SF": 1
        }
      ]
    },
    "4": {
      "LCNAME": "Uni_Y",
      "DESC": "",
      "INCRE_STEP": 10,
      "bCONS_PDELTA": true,
      "bUSEINITIAL": false,
      "bREACOUTPUT": false,
      "INCRE_METHOD": "DISP",
      "STEPCTRLOPTION": "AUTO",
      "INCFUNC_KEY": 0,
      "STIFF_RATIO": 0,
      "bLIMITDEFORMANGLE": true,
      "LIMITDEFORMANGLE": 10,
      "bDRIFTMAX": true,
      "bDRIFTCENTER": false,
      "bDRIFTAVER": false,
      "DISPCTRLOPTION": "NODE",
      "GLOBAL_MAX_DISP": 0,
      "MASTERNODE": 134,
      "MASTERDIRECTION": "DY",
      "MASTERMAXDISP": 1,
      "LOADPATTERNTYPE": "NOR_MODE",
      "LOADPATTERN": [
        {
          "MODE": 1,
          "SF": 1
        }
      ]
    }
  }
}
```


---

### Pushover Load Case — `/db/POLC-M1ᴴˢ⁾`

**方法**: POST, GET, PUT, DELETE | **参数**: 20 必填 + 1 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `LCNAME` | 文字（字符串） | **是** | Load Case |
| `INCRE_STEP` | 整数 | **是** | Increment Steps (nstep) |
| `NLTYPE` | string (enum) | **是** | Geometric Nonlinearity Type• None: NONE• P-Delta: PDELTA• Large Displacements: L |
| `bUSEINITIAL` | 是/否（布尔值） | **是** | Use Initial Load |
| `bREACOUTPUT` | 是/否（布尔值） | **是** | Cumulative Reaction by Initial Load |
| `INCRE_METHOD` | string (enum) | **是** | Increment Method• Load Control: LOAD• Displacement Control: DISP |
| `CTRL_OPT` | 对象（一组键值对） | **是** | Control Option |
| `STEPCTRLOPTION` | string (enum) | **是** | Auto-Stepping Control• Auto-Stepping Control: AUTO• Equal Step: EQUAL• Increment |
| `INCFUNC_NAME` | 文字（字符串） | **是** | Increment Function Name |
| `STIFF_RATIO` | 数字 | **是** | Current Stiffness Ratio (Cs) |
| `DISPCTRLOPTION` | string (enum) | **是** | Global• Global: GLOBAL• Master Node: NODE |
| `GLOBAL_MAX_DISP` | 数字 | **是** | Max. Translational Displacement |
| `MASTERNODE` | 整数 | **是** | Node |
| `MASTERDIRECTION` | string (enum) | **是** | Direction• DX: DX• DY: DY• DZ: DZ |
| `MASTERMAXDISP` | 数字 | **是** | Max. Displacement |
| `LOADPATTERNTYPE` | string (enum) | **是** | Load Pattern• Static Load Cases: LOAD• Uniform Acceleration: ACC• Mode Shape: MO |
| `LOADPATTERN` | array [object] | **是** | Load Pattern |
| `SF` | 数字 | **是** | Scale Factor |
| `DIR` | string (enum) | **是** | Direction• DX: DX• DY: DY• DZ: DZ |
| `MODE` | 整数 | **是** | Mode |
| `DESC` | 文字（字符串） | 否 | Description |

**最简 JSON**：
```json
{
  "LCNAME": "<LCNAME>",
  "INCRE_STEP": 0,
  "NLTYPE": {},
  "bUSEINITIAL": true,
  "bREACOUTPUT": true,
  "INCRE_METHOD": {},
  "CTRL_OPT": {},
  "STEPCTRLOPTION": {},
  "INCFUNC_NAME": "<INCFUNC_NAME>",
  "STIFF_RATIO": 0,
  "DISPCTRLOPTION": {},
  "GLOBAL_MAX_DISP": 0,
  "MASTERNODE": 0,
  "MASTERDIRECTION": {},
  "MASTERMAXDISP": 0,
  "LOADPATTERNTYPE": {},
  "LOADPATTERN": [],
  "SF": 0,
  "DIR": {},
  "MODE": 0
}
```


---

### RC Design Code — `/db/DCON`

**方法**: POST, GET, PUT, DELETE | **参数**: 1 必填 + 0 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `DGNCODE` | 文字（字符串） | **是** | Design Code¹⁾ |

**最简 JSON**：
```json
{
  "DCON": {
    "DGNCODE": "<DGNCODE>"
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "DGNCODE": "KCI-USD12"
    }
  }
}
```


---

### Modify Concrete Materials — `/db/MATD`

**方法**: GET, PUT, DELETE | **参数**: 8 必填 + 22 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TYPE` | 文字（字符串） | **是** | Material Type• Concrete: "CONC" |
| `NAME` | 文字（字符串） | **是** | Material Name |
| `DATA1` | 对象（一组键值对） | **是** | Concrete Material Information |
| `CODENAME` | 文字（字符串） | **是** | Material Code Name |
| `CODEMATLNAME` | 文字（字符串） | **是** | Material Grade |
| `DESIGN` | 文字（字符串） | **是** | Material Design Values |
| `MAINREBAR_REBARNAME` | 文字（字符串） | **是** | Main Rebar Name |
| `RABAR_CODENAME` | 文字（字符串） | **是** | Rebar Code Name |
| `SUBCODENAME` | 文字（字符串） | 否 | SubCodeName |
| `bHYBRID_FACTOR` | 是/否（布尔值） | 否 | HybirdFactor |
| `ANAL` | 对象（一组键值对） | 否 | AnalysisData |
| `TOP_F_ANAL` | 对象（一组键值对） | 否 | AnalysisDataTopFlange |
| `BOT_F_ANAL` | 对象（一组键值对） | 否 | AnalysisDataTopFlange |
| `WEB_ANAL` | 对象（一组键值对） | 否 | AnalysisDataTopFlange |
| `TOP_F_DESIGN` | 对象（一组键值对） | 否 | DesignDataTopFlange |
| `BOT_F_DESIGN` | 对象（一组键值对） | 否 | DesignDataTopFlange |
| `WEB_DESIGN` | 对象（一组键值对） | 否 | DesignDataTopFlange |
| `DATA2` | 对象（一组键值对） | 否 | Data2 |
| ... | ... | ... | *还有 12 个可选参数* |

**最简 JSON**：
```json
{
  "MATD": {
    "TYPE": "<TYPE>",
    "NAME": "<NAME>",
    "DATA1": {},
    "DATA2": {
      "CODENAME": "<CODENAME>",
      "CODEMATLNAME": "<CODEMATLNAME>",
      "DESIGN": "<DESIGN>"
    },
    "MAINREBAR_REBARNAME": "<MAINREBAR_REBARNAME>"
  },
  "RABAR_CODENAME": "<RABAR_CODENAME>"
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "TYPE": "CONC",
      "NAME": "C16/20",
      "DATA1": {
        "CODENAME": "EN(RC)",
        "CODEMATLNAME": "C16/20",
        "DESIGN": {
          "C_FC": 16000,
          "C_FCI": 11200
        }
      },
      "REBAR_CODENAME": "EN04(RC)",
      "MAINREBAR_REBARNAME": "ClassB",
      "SUBREBAR_REBARNAME": "ClassC",
      "MAINREBAR_B_FY": 500000,
      "SUBREBAR_B_FY": 600000
    }
  }
}
```


---

### Rebar Input for Checking - Beam/Column — `/db/RCHK`

**方法**: POST, GET, PUT, DELETE | **参数**: 8 必填 + 1 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `MEMBTYPE` | 文字（字符串） | **是** | Member Type• Beam: "BEAM"• Column: "COLUMN" |
| `ENVTYPE` | 整数 | **是** | Crack Checking• Class 1 Exposure Condition: 0• Class 2 Exposuse Condition: 1 |
| `BEAM` | 对象（一组键值对） | **是** | Rebar Infomation for Beam |
| `vMAIN` | Array[Object] | **是** | Longitudinal Rebar• Insert the data as an object• [I, J, M] |
| `vSUB_BAR` | Array[Object] | **是** | Transverse Rebar• Insert the data as an Obejct• [I, J, M] |
| `COLM` | 对象（一组键值对） | **是** | Rebar Infomation for Column |
| `vLAYER` | Array[Object] | **是** | Longitudinal Rebar• Insert the data as an object |
| `SUB_BAR` | Array[Object] | **是** | Transverse Rebar• Insert the data as an Obejct |
| `OPTION_IMJSAME` | 是/否（布尔值） | 否 | IMJSameOption(itneedsonlyI) |

**最简 JSON**：
```json
{
  "RCHK": {
    "MEMBTYPE": "<MEMBTYPE>",
    "ENVTYPE": 0,
    "BEAM": {
      "vMAIN": [],
      "vSUB_BAR": []
    },
    "COLM": {
      "vLAYER": [],
      "SUB_BAR": []
    }
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "MEMBTYPE": "COLUMN",
      "ENVTYPE": 0,
      "COLM": {
        "vLAYER": [
          {
            "INDEX": 1,
            "dDc": 0.1,
            "vPOSITION": [
              {
                "POSITION": "P1",
                "BAR_NUM": 24,
                "BAR_NAME1": "#4",
                "BAR_NAME2": ""
              }
            ]
          },
          {
            "INDEX": 2,
            "dDc": 0.2,
            "vPOSITION": [
              {
                "POSITION": "P1",
                "BAR_NUM": 24,
                "BAR_NAME1": "#4",
                "BAR_NAME2": ""
              }
            ]
          }
        ],
        "SUB_BAR": {
          "SUBBAR_NAME": "#4",
          "SUBBAR_DIST": 0.1,
          "SUBBAR_NUM": 12,
          "SUBBAR_NAME_Y": "#4",
          "SUBBAR_NAME_Z": "#4",
          "SUBBAR_NUM_Y": 12,
          "SUBBAR_NUM_Z": 12
        }
      }
    },
    "2": {
      "MEMBTYPE": "BEAM",
      "ENVTYPE": 1,
      "BEAM": {
        "vMAIN": [
          {
            "SECTOR": "I",
            "POS_TOP_LAYERS": [
              {
                "LAYER": 1,
                "dD": 0.1,
                "BAR_NUM": 12,
                "BAR_NAME1": "#5",
                "BAR_NAME2": ""
              }
            ],
            "POS_BOT_LAYERS": [
              {
                "LAYER": 1,
                "dD": 0.1,
                "BAR_NUM": 12,
                "BAR_NAME1": "#7",
                "BAR_NAME2": ""
              }
            ]
          },
          {
            "SECTOR": "M",
            "POS_TOP_LAYERS": [
              {
                "LAYER": 1,
                "dD": 0.1,
                "BAR_NUM": 12,
                "BAR_NAME1": "#5",
                "BAR_NAME2": ""
              }
            ],
            "POS_BOT_LAYERS": [
              {
                "LAYER": 1,
                "dD": 0.1,
                "BAR_NUM": 12,
                "BAR_NAME1": "#7",
                "BAR_NAME2": ""
              }
            ]
          },
          {
            "SECTOR": "J",
            "POS_TOP_LAYERS": [
              {
                "LAYER": 1,
                "dD": 0.1,
                "BAR_NUM": 12,
                "BAR_NAME1": "#5",
                "BAR_NAME2": ""
              }
            ],
            "POS_BOT_LAYERS": [
              {
                "LAYER": 1,
                "dD": 0.1,
                "BAR_NUM": 12,
                "BAR_NAME1": "#7",
                "BAR_NAME2": ""
              }
            ]
          }
        ],
        "vSUB_BAR": [
          {
            "SECTOR": "I",
            "dSUB_BARNUM": 2,
            "SUB_BARNAME": "#6",
            "dSUB_BARDIST": 0.1,
            "dSUB_BARANGLE": 90
          },
          {
            "SECTOR": "M",
            "dSUB_BARNUM": 2,
            "SUB_BARNAME": "#6",
            "dSUB_BARDIST": 0.1,
            "dSUB_BARANGLE": 90
          },
          {
            "SECTOR": "J",
            "dSUB_BARNUM": 2,
            "SUB_BARNAME": "#6",
            "dSUB_BARDIST": 0.1,
            "dSUB_BARANGLE": 90
          }
        ]
      }
    },
    "3": {
      "MEMBTYPE": "COLUMN",
      "ENVTYPE": 0,
      "COLM": {
        "vLAYER": [
          {
            "INDEX": 1,
            "dDc": 0.1,
            "vPOSITION": [
              {
                "POSITION": "P1",
                "BAR_NUM": 8,
                "BAR_NAME1": "#6",
                "BAR_NAME2": ""
              },
              {
                "POSITION": "P2",
                "BAR_NUM": 12,
                "BAR_NAME1": "#6",
                "BAR_NAME2": ""
              }
            ]
          }
        ],
        "SUB_BAR": {
          "SUBBAR_NAME": "#5",
          "SUBBAR_DIST": 0.1,
          "SUBBAR_NUM": 2,
          "SUBBAR_NAME_Y": "#5",
          "SUBBAR_NAME_Z": "#5",
          "SUBBAR_NUM_Y": 10,
          "SUBBAR_NUM_Z": 8
        }
      }
    }
  }
}
```


---

### Unbraced Length — `/db/LENG`

**方法**: POST, GET, PUT, DELETE | **参数**: 0 必填 + 6 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `LY` | 数字 | 否 | Unbraced Length Ly |
| `LZ` | 数字 | 否 | Unbraced Length Lz |
| `LB` | 数字 | 否 | Laterally Unbraced Length |
| `bNOTUSE` | 是/否（布尔值） | 否 | Do not consider of laterally unbraced length |
| `bAUTOCALC` | 是/否（布尔值） | 否 | Calculate by Code |
| `LT` | 数字 | 否 | Torsional Unbraced Length |

**官方示例**：
```json
{
  "Assign": {
    "21": {
      "LY": 9.464111,
      "LZ": 4,
      "LB": 4,
      "bNOTUSE": false,
      "bAUTOCALC": false,
      "LT": 9.464111
    }
  }
}
```


---

### Member Assignment — `/db/MEMB`

**方法**: POST, GET, PUT, DELETE | **参数**: 1 必填 + 1 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `AELEM` | 整数数组 | **是** | Element Lists |
| `bREVERSE` | 是/否（布尔值） | 否 | Reverse Local Direction |

**最简 JSON**：
```json
{
  "Argument": {
    "AELEM": 0
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "AELEM": [
        36,
        48,
        46,
        49,
        47
      ]
    },
    "2": {
      "AELEM": [
        32,
        43
      ],
      "bREVERSE": true
    }
  }
}
```


---

### Definition of Frame — `/db/DCTL`

**方法**: POST, GET, PUT, DELETE | **参数**: 0 必填 + 4 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `FRAMEX` | 文字（字符串） | 否 | X-Direction of Frame• Unbraced | Sway: “Unbraced Sway”• Braced | Non-sway: “Brac |
| `FRAMEY` | 文字（字符串） | 否 | Y-Direction of Frame• Unbraced | Sway: “Unbraced Sway”• Braced | Non-sway: “Brac |
| `bAUTOKF` | 是/否（布尔值） | 否 | Auto Calculate Effective Length Factor |
| `DT` | 文字（字符串） | 否 | Design Type• 3-D : “3D”• X-Z Plane : “XZ”• Y-Z Plane : “YZ”• X-Y Plane : “XY” |

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "FRAMEX": "Braced Non-sway",
      "FRAMEY": "Braced Non-sway",
      "bAUTOKF": false,
      "DT": "XY"
    }
  }
}
```


---

### Limiting Slenderness Ratio — `/db/LTSR`

**方法**: POST, GET, PUT, DELETE | **参数**: 2 必填 + 1 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `COMP` | 数字 | **是** | Limiting Slenderness Ratio for Compression |
| `TENS` | 数字 | **是** | Limiting Slenderness Ratio for Tension |
| `bNOTCHECK` | 是/否（布尔值） | 否 | Do not check for Slenderness Ratio |

**最简 JSON**：
```json
{
  "Argument": {
    "COMP": 0,
    "TENS": 0
  }
}
```

**官方示例**：
```json
{
  "LTSR": {
    "602": {
      "bNOTCHECK": false,
      "COMP": 150,
      "TENS": 400
    },
    "651": {
      "bNOTCHECK": false,
      "COMP": 200,
      "TENS": 300
    },
    "734": {
      "bNOTCHECK": false,
      "COMP": 200,
      "TENS": 300
    }
  }
}
```


---

### Underground Load Combination Type — `/db/ULCT`

**方法**: POST, GET, PUT, DELETE | **参数**: 0 必填 + 1 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `bUNDERLOADTYPE` | 是/否（布尔值） | 否 | Assign Member• For Underground Loads : true• For None-underground Loads : false |

**官方示例**：
```json
{
  "Assign": {
    "2": {
      "bUNDERLOADTYPE": true
    },
    "397": {
      "bUNDERLOADTYPE": false
    }
  }
}
```


---

### Modify Member Type — `/db/MBTP`

**方法**: POST, GET, PUT, DELETE | **参数**: 1 必填 + 0 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `TYPE` | 文字（字符串） | **是** | Member Type• Column : "COLUMN"• Beam : "BEAM"• Brace : "BRACE" |

**最简 JSON**：
```json
{
  "TYPE": "<TYPE>"
}
```

**官方示例**：
```json
{
  "Assign": {
    "160": {
      "TYPE": "COLUMN"
    },
    "174": {
      "TYPE": "COLUMN"
    },
    "188": {
      "TYPE": "BEAM"
    },
    "306": {
      "TYPE": "BEAM"
    },
    "376": {
      "TYPE": "BRACE"
    },
    "377": {
      "TYPE": "BRACE"
    }
  }
}
```


---

### Modify Wall Mark Design — `/db/WMAK`

**方法**: POST, GET, PUT, DELETE | **参数**: 2 必填 + 0 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `MARKNAME` | 文字（字符串） | **是** | Wall Mark Name |
| `WID_LIST` | 整数数组 | **是** | Wall ID List |

**最简 JSON**：
```json
{
  "MARKNAME": "<MARKNAME>",
  "WID_LIST": 0
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "MARKNAME": "W1",
      "WID_LIST": [
        1,
        5,
        8
      ]
    },
    "2": {
      "MARKNAME": "W2",
      "WID_LIST": [
        2,
        3,
        4,
        6,
        7
      ]
    },
    "3": {
      "MARKNAME": "W3",
      "WID_LIST": [
        9,
        10,
        11
      ]
    }
  }
}
```


---

### Design Steel Code — `/db/DSTL`

**方法**: POST, GET, PUT, DELETE | **参数**: 1 必填 + 0 可选

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `DGNCODE` | 文字（字符串） | **是** | Design Code¹⁾ |

**最简 JSON**：
```json
{
  "Argument": {
    "DGNCODE": "<DGNCODE>"
  }
}
```

**官方示例**：
```json
{
  "Assign": {
    "1": {
      "DGNCODE": "Eurocode3-2:05"
    }
  }
}
```


---
