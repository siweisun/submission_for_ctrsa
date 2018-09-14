for((i=0;i<$1;i++)); do 
  for ((j=0;j<$1;j++)); do
    stp cvc_$1/${i}_${j}.cvc > cvc_$1/res/${i}_${j}.res&
  done
  for job in `jobs -p`; do
    wait $job
  done
done


echo 'change the filter condition to fit your computer' >> $2
ls -l cvc_$1/res | grep '7 Sep' >> $2

