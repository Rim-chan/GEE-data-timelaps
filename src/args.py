from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser


def get_main_args():
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    arg = parser.add_argument
    
    arg("--cloud_coverage_percentage", type=int, default=20, help="Cloud Coverage Percentage")
    arg("--yearsL5789", type=list, default=[2000+i for i in range(24)], help="List of Years")
    arg("--yearsS2", type=list, default=[2017+i for i in range(7)], help="List of Years")
    arg("--months", type=list, default=[i+1 for i in range(12)], help="List of Months")
    arg("--calendar", type=dict, default={'January': 1, 'February' : 2, 'March' : 3, 'April' : 4,
                                          'May' : 5, 'June' : 6, 'July' : 7, 'August' : 8, 'September' : 9,
                                          'October' : 10, 'November' : 11, 'December' : 12}, help="Calendar")
    
    
    arg("--image_idx", type=int, default=0, help="Index of Image to Display")
    
    arg("--RGBvis", type=dict, default={'bands': ['B4', 'B3', 'B2'], 'min': 0.0, 'max': 0.4},
                               help="Visualization Parameters of True Color Raster")
    
    arg("--ndviVis", type=dict, default={'bands': ['NDVI'], 'min': -1.0, 'max': 1.0, 'palette': ['red', 'white', 'green'] },
                                help="Visualization Parameters of NDVI")
    
    arg("--saviVis", type=dict, default={'bands': ['SAVI'], 'min': -1.0, 'max': 1.0, 'palette': ['red', 'white', 'green'] },
                                help="Visualization Parameters of SAVI")
    
    arg("--msavi2Vis", type=dict, default={'bands': ['MSAVI2'], 'min': -1.0, 'max': 1.0, 'palette': ['red', 'white', 'green'] },
                                help="Visualization Parameters of MSAVI2")

    return parser.parse_args()
