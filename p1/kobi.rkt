#lang racket
(require rackunit)
(define PI 3.14159265359)
;#####################
; Problem 1
;#####################

(define (integral func num-steps x1 x2)
  ; define a step for each movement. 
  (define step (/ (- x2 x1) num-steps))
  ; define the sum.
  (define sum 0)
  ; the sum of the function value times the small step
  (define (func-rect x1 x2) (* ( - x2 x1) (func x1)))
  
  (for([i num-steps])
    (set! sum (+ sum (func-rect (+ x1 (* i step)) (+ x1 (* (add1 i) step))))))
  (+ sum 0))

 
(test-eq? "x^2 integral with 1 step" (integral (lambda (x) (expt x 2)) 1 3 5) 18)
(test-eq? "x^2 integral with 2 steps" (integral (lambda (x) (expt x 2)) 2 3 5) 25)
(test-eq? "x^3 integral with 2 steps" (integral (lambda (x) (expt x 3)) 2 3 5) 91)

;######################
; Problem 2
;######################

(define (approx-pi num-steps)
  (integral (lambda (x) (* 4 (sqrt (- 1 (expt x 2))))) num-steps 0 1)
)
(test-eq? "approx pi with a single step " (approx-pi 1) 4)
(test-= "test approx-pi with 600 steps should be Pi with a two decimal precision "
        (approx-pi 600) 3.14 0.01)

;######################
; Problem 3
;######################

(define (rectangle func x1 x2)
   (* ( - x2 x1) (func x1)))

(define (trapezoid func x1 x2)
   (/ (* ( - x2 x1) (+ (func x1) (func x2))) 2))

(define (integral-with piece func num-steps x1 x2)
  ; define a step for each movement. 
  (define step (/ (- x2 x1) num-steps))
  ; define the sum.
  (define sum 0)
  
  (for([i num-steps])
    (set! sum (+ sum (piece func (+ x1 (* i step)) (+ x1 (* (add1 i) step))))))
  (+ sum 0))

(test-eq? "test a rectangle piece function of x^2 should be (1)^2 times the length(3)"
          (rectangle (lambda(x) (expt x 2)) 1 4) 3)
(test-eq? "test a rectangle function of x^2 should be (2)^2 times the length(5)"
          (rectangle (lambda(x) (expt x 2)) 2 7) 20)

(test-= "test a trapezoid function of x^2 should be [(1)^2 + (4)^2 times the length(3)]/ 2"
          (trapezoid (lambda(x) (expt x 2)) 1 4) 25.5 0.001)
(test-= "test a trapezoid function of x^2 should be [(2)^2 + (7)^2 times the length(5)] / 2"
          (trapezoid (lambda(x) (expt x 2)) 2 7) 132.5 0.001)

;###################
;Problem 4
;###################
(define (better-pi num-steps)
  (integral-with trapezoid (lambda (x) (* 4 (sqrt (- 1 (expt x 2))))) num-steps 0 1)
)
(test-true "test that better-pi gives a closer approx. to pi,  then approx-pi "
          ( < (abs (- PI (better-pi 600))) (abs (- PI (approx-pi 600)))))
