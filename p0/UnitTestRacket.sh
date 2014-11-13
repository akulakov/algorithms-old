#!/bin/bash


####################################
# Add a prefix out for each Module #
####################################
for f in *.rkt
do
    name="${f%.*}"
    echo "\n    (provide(prefix-out "$name": (all-defined-out)))" >> $f
done

##########################################
# Create Test Module and add a few tests #
##########################################

echo '#lang racket' >> test.txt
echo '(require rackunit)' >> test.txt

for f in *.rkt
do
    echo "(require \"$f\")" >> test.txt
done
##########################################
# Create Test Module and add a few tests #
##########################################
echo  '(module+ test' >> test.txt
echo -n '(check-equal?' >> test.txt

for f in *.rkt
do
    name="${f%.*}" 
    echo -n " ($name:bitfunc 2)" >> test.txt
done
echo -n " 0" >> test.txt
echo -n " \"Simple bitFunc\")" >> test.txt
echo -n ')' >> test.txt
mv test.txt test.rkt

#########################
# Complie and run tests #
#########################

sh ~/projects/racket/racket/bin/raco make test.rkt
sh ~/projects/racket/racket/bin/raco test -x .


#################################
# Remove the Provide from files #
#################################
for f in *.rkt
do
    sed -i '$ d' $f
    
done

rm -f test.rkt

