#lang racket

; bitfunc function :
(define (bitfunc x)(+ (expt x 4) (* -5 (expt x 2)) 4))
; bitfunc rect function:
(define (bitfunc-rect x1 x2) (* ( - x2 x1) (bitfunc x1)))

(define (bitfunc-integral-recur num-steps x1 x2)
  ; define a step for each movement. 
  (define step (/ (- x2 x1) num-steps))
    ; define a helper function
  (define (recuresion-helper x1 x2 sum num-steps) 
    (if (= num-steps 0) sum ( recuresion-helper (- x1 step) (- x2 step) (+ sum (bitfunc-rect x1 x2)) (sub1 num-steps))))
  ; call helper function
  (recuresion-helper (- x2 step) x2 0 num-steps))

; bitfunc integral iteration
(define (bitfunc-integral-iter num-steps x1 x2)
    ; define a step for each movement. 
  (define step (/ (- x2 x1) num-steps))
  (define sum 0)
  (for([i num-steps])
    (set! sum (+ sum (bitfunc-rect (+ x1 (* i step)) (+ x1 (* (add1 i) step))))))
  (+ sum 0))

(define (bitfunc-integral-difference num-steps x1 x2)
  (abs (- (bitfunc-integral-iter num-steps x1 x2) (bitfunc-integral-recur num-steps x1 x2))))

