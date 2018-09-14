if [ ! -d "Result/" ]; then
    mkdir Result/ && touch Result/res_$1_$2.txt
else touch Result/res_$1_$2.txt
fi

# we will print results information to Result/res_$1_$2.txt
touch Result/res_$1_$2.txt
echo "SIMON$1 ROUND $2" > Result/res_$1_$2.txt
echo "" >> Result/res_$1_$2.txt
date >> Result/res_$1_$2.txt

echo "" >> Result/res_$1_$2.txt

if [ ! -d "cvc_$1_$2_FOR_K/" ]; then
    mkdir cvc_$1_$2_FOR_K && mkdir cvc_$1_$2_FOR_K/res/
elif [ ! -d "cvc_$1_$2_FOR_K/res/" ]; then
    mkdir cvc_$1_$2_FOR_K/res/
fi
    
for((i=0;i<$1;i++)); do
    python3 simon3.py $1 $2 $i 0 > cvc_$1_$2_FOR_K/$i.cvc &
done

for job in `jobs -p`; do
   wait $job
done
 
for((i=0;i<$1;i++)); do 
  stp cvc_$1_$2_FOR_K/${i}.cvc --cryptominisat --threads 2 > cvc_$1_$2_FOR_K/res/${i}.res &
done

for job in `jobs -p`; do
   wait $job
done
 

if [ ! -d "cvc_$1_$2_FOR_L/" ]; then
    mkdir cvc_$1_$2_FOR_L && mkdir cvc_$1_$2_FOR_L/res/
elif [ ! -d "cvc_$1_$2_FOR_L/res/" ]; then
    mkdir cvc_$1_$2_FOR_L/res
fi
    
for((i=0;i<$1;i++)); do
    python3 simon3.py $1 $2 $i 1 > cvc_$1_$2_FOR_L/$i.cvc &
done

for job in `jobs -p`; do
   wait $job
done
 
for((i=0;i<$1;i++)); do 
  stp cvc_$1_$2_FOR_L/${i}.cvc --cryptominisat --threads 2 > cvc_$1_$2_FOR_L/res/${i}.res &
done

for job in `jobs -p`; do
   wait $job
done
 

# output the running results to the result file, you can add a "grep" to filter the results
# since the results of "ls -l" depend on the machine, we cannot predefine it the "grep" statement,
echo "The results for K, 7 for 'VALID.\n'(Infeasible) and 9 for 'Invalid.\n'(feasible)" >> Result/res_$1_$2.txt 
ls -l cvc_$1_$2_FOR_K/res >> Result/res_$1_$2.txt
echo "" >> Result/res_$1_$2.txt

echo "The results for L, 7 for 'VALID.\n'(Infeasible) and 9 for 'Invalid.\n'(feasible)" >> Result/res_$1_$2.txt 
ls -l cvc_$1_$2_FOR_L/res >> Result/res_$1_$2.txt
echo "" >> Result/res_$1_$2.txt
echo "Please check the results for K first and then check those of L manually" >> Result/res_$1_$2.txt

date >> Result/res_$1_$2.txt

cat Result/res_$1_$2.txt

