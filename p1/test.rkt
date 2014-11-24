#lang racket

(require rackunit/text-ui)
(require rackunit)
(require "p1.rkt")
(define-test-suite p1-tests 
                            (test-suite
                             " tests for Problem 1 "
                             (test-eq? "x^2 integral with 1 step" (integral (lambda (x) (expt x 2)) 1 3 5) 18)
                             (test-eq? "x^2 integral with 2 steps" (integral (lambda (x) (expt x 2)) 2 3 5) 25)
                             (test-eq? "x^3 integral with 2 steps" (integral (lambda (x) (expt x 3)) 2 3 5) 91))
                            
                            
                            
                            (test-suite
                             " tests for Problem 2 "
                             (test-eq? "approx pi with a single step " (approx-pi 1) 4)
                             (test-= "test approx-pi with 600 steps should be Pi with a two decimal precision "
                                     (approx-pi 600) 3.14 0.01))
                            
                            
                            
                            (test-suite
                             " tests for Problem 3 "
                             (test-eq? "test a rectangle piece function of x^2 should be (1)^2 times the length(3)"
                                       (rectangle (lambda(x) (expt x 2)) 1 4) 3)
                             (test-eq? "test a rectangle function of x^2 should be (2)^2 times the length(5)"
                                       (rectangle (lambda(x) (expt x 2)) 2 7) 20)
                             (test-= "test a trapezoid function of x^2 should be [(1)^2 + (4)^2 times the length(3)]/ 2"
                                     (trapezoid (lambda(x) (expt x 2)) 1 4) 25.5 0.001)
                             (test-= "test a trapezoid function of x^2 should be [(2)^2 + (7)^2 times the length(5)] / 2"
                                     (trapezoid (lambda(x) (expt x 2)) 2 7) 132.5 0.001))
                            
                            
                            
                            (test-suite
                             " tests for Problem 4 "
                             (test-true "test that better-pi gives a closer approx. to pi,  then approx-pi "
                                        ( < (abs (- PI (better-pi 600))) (abs (- PI (approx-pi 600))))))
                            
                            
                            
                            (test-suite
                             " tests for Problem 5 "
                             (test-eq? "test for derivation using same var. " (deriv-variable 'x 'x) 1)
                             (test-eq? "test for derivation using different var. " (deriv-variable 'x 'y) 0))
                            
                            
                            
                            (test-suite
                             " tests for Problem 7 "
                             (test-equal? "test for sum derivation" (deriv-sum '(+ x 2) 'x) '(+ 1 0))
                             (test-equal? "test for sum derivation" (derivative '(+ x 2) 'x) '(+ 1 0)))
                            
                            
                            
                            (test-suite
                             " tests for Problem 8 "
                             (test-true "test for product derivation" (or (equal? (deriv-product '(* x 3) 'x) '(+ (* x 0) (* 1 3)))
                                                                          (equal? (eval (deriv-product '(* x 3) 'x)) 3)))))

(run-tests p1-tests)