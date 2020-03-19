# -*- coding: utf-8 -*-
"""
Created on Tue May 16 16:11:49 2017

@author: jparent
"""

import xml.etree.ElementTree as ET
import csv
import os

def ReadStroboSetup(path) :
    """
    Read StroboSetup.xml file saved by koala,
    Return two list : parameters and values that contains parameters name and respective values
    """
    #Parse file and get tree
    file = os.path.join(path,'strobosetup.xml')
    if not os.path.exists(file) :
        print('strobosetup.xml not found')
        return None, None
    tree = ET.parse(file)
    root = tree.getroot()
    fileVersion = root.find('FileVersion').text
    #Check file version
    if fileVersion != '2013.08.27' :
        print("strobostetup version not supported : ",fileVersion)
        return None, None
    setup = root.find('Setup')
    
    #Get setup information
    operatingMode       = setup.find('OperatingMode').text
    #Get general settings
    generalSettings     = setup.find('GeneralSettings')
    samplePerPeriod     = generalSettings.find('SamplesNbPerPeriod').text
    frequency           = generalSettings.find('FrequencyHz').text
    parameters = ['OperatingMode','SamplePerPeriod','Frequency']
    values = [operatingMode,int(samplePerPeriod),float(frequency)]

    #Get scannig settings
    scanningSettings    = setup.find('ScanningSettings')
    if scanningSettings is not None :
        #mode                = scanningSettings.find('Mode').text
        #unit                = scanningSettings.find('Units').text
        frequencyStart      = scanningSettings.find('StartValue').text
        frequencyStep       = scanningSettings.find('StepValue').text
        stepNumber          = scanningSettings.find('StepsNb').text
        frequencyStop       = scanningSettings.find('StopValue').text
        periodPerFrequency = scanningSettings.find('PeriodsNbPerStep').text
        parameters = parameters + ['FrequencyStart','FrequencyStep','FrequencyStop','StepNumber','PeriodPerFrequency']
        values = values + [float(frequencyStart),float(frequencyStep),float(frequencyStop),int(stepNumber),int(periodPerFrequency)]
    return parameters, values
        
def ReadTimeStamps(path) :
    """
    Look for timestamps.txt and strobo_timstamps.txt in path
    Return N, the number of lines and timestamps a list containing all data
    """
    file = os.path.join(path,'timestamps.txt')
    if not os.path.exists(file) : 
        file = os.path.join(path,'strobo_timestamps.txt')
        if not os.path.exists(file) :
            print('timestamps.txt and strobo_timestamps.txt not found')
            return None, None
        
    with open(file) as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        timestamps = list()
        for row in reader:
            timestamps.append(row)
        N = reader.line_num;
        return N, timestamps

#fpath = r'C:\DHM on c drive\Support\UCDAVIS\grid\9 Mhz'
#[params,values] = ReadStroboSetup(fpath)
#[N, timestamps] = ReadTimeStamps(fpath)