for((i=0;i<$1;i++)); do 
  stp cvc_$1_$2/${i}.cvc --cryptominisat --threads 2 > cvc_$1_$2/res/${i}.res&

done


  for job in `jobs -p`; do
     wait $job
  done

ls -l cvc_$1_$2/res >> $3

  for job in `jobs -p`; do
     wait $job
  done
