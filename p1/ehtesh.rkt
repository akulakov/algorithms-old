#lang racket

(define PI 3.14159265359)
(provide (all-defined-out))

(define (rectangle func x1 x2)
  (* (func x1) (- x2 x1)))

;; TODO debug later
(define (trapezoid func x1 x2)
  (let ([diff (- x2 x1)]
        [min-func-x (min (func x1) (func x2))]
        [base (abs (- (func x1) (func x2)))])
    ; area_trap = area_tri + area_rect
    (+ (* base diff 1/2)
       (* min-func-x diff))))

;; TODO simpson's rule
(define (simpson-rule func x1 x2)
  'your-code-here)

(define (integral-with piece func num-steps x1 x2)
  (let ([slice (/ (- x2 x1) num-steps)])
    ;(printf "integral ~a ~a ~a ~a ~n" num-steps x1 x2 slice)
    (foldl + 0
      (for/list ([i (in-range x1 (+ x2 0) slice)])
        ;(printf "x: ~a, y:~a piece(i,i+slice):~a~n" i (func i) (piece func i (+ i slice)))
        (piece func i (+ i slice))))))

(define (integral func num-steps x1 x2)
  (integral-with rectangle func num-steps x1 x2))

(define (square x) (* x x))
(define (cube x) (* x x x))
(define (xy x) x)
(define (line x) 5)
(define (func-circle x)
  (sqrt (- 1 (expt x 2))))

(define (approx-pi num-steps)
    (* 4 (integral func-circle num-steps 0 1)))

(define (better-pi num-steps)
    (* 4 (integral-with trapezoid func-circle num-steps 0 1)))

(define (deriv-constant constant wrt) 0)

(define (deriv-variable var wrt)
    (if (equal? var wrt) 1 0))

; TODO is this the right way? Currying is useful though.
; TODO is there a way without re-using 'derivative?
; TODO maybe map doesn't make sense when there is only 2 elements, unless deriv-product generalizes for N elements
(define (deriv-sum var wrt)
  (cons '+ (map (curry derivative wrt) (rest var))))

(define (deriv-product var wrt)
  (let ([A (second var)]
        [B (third var)])
  (list '+
        (list '* A (derivative B wrt))
        (list '* (derivative A wrt) B ))))

; this looks like it could be expanded to a real CAS! Cool...
(define (derivative expr wrt)
(cond
  [(integer? expr) (deriv-constant expr wrt)]
  [(symbol? expr) (deriv-variable expr wrt)]
  [(list? expr)
   (cond
     [(equal? '+ (first expr)) (deriv-sum expr wrt)]
     [(equal? '* (first expr)) (deriv-product expr wrt)]

     (else (error "Don't know how to differentiate" expr)))]
  (else (error "Don't know how to differentiate" expr))))

;; ================== TESTS ==================

;;; With only one step, the integral of y = x^2 from 3 to 5
;;; should be 3^2 * 2 = 18
;(integral (lambda (x) (expt x 2)) 1 3 5)
;;; With two steps, we should get 3^2 + 4^2 = 25
;(integral (lambda (x) (expt x 2)) 2 3 5)

;(integral-with trapezoid (lambda (x) (expt x 2)) 1 3 5)
;(integral-with trapezoid (lambda (x) (expt x 2)) 2 3 5)

;(approx-pi 1)   ;; Should be 4
;(approx-pi 2)   ;; Hopefully lower than 4
;(approx-pi 600) ;; Right to the first two decimal places?

;(better-pi 1)
;(better-pi 2)
;(better-pi 600)

;(deriv-variable 'y 'x) ;; Should be 0
;(deriv-variable 'x 'x) ;; Should be 1
;(deriv-constant 0 'x) ;; Should be 0
;(deriv-sum '(+ x 2) 'x) ; -> (+ 1 0)
;(deriv-product '(* x 3) 'x) ; -> (+ (* x 0) (* 1 3))
;(derivative 3 'x) ; -> 0
;(derivative 'x 'x) ; -> 1
;(derivative '(+ x 2) 'x) ; -> (+ 1 0)
;(derivative '(* x 3) 'x) ; -> (+ (* x 0) (* 1 3))

