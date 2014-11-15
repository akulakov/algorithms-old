#lang racket

(define (bitfunc x)
  (+ (- (expt x 4) (* 5 (expt x 2))) 4))

(define (bitfunc-rect x1 x2)
  (* (- x2 x1) (bitfunc x1)))

(define (bitfunc-integral-recur num-steps x1 x2)
  (if (= num-steps 0)
    0 
    (let [[slice (+ x1 (/ (- x2 x1) num-steps))]]
        (+ (bitfunc-integral-recur (- num-steps 1) 
                                      slice
                                      x2)
           (bitfunc-rect x1 slice)))))

(define (bitfunc-integral-iter num-steps x1 x2)
  (let [[slice (+ x1 (/ (- x2 x1) num-steps))]]
    (foldl 
      + 
      0 
      (for/list ([i (in-range x1 x2 slice)])
        (bitfunc-rect i (+ i slice))))))
