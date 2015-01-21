#!/bin/bash

# Loop over events
for event in 759
do
    echo '***************************************************'
    echo 'Beginning generating frames for event =' $event'...'
    echo '***************************************************'
    
    # Create event directory if it doesn't exist
    resultsDir="results-`echo $event`"
    if [ ! -d "$resultsDir" ]
    then
        mkdir $resultsDir
    fi
    
    dataFile="averaged_S_on_FOsurface_ev`echo $event`.dat"
    
    # Loop over TDEP versions
    for TDEPV in 2 3 4
    do
        # Create TDEP directory if it doesn't exist
        TDEPVsubDir="`echo $resultsDir`/TDEP_V`echo $TDEPV`"
        if [ ! -d "$TDEPVsubDir" ]
        then
            mkdir $TDEPVsubDir
        fi
        
        sourceDirec="/home/plumberg.1/HBTwidths_viscosity_dependence/RESULTS/RESULTS_etaBYs_0.08/NEW_TDEP_V`echo $TDEPV`/NEW_TDEP_V`echo $TDEPV`_results-`echo $event`"
        sourceFile=$sourceDirec/$dataFile
        
        echo '  --> Submitting KT jobs for event =' $event', TDEPV =' $TDEPV'...'
        
        # Loop over KT values
        for KTval in 0.0 0.5 1.0 1.5 2.0
        do
            # Create KT directory if it doesn't exist
            KTsubsubDir="`echo $TDEPVsubDir`/KT_`echo $KTval`"
            if [ ! -d "$KTsubsubDir" ]
            then
                mkdir $KTsubsubDir
            fi
            
            python generate_rotating_figure_1.py $KTval $sourceFile $KTsubsubDir &> $KTsubsubDir/generate_rotating_figure_1.out &
        done
        
        echo '  --> Waiting on KT jobs for event =' $event', TDEPV =' $TDEPV 'to finish...'
        wait
        echo '  --> Finished KT jobs for event =' $event', TDEPV =' $TDEPV'.'
        echo
    done
    
    echo '***************************************************'
    echo 'Finished generating frames for event =' $event'.'
    echo '***************************************************'
    echo
    echo
done

echo 'Finished all.'
