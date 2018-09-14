for((i=0;i<64;i++)); do 
  python3 Present.py 9 ${i} > cvc/${i}.cvc & 
done

for job in `jobs -p`; do
  wait $job
done

for ((i=0;i<64;i++)); do 
  stp cvc/${i}.cvc --cryptominisat --threads 1 > cvc/res/${i}.res & 
done

for job in `jobs -p`; do 
  wait $job
done

ls -l cvc/res  | grep '7 Jul' 

