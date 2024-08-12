(define (square n) (* n n))

(define (pow base exp) 
        (cond ((zero? exp) 1)
              ((odd? exp) (* base (pow base (- exp 1))))
              ((even? exp) (square (pow base (quotient exp 2))))))

(define (repeatedly-cube n x)
  (if (zero? n)
      x
      (let ((y (repeatedly-cube (- n 1) x)))
        (* y y y))))

(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s))) 

(define (caddr s) (car (cddr s)))

(define (ascending? s) 
        (cond ((null? s) #t) 
              ((= (length s) 1) #t)
              ((< (cadr s) (car s)) #f)
              (else (ascending? (cdr s)))))

(define (my-filter pred s) 
        (cond ((null? s) nil)
        ((pred (car s)) (cons (car s) (my-filter pred (cdr s))))
        (else (my-filter pred (cdr s)))))

(define (no-repeats s) 
        (define (cut-repats s)
                (cond ((null? s) nil)
                      (else (begin 
                                   (define (equal? x) (not (= (car s) x)))
                                   (if (= (length s) 1) s (cons (car s) (filter equal? (cdr s))))))))
                
        ;(cut-repats s)   
        (cond ((null? s) nil)
              ((= (length s) 1) s)
              (else (cons (car (cut-repats s)) (no-repeats (cdr (cut-repats s)))))
        )
    )

;(no-repeats '())
; helper function
; returns the values of lst that are bigger than x
; e.g., (larger-values 3 '(1 2 3 4 5 1 2 3 4 5)) --> (4 5 4 5)
(define (larger-values x lst)
        (cond ((null? lst) nil)
        ((< x (car lst)) (cons (car lst) (larger-values x (cdr lst))))
        (else (larger-values x (cdr lst)))
        )
    )
 

(define (longest-increasing-subsequence lst)
  (if (null? lst)
      nil
      (begin (define first (car lst))
             (define rest (cdr lst))
             (define large-values-rest
                     (larger-values first rest))
             (define with-first
                     (cons first (longest-increasing-subsequence large-values-rest)))
             (define without-first
                     (longest-increasing-subsequence rest))
             (if (> (length with-first) (length without-first))
                 with-first
                 without-first))))
            
