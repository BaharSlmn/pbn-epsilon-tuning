#include <iostream>
#include <fstream> //For file operation
#include <regex>  // For regular expression

#include <cstdio>
#include <iostream>
#include <memory>
#include <stdexcept>
#include <string>
#include <sstream>
#include <array>
#include <map>
#include <math.h>       /* log */
#include <limits> /* precision of floats */
#include <boost/lexical_cast.hpp>




std::string storm_tuning_executable = "../build/storm-project-starter1";
std::string storm_benchmarks_directory = "storm-benchmarks/";
std::string bayesserver_directory = "bayesserver-benchmarks/p1/";
std::string config_files_directory = "storm-vs-bayesserver/config_files/";
std::string outputfiles_directory = "output-files/";
std::string csvfiles_directory = "csv-files/";

/* default */
int numberOfRandom = 10000;
int maxIterations = 6;
int numberOfParams = 1;
double expansionFactor = 2;
double epsilon = 0.0625;
double refThreshold = 0.01;





double timeout = 20; /* minutes*/
enum PBNClass {p1 = 1, p2 = 2, p4 = 4, p8 = 8, pstar };
enum Variant {coverageChanged, threshholdChanged, epsilonChanged};



std::string readFile(std::string filePath, std::string defaultContent){
    std::ifstream ifs(filePath);
     std::string content( (std::istreambuf_iterator<char>(ifs) ),
                          (std::istreambuf_iterator<char>()    ) );
    return content;
}

void writeFile(std::string filePath, std::string fileContent){
    std::ofstream outputFile;
    outputFile.open(filePath);
    outputFile << fileContent;
}

std::string exec(const char* cmd) {
    std::array<char, 128> buffer;
    std::string result;
    std::unique_ptr<FILE, decltype(&pclose)> pipe(popen(cmd, "r"), pclose);
    if (!pipe) {
       throw std::runtime_error("popen() failed!");
    }
    while (fgets(buffer.data(), buffer.size(), pipe.get()) != nullptr) {
        result += buffer.data();
    }
    return result;
}


std::string getStormNumberOfIterations(std::string textresult,  std::string infoKey ){
    std::istringstream f(textresult);
    std::string line;
    bool isTimeOut = true;
    while (std::getline(f, line)) {
        if(line.find(infoKey) != std::string::npos){
            isTimeOut = false;
            break;
        }
    }
    if(isTimeOut)
        return "10000"; /*TIMEOUT*/
    std::vector<std::string> infolinevector;
    std::istringstream iss(line);
    for(std::string s; iss >> line; )
        infolinevector.push_back(line);
    std::string info = infolinevector.at(3);
    return info;
}


std::string getStormPLATime(std::string textresult, std::string infoKey){
    std::istringstream f(textresult);
    std::string line;
    bool isTimeOut = true;
    while (std::getline(f, line)) {
        if(line.find(infoKey) != std::string::npos){
            isTimeOut = false;
            break;
        }
    }
    if(isTimeOut)
        return "10000"; /*TIMEOUT*/
    std::vector<std::string> infolinevector;
    std::istringstream iss(line);
    for(std::string s; iss >> line; )
        infolinevector.push_back(line);
    std::string info = infolinevector.at(5);
    info.erase(std::prev(info.end()));
    info.erase(std::prev(info.end()));
    return info;
}

std::string getStormLastModelCheckingTime(std::string result, int numIt){
    std::string infoKey = "Time for PLA, iteration " + std::to_string(numIt);
    std::string lastPLATime = getStormPLATime(result, infoKey);

    return lastPLATime;

}

std::string getStormAccumulativeModelCheckingTime(std::string result, int numIt){
    double stormTotalPLATime = 0;
    std::string thisPLATime = "10000";
    if( numIt != 10000){
        for(int i = 1; i < numIt + 1; i ++){
            std::string infoKey = "Time for PLA, iteration " + std::to_string(i);
            thisPLATime = getStormPLATime(result, infoKey);
            if(std::stod(thisPLATime) != 10000)
                stormTotalPLATime += std::stod(thisPLATime);
        }
    }
    std::string accModelCheckingTime = std::to_string(stormTotalPLATime);
    return accModelCheckingTime;

}

std::string getStormTuningTime(std::string textresult, std::string infoKey){
    std::string tuningTime = "";

    /*to be added */
    return tuningTime;
}

std::string getBayesserverInstantiation(std::string textresult){
    std::string infoKey = "instantiation:";
    std::istringstream f(textresult);
    std::string line;
    bool isTimeOut = true;
    while (std::getline(f, line)) {
        if(line.find(infoKey) != std::string::npos){
            isTimeOut = false;
            break;
        }
    }
    if(isTimeOut)
        return "10000"; /*TIMEOUT*/
    std::vector<std::string> infolinevector;
    std::istringstream iss(line);
    for(std::string s; iss >> line; )
        infolinevector.push_back(line);
    std::string info = infolinevector.at(1);
    return info;
}

std::string getBayesserverTuningTime(std::string textresult){
    std::string infoKey = "tuning time:";
    std::istringstream f(textresult);
    std::string line;
    bool isTimeOut = true;
    while (std::getline(f, line)) {
        if(line.find(infoKey) != std::string::npos){
            isTimeOut = false;
            break;
        }
    }
    if(isTimeOut)
        return "10000"; /*TIMEOUT*/
    std::vector<std::string> infolinevector;
    std::istringstream iss(line);
    for(std::string s; iss >> line; )
        infolinevector.push_back(line);
    std::string info = infolinevector.at(2);
    return info;
}


std::string getStormP1NewInstantiation(std::string textresult, std::string infoKey){
    std::istringstream f(textresult);
    std::string line;
    bool isTimeOut = true;
    while (std::getline(f, line)) {
        if(line.find(infoKey) != std::string::npos){
            isTimeOut = false;
            break;
        }
    }
    if(isTimeOut)
        return "10000"; /*TIMEOUT*/
    std::vector<std::string> infolinevector;
    std::istringstream iss(line);
    for(std::string s; iss >> line; )
        infolinevector.push_back(line);
    std::string info = infolinevector.at(1);
    return info;
}


std::string getStormECDistance(std::string textresult, std::string infoKey){
    std::istringstream f(textresult);
    std::string line;
    bool isTimeOut = true;
    while (std::getline(f, line)) {
        if(line.find(infoKey) != std::string::npos){
            isTimeOut = false;
            break;
        }
    }
    if(isTimeOut)
        return "10000"; /*TIMEOUT*/
    std::vector<std::string> infolinevector;
    std::istringstream iss(line);
    for(std::string s; iss >> line; )
        infolinevector.push_back(line);
    std::string info = infolinevector.at(8);
    return info;
}



std::string getBayesserverTotalTime(std::string textresult){
    std::string total_time = "";
    /* to be added */
    return total_time;
}

std::string readInitParVal(std::string fileContent, std::string param){
    std::istringstream f(fileContent);
    std::string line;
    bool isTimeOut = true;
    while (std::getline(f, line)) {
        if(line.find(param) != std::string::npos){
            isTimeOut = false;
            break;
        }
    }

    if(isTimeOut)
        return "0.5"; /*default par init val*/
    std::vector<std::string> infolinevector;
    std::istringstream iss(line);
    for(std::string s; iss >> line; )
        infolinevector.push_back(line);
    std::string info = infolinevector.at(1);
    return info;

}

std::string makeParametersList(std::map<std::string,std::string> initVals){
    std::string parametersList = "";
    if(initVals.size()==0){
        return parametersList;
    }
    std::map<std::string, std::string>::iterator it;
    for (it = initVals.begin(); it != initVals.end(); it++){
        parametersList += it->second + "<=" +  it->first + "<=" + it->second + ",";
    }
    parametersList.erase(std::prev(parametersList.end()));
    return parametersList;
}

std::string makeStormTuningCommand(std::string networkName, std::string instance, /*std::string belowOrAbove, std::string threshhold, in the pctl formula encoded */std::string pctlFormula, std::map<std::string,std::string> initVals, std::string epsilon, std::string refinementFactor, std::string depthLimit, std::string numberOfRegions, std::string subclassStr){
    std::string command = "";
   command += "time timeout " + std::to_string(timeout) + "m " + storm_tuning_executable + " " + storm_benchmarks_directory + "/" + subclassStr + "/" + networkName + "_" + instance + ".drn ";
   //command +=  "\"P" + belowOrAbove + threshhold +  " " + pctlFormula + "\"";
   command += "\"" + pctlFormula + "\"";
   command += " \"";
   command += makeParametersList(initVals);
    command += "\" " + epsilon + " --refThreshold " + refinementFactor /*+  " --depthLimit " +  depthLimit */ + " --numberOfRandom " + numberOfRegions + " --expansionFactor " + std::to_string(expansionFactor) + " --maxAttempts " + std::to_string(maxIterations) + " --paramNum " + std::to_string(numberOfParams);
    std::cout << command << std::endl;
    return command;
}


std::string makeBayesserverCommandP1(std::string networkName ){ /*std::string belowOrAbove, std::string threshhold, and std::string query encoded in the bayesserver config file */
    std::string command = "";
    command += "time timeout " +  std::to_string(timeout) + "m python "  + bayesserver_directory + networkName + "1/" + networkName + "_parameter_tuning.py";
    //std::cout << command << std::endl;
    return command;
}



std::string parseForOneInstance(std::string networkName, std::string instance, std::string pctlFormula, std::map<std::string,std::string> initVals, std::string unusedEpsilon, std::string refinementFactor, std::string depthLimit, std::string numberOfRegions, PBNClass c, Variant v, std::string comparison, std::string threshhold){
    std::string csvcontent = "";


    std::string filePath = outputfiles_directory;
    switch (v) {
        case coverageChanged: {
            filePath +=  networkName + "/" + networkName + "_" + instance + "_storm_" + refinementFactor + ".txt";
            break;
        }
        case threshholdChanged: {
            filePath += "/threshhold-experiments/" + networkName + "/" + networkName + "_" + instance + "_storm_" /*+ comparison*/ + threshhold + ".txt";
            break;
        }

        case epsilonChanged: {
            filePath += "/epsilon-experiments/" + networkName + "/" + networkName + "_" + instance + "_storm_" /*+ comparison*/ + threshhold + "-gamma" + std::to_string(expansionFactor) + "-Iter" +  std::to_string(maxIterations) + ".txt";
            break;
        }
    }

   // std::cout << filePath << std::endl;

    std::string stormResult = readFile(filePath,"");
    std::cout << stormResult;
    std::string numberOfIterations = getStormNumberOfIterations(stormResult, "Number of iterations");

    std::string totalPLATime = getStormAccumulativeModelCheckingTime(stormResult, std::stoi(numberOfIterations));
    std::string lastModelCheckingTime = getStormLastModelCheckingTime(stormResult, std::stoi(numberOfIterations));
    std::string stormECDistance = getStormECDistance(stormResult, "The EC-distance between the original and new instantiation");
    std::string stormP1Instantiation = "";
    std::string bayesserverTuningTime = "";
    std::string bayesserverInstantiation = "";
    std::string baysserverECDistance = "";
    std::string stormbayesserverdistancediff = "";


    std::map<std::string, double> SamIam;
    SamIam["alarm"] = 0.362012; //BP_0
    SamIam["hailfinder"] = 0.832838;
    SamIam["hepar2"] = 0.079602; //Density_0 < 0.1
    SamIam["win95pts"] = 0.274627; //GDIIN_0
    SamIam["sachs"] = 0.97554; //Raf_0

    std::string samiamECDistance = "";
    std::string stormsamiamdistancediff = "";

    switch(c){
        case p1: {
            stormP1Instantiation = getStormP1NewInstantiation(stormResult, "p0=");
            std::string bayesserverResult = readFile(outputfiles_directory + "/" + networkName + "/" + networkName + "_" + instance + "_bayesserver.txt","");
            bayesserverInstantiation = getBayesserverInstantiation(bayesserverResult);
            bayesserverTuningTime = getBayesserverTuningTime(bayesserverResult);
            baysserverECDistance = std::to_string(abs(stod(bayesserverInstantiation) - stod(initVals["p0"])));
            stormECDistance = std::to_string(abs(stod(stormP1Instantiation) - stod(initVals["p0"])));
            stormbayesserverdistancediff = std::to_string(abs(stod(stormP1Instantiation) - stod(bayesserverInstantiation)));
            samiamECDistance = std::to_string(abs(SamIam.at(networkName) - stod(initVals["p0"])));
            stormsamiamdistancediff = std::to_string(abs(stod(stormP1Instantiation) - SamIam.at(networkName)));
            //std::to_string(stold(stormECDistance) - stold(baysserverECDistance));
            std::string zero = "0.000000";
            if(stormbayesserverdistancediff.compare(zero) == 0)
              //  stormbayesserverdistancediff = "0.0000001";
            if(stormECDistance.compare(zero) == 0)
                stormECDistance = "0.001";
            if(stormP1Instantiation.compare("10000") == 0){
                stormECDistance = "10";
            }
            if(stormECDistance.compare("10000") == 0) {
                stormECDistance = "10";
            }
            break;
        }
        default: {

            break; /* Not supported by SamIam and Bayesserver */
        }
    }

    //std::string csvcontent = "networkname,networkinstance,realparamnum,storminstantiation,stormECDistance,stormIterations,stormLastPLAtime,stormtotalTuningtime,p1bayesserverinstantiation,bayesserverECDistance, p1bayesservertuningtime\n";
    switch(c){

        //networkname,networkinstance,refinementFactor,coverageFactor,storminstantiation,stormECDistance,stormiteration,stormLastPLAtime,stormtotaltuningime,p1bayesserverinstantiation,p1bayesserverECDistance,p1bayesservertuningtime,stormbayesserverdistancediff,stormbayesservertimediff,samiamEC,stormsamiamdiff
        case p1: csvcontent += networkName + "," + instance + "," + ((refinementFactor)) + "," + std::to_string(1.0- stod(refinementFactor)) + "," + stormP1Instantiation + "," + stormECDistance + "," + numberOfIterations + "," + std::to_string(stod(lastModelCheckingTime)) + "," + totalPLATime + "," + bayesserverInstantiation + "," + baysserverECDistance + "," + bayesserverTuningTime +
                + "," + stormbayesserverdistancediff  + "," + std::to_string((stod(totalPLATime) - stold(bayesserverTuningTime))) + "," + samiamECDistance + "," + stormsamiamdistancediff + "," + std::to_string(expansionFactor) + "," + std::to_string(maxIterations) + "," + std::to_string(epsilon) + "\n";
        case pstar: break;
    }

    return csvcontent;
    /* to be completed */
}


void runForOneInstance(std::string networkName, std::string instance, /*std::string belowOrAbove, std::string threshhold, encoded in the pctlformula */ std::string pctlFormula, std::map<std::string,std::string> initVals, std::string epsilon, std::string refinementFactor, std::string depthLimit, std::string numberOfRegions, PBNClass c, std::string subclassStr, Variant v, std::string comparison, std::string threshhold){
    std::string stormcommand = "";
    std::string stormresult = "";

    stormcommand = makeStormTuningCommand(networkName, instance, pctlFormula, initVals, epsilon, refinementFactor, depthLimit, numberOfRegions, subclassStr);
    std::cout << stormcommand << std::endl;
    const char *cmnd = stormcommand.c_str();
    try{
        stormresult = exec(cmnd);
    }
    catch(const std::exception& e){
        stormresult = -1;
    }

    std::cout << "This point1" << std::endl;
    std::string filePath = outputfiles_directory;
    switch (v) {
        case coverageChanged: {
            filePath += networkName + "/" + networkName + "_" + instance + "_storm_" + refinementFactor + ".txt";
            break;
        }
        case threshholdChanged: {
            filePath += "threshhold-experiments/" + networkName + "/" + networkName + "_" + instance + "_storm_" /*+ comparison */ + threshhold + ".txt";
            break;
        }
        case epsilonChanged: {
            filePath += "epsilon-experiments/" + networkName + "/" + networkName + "_" + instance + "_storm_" /*+ comparison*/ + threshhold + "-gamma" + std::to_string(expansionFactor) + "-Iter" +  std::to_string(maxIterations) + ".txt";
            std::cout << "filePath" << filePath << std::endl;
            break;
        }
    }

    std::cout << "This point1" << "filePath" << std::endl;

    writeFile(filePath, stormresult);

    std::cout << stormresult;
    std::cout << "This point1" << std::endl;



    std::string bayesservercommand = "";
    std::string bayesserverresult = "";
    switch(c)
    {
        case p1: {
            bayesservercommand = makeBayesserverCommandP1(networkName);
            const char *cmnd2 = bayesservercommand.c_str();
            try {
                bayesserverresult = exec(cmnd2);
            }
            catch (const std::exception &e) {
                bayesserverresult = -1;
            }
           // writeFile(filePathPrefix + "_bayesserver.txt", bayesserverresult);
            break;
        }
        case pstar: break; /* pstart class is not supported by bayesserver */
    }
}



/* Storm vs Bayesserver */
void runTuningExperiments(PBNClass subclass, std::string subclassStr, int numpars){
    numberOfParams = numpars;
    std::string networks[3] = {"andes","pathfinder","barley"}; //hepar2{"cancer", "asia", "earthquake" , "sachs", "alarm", "win95pts", "hepar2", "hailfinder", "insurance", "water","andes"};//  "pathfinder", "barley"};
    std::string refinementFactors[18] = {"0.5","0.45","0.4","0.35","0.3","0.25","0.20","0.15","0.10","0.05","0.04","0.03","0.02","0.01","0.001","0.0001","0.00001","0.000001"}; //,"0.0000001","0.00000001","0.000000001","0.0000000001","0.00000000001"};
    for(int i = 0; i < 3; i++){
        std::string pctlFilePath = storm_benchmarks_directory + "/" + subclassStr + "/" + "storm_prop_files" + "/" + networks[i] + ".pctl";
        std::string pctlformula = readFile(pctlFilePath ,"P>=0 [F(true)]");
        std::string initFilePath = storm_benchmarks_directory + "/" + subclassStr + "/" + networks[i] + "_" + subclassStr + ".init";
        std::string initFile = readFile(initFilePath,"");
        std::map<std::string, std::string> initVals;
        for(int i = 0; i < numpars; i ++){
            std::string parName = "p" + std::to_string(i);
            std::string parVal = readInitParVal(initFile, parName);
            initVals.insert(std::pair<std::string, std::string>(parName, parVal));
        }
        for(int j = 0; j < 18; j++)
            runForOneInstance(networks[i], subclassStr, pctlformula, initVals, "0.0625", refinementFactors[j], "10","10000",subclass, subclassStr, coverageChanged, "-", "0");
    }
}



std::string parseTuningExperiments(PBNClass subclass, std::string subclassStr, int numpars){
    std::string header = "networkname,networkinstance,refinementFactor,coverageFactor,storminstantiation,stormECDistance,stormiteration,stormLastPLAtime,stormtotaltuningime,p1bayesserverinstantiation,p1bayesserverECDistance,p1bayesservertuningtime,stormbayesserverdistancediff,stormbayesservertimediff,samiamEC,stormsamiamdiff\n";

    std::string fullcsvcontent = header;

    std::string networks[3] = {"andes","pathfinder","barley"}; // {"win95pts","hepar2","alarm","hailfinder","sachs"};//hepar2{"cancer", "asia", "earthquake" , "sachs", "alarm", "win95pts", "hepar2", "hailfinder", "insurance", "water","andes"};// "andes", "pathfinder", "barley"};
    //std::string refinementFactors[23] = {"0.5","0.45","0.4","0.35","0.3","0.25","0.20","0.15","0.10","0.05","0.04","0.03","0.02","0.01","0.001","0.0001","0.00001","0.000001","0.0000001","0.00000001","0.000000001","0.0000000001","0.00000000001"};
    //std::string refinementFactors[6] = {"0.10","0.01","0.001","0.0001","0.00001","0.000001"};//,"0.0000001","0.00000001","0.000000001","0.0000000001","0.00000000001"};
    std::string refinementFactors[18] = {"0.5","0.45","0.4","0.35","0.3","0.25","0.20","0.15","0.10","0.05","0.04","0.03","0.02","0.01","0.001","0.0001","0.00001","0.000001"}; //,"0.0000001","0.00000001","0.000000001","0.0000000001","0.00000000001"};


    for(int i = 0; i < 3; i++){
        std::string pctlFilePath = storm_benchmarks_directory + "/" + subclassStr + "/" + "storm_prop_files" + "/" + networks[i] + ".pctl";
        std::string pctlformulaFullformat = readFile(pctlFilePath ,"P>=0 [F(true)]");
        std::string initFilePath = storm_benchmarks_directory + "/" + subclassStr + "/" + networks[i] + "_" + subclassStr + ".init";
        std::string initFile = readFile(initFilePath,"");
        std::map<std::string, std::string> initVals;
        for(int i = 0; i < numpars; i ++){
            std::string parName = "p" + std::to_string(i);
            std::string parVal = readInitParVal(initFile, parName);
            initVals.insert(std::pair<std::string, std::string>(parName, parVal));
        }
        std::string thiscsvcontent = header;
        for(int j = 0; j < 6; j++){
            std::string thisRow = parseForOneInstance(networks[i], subclassStr, pctlformulaFullformat, initVals, "0.0625", refinementFactors[j], "10","10000",subclass, coverageChanged, "-", "0") + "\n";
            thiscsvcontent += thisRow;
            fullcsvcontent += thisRow;
        }
      //  std::cout << thiscsvcontent;
        writeFile(csvfiles_directory + networks[i] + "-" + subclassStr + "-coverage.csv", thiscsvcontent);
    }

    std::cout << fullcsvcontent;
    return fullcsvcontent;

}


std::string runTuningExperimentsThreshholdChanges(){


    std::string header = "thresshold,networkname,networkinstance,refinementFactor,coverageFactor,storminstantiation,stormECDistance,stormiteration,stormLastPLAtime,stormtotaltuningime,p1bayesserverinstantiation,p1bayesserverECDistance,p1bayesservertuningtime,stormbayesserverdistancediff,stormbayesservertimediff,samiamEC,stormsamiamdiff\n";
    std::string csvcontent = header;


    /* pBN Info */
   /* std::string networks[4] = {"hepar2","win95pts","alarm","hailfinder"};
    PBNClass subclass[4] = {p2, p2, p2, p2};
    std::string subclassStr[4] = {"p2","p2","p2","p2"};
    int numpars[4] = {2,2,2,2}; */

     std::string networks[2] = {"win95pts","sachs"};//{"hepar2","win95pts","alarm","hailfinder"};
    PBNClass subclass[2] = {p1, p1};//, p1, p1};
    std::string subclassStr[2] = {"p1","p1"};//,"p1","p1"};
    int numpars[2] = {1,1};//,1,1};


    std::string refinementFactors[2] = {"0.0000001", "0.0000001"};//,"0.0000001","0.0000001"}; /* 0.01 refinement = 99 % coverage */


    std::string threshhold[14] = {"0.3","0.35","0.4","0.45","0.5","0.55","0.6","0.65","0.7","0.75","0.8","0.85","0.9","0.95"};



    for(int i = 0; i < 2; i++){

        numberOfParams = numpars[i];
        std::string initFilePath = storm_benchmarks_directory + "/" + subclassStr[i] + "/" + networks[i] + "_" + subclassStr[i] + ".init";
        std::string initFile = readFile(initFilePath,"");
        std::map<std::string, std::string> initVals;
        for(int k = 0; k < numpars[i]; k ++){
            std::string parName = "p" + std::to_string(k);
            std::string parVal = readInitParVal(initFile, parName);
            initVals.insert(std::pair<std::string, std::string>(parName, parVal));
        }


        std::string thisNetworkcsv = header;

        for(int j = 0; j < 14; j++) {
            /* constraint Info */
            std::string hypFilePath = storm_benchmarks_directory + "/" + subclassStr[i] + "/storm_prop_files/" + networks[i] + ".hyp";
            std::string hyp = readFile(hypFilePath ,"true");
            std::string comparisonFac[4] = {">=",">=",">=",">="};
            std::string pctlformula = "P" + comparisonFac[i] + threshhold[j] + " [F(\\\" "  + hyp + "\\\")]";
            std::cout << pctlformula << std::endl;

            //runForOneInstance(networks[i], subclassStr[i], pctlformula, initVals, "0.0625", refinementFactors[i], "10", "10000", subclass[i], subclassStr[i], threshholdChanged, comparisonFac[i], threshhold[j]);
            std::string term = threshhold[j] + "," +
                          parseForOneInstance(networks[i], subclassStr[i], pctlformula, initVals, "0.0625", refinementFactors[i], "10", "10000", subclass[i], threshholdChanged, comparisonFac[i], threshhold[j]);
            csvcontent += term;
            thisNetworkcsv += term;
           // std::cout << term << std::endl;
        }

        writeFile(csvfiles_directory + networks[i] + "-" + subclassStr[i] + "-" + "thresh-10-7.csv" , thisNetworkcsv);
        std::cout << csvcontent;
        writeFile(csvfiles_directory + "p1-cov99.99999-coverage-experiments-results.csv", csvcontent);
    }
}


std::string runTuningExperimentsEpsilonChanges(){


    std::string header = "thresshold,networkname,networkinstance,refinementFactor,coverageFactor,storminstantiation,stormECDistance,stormiteration,stormLastPLAtime,stormtotaltuningime,p1bayesserverinstantiation,p1bayesserverECDistance,p1bayesservertuningtime,stormbayesserverdistancediff,stormbayesservertimediff,samiamEC,stormsamiamdiff,regionExpansionFac,maxIter,epsilon\n";
    std::string csvcontent = header;


    /* pBN Info */
    /* std::string networks[4] = {"hepar2","win95pts","alarm","hailfinder"};
     PBNClass subclass[4] = {p2, p2, p2, p2};
     std::string subclassStr[4] = {"p2","p2","p2","p2"};
     int numpars[4] = {2,2,2,2}; */

    std::string networks[1] = {"win95pts"};//{"hepar2","alarm","hailfinder"};
    PBNClass subclass[1] = {p4}; //, p4,p4};
    std::string subclassStr[1] = {"p4"}; //"p4","p4"};
    int numpars[1] = {4}; //,4,4};

    std::string comparisonFac = ">=";

    //std::string closeThreshhold = "0.3";
    //std::string mediumThreshhold = "0.6";
    //std::string farThreshhold = "0.9";

    std::string threshholdCategory[4] = {"sat","close","medium","far"};

    std::string threshhold[4] = {"0.3","0.115","0.25","0.45"};

   // std::string threshhold[4] = {"0.3","0.25","0.6","0.9"};






    std::string refinementFactors[1] =  {"0.2"}; //,"0.2","0.2"};//{"0.0000001", "0.0000001","0.0000001"};//,"0.0000001","0.0000001"}; /* 0.01 refinement = 99 % coverage */




    double regionExpansionFactors[3] = {1.25,2,5};
    //int maxIters[4] = {2,4,6,8};
    int maxIters[2] = {10,5};


    for(int i = 0; i < 1; i++){

        numberOfParams = numpars[i];

        std::string initFilePath = storm_benchmarks_directory + "/" + subclassStr[i] + "/" + networks[i] + "_" + subclassStr[i] + ".init";
        std::string initFile = readFile(initFilePath,"");
        std::map<std::string, std::string> initVals;
        for(int k = 0; k < numpars[i]; k ++){
            std::string parName = "p" + std::to_string(k);
            std::string parVal = readInitParVal(initFile, parName);
            initVals.insert(std::pair<std::string, std::string>(parName, parVal));
        }

        std::string hypFilePath = storm_benchmarks_directory + "/" + subclassStr[i] + "/storm_prop_files/" + networks[i] + ".hyp";
        std::string hyp = readFile(hypFilePath ,"true");


        for(int x = 0; x < 4; x++) { //threshholds


            std::string pctlformula = "P" + comparisonFac + threshhold[x] + " [F(\\\" " + hyp + "\\\")]";
            std::cout << pctlformula << std::endl;


            std::string thisNetworkcsv = header;

            for (int d = 0; d < 2; d++) { /*maxIterations */

                    for (int j = 0; j < 3; j++) { /* expansion factors */


                    epsilon = pow(1 / double(regionExpansionFactors[j]), maxIters[d] - 1);
                    maxIterations = maxIters[d];
                    expansionFactor = regionExpansionFactors[j];

                    runForOneInstance(networks[i], subclassStr[i], pctlformula, initVals, "0.0625",
                                      refinementFactors[i],
                                      "10", "10000", subclass[i], subclassStr[i], epsilonChanged, comparisonFac,
                                      threshhold[x]);
                   std::string term = threshhold[x] + "," +
                                       parseForOneInstance(networks[i], subclassStr[i], pctlformula, initVals, "0.0625",
                                                           refinementFactors[i], "10", "10000", subclass[i],
                                                           epsilonChanged, comparisonFac, threshhold[x]);
                    csvcontent += term;
                    thisNetworkcsv += term;
                    std::cout << term << std::endl;
                }
            }
            writeFile(csvfiles_directory + networks[i] + "-" + subclassStr[i] + "-expansion-" + threshholdCategory[x] + "-gamma" + std::to_string(expansionFactor) + "-Iter" +  std::to_string(maxIterations) + ".csv", thisNetworkcsv);
            std::cout << csvcontent;
        }


        writeFile(csvfiles_directory + "expansion-multiple-settings-experiments.csv", csvcontent);
    }
}



void runAndParseTuningExperimentsPn() {
}



int main() {

    runTuningExperimentsEpsilonChanges();



 /* double regionExpansionFactors[4] = {1.25,2,2.5,5};
    int maxIters[3] = {2, 4, 6};

    for(int j = 0; j < 4; j++) { /* expansion factors */

   /*  for (int k = 0; k < 3; k++) {
            double epsilon = pow(1/(regionExpansionFactors[j]), maxIters[k] - 1);
            std::cout << regionExpansionFactors[j] << "," << maxIters[k] << "epsilon: " << std::to_string(epsilon) << std::endl;
    }
    } */

    /* double param = 5.5;
    double result = log (param);
    printf ("log(%f) = %f\n", param, result );

    typedef std::numeric_limits< double > dbl;

    double inst = 0.07960198270809421;
    0.079601981460897225
    0.079601981460897225
    std::cout.precision(dbl::max_digits10);
    std::cout << "inst: " << inst << std::endl;
    std::cout << log(param) << std::endl; */

    //runTuningExperimentsThreshholdChanges();

   // runTuningExperiments(p1, "p1", 1);

   // parseTuningExperiments(p1, "p1", 1);

    //std::string csvcontent = parseTuningExperiments(p1, "p1", 1);
    // runTuningExperiments(p2, "p2", 2);
    // std::string csvcontent = parseTuningExperiments(p2, "p2", 2);

   // runTuningExperiments(p4, "p4", 4);
   // csvcontent = parseTuningExperiments(p4, "p4", 4);

   // runTuningExperiments(p8, "p8", 8);
   // std::string csvcontent = parseTuningExperiments(p8, "p8", 8);
    //std::cout << csvcontent;
    //writeFile(csvfiles_directory + "full-p1-tuning-results.csv", csvcontent);
    return 0;
}

