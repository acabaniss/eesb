# Using the Entropy Estimating Statistical Bootstrap (EESB) from the THOTH package

The entropy estimating statistical bootstrap (EESB) proposed in DeDeo et al. (Entropy 2013, 15(6), 2246-2276; [https://doi.org/10.3390/e15062246](https://doi.org/10.3390/e15062246)) and released as the [THOTH python package](http://thoth-python.org/) are very useful for conceptualizing the effects of repeated sampling on measures of diversity/information.

This repository presents code for using THOTH package as mentioned and deployed in my 2019 paper in Frontiers in Digital Humanities (Front. Digit. Humanit., 11 June 2019 [https://doi.org/10.3389/fdigh.2019.00011](https://doi.org/10.3389/fdigh.2019.00011)). It includes three scripts. All three scrips have a dependency on the THOTH package, which must be installed before use. These scripts are mildly edited for clarify from their original publication as the supplemental materials to that paper.

The first, **thothSupplemental.py**, provides functions for data cleaning and a wrapper for the THOTH main function, calc\_entropy. The command "get\_entropy" in this package makes it possible to get the results of a THOTH bootstrap entropy command in a pandas-compatible format, while "create\_structure" and "add\_row" provide commands for setting up and editing a pandas DataFrame that stores multiple THOTH results.

The second script, **sampleData.py**, uses **thothSupplemental.py** and scipy to create a large number of artificial counted datasets. Each dataset has a _true_ or _population_ entropy or diversity based on a draw from a Dirichlet distribution of _m_ categories (default: 2<=m<11, 10 for each value of m). This distribution is then the source for a small sample of size n (default: 2<=n<31, 10 for each sample size). These numerical data are then used to compute the uninformed entropy and the EESB entropy. These are then output to a .csv file, which is included with this distribution. 

The third and final script, **frontiersFigures.py**, provides code to generate the figure actually illustrated in Frontiers (figure 2). It takes the results of the **sampleData.py** script and graphs how close to the "true" or "population" entropy the estimate is, as well as whether the estimated entropy is above or below the maximum value.

I also include the results of the sample data actually produced by **sampleData.py** and used for the paper in the subfolder _data_.

If you have any questions about any of these materials, please don't hesitate to get in touch with me at ahfc (at) umich (dot) edu.

