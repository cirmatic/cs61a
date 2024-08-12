(define (cadr lst) (car (cdr lst)))

(define (make-kwlist1 keys values)
        (if (null? keys) nil (cons keys (cons values nil))
        )
)

(define (get-keys-kwlist1 kwlist) 
        (car kwlist)
)

(define (get-values-kwlist1 kwlist)
        (cadr kwlist)
)

(define (make-kwlist2 keys values)
        (if (null? keys) 
            nil 
            (cons (cons (car keys) (cons (car values) nil)) (make-kwlist2 (cdr keys) (cdr values))))  
)



(define (get-keys-kwlist2 kwlist)
        (if (null? kwlist)
            nil
            (cons (car (car kwlist)) (get-keys-kwlist2 (cdr kwlist))))
)



(define (get-values-kwlist2 kwlist)
        (if (null? kwlist)
            nil
            (cons (cadr (car kwlist)) (get-values-kwlist2 (cdr kwlist))))
)

(define (add-to-kwlist kwlist key value)
        (define keys (append (get-keys-kwlist kwlist) (cons key nil)))
        (define values (append (get-values-kwlist kwlist) (cons value nil)))
        (make-kwlist keys values)
) 



(define (get-first-from-kwlist kwlist key)
        (if (null? kwlist)
            nil
            (begin (define keys (get-keys-kwlist kwlist))
                   (define values (get-values-kwlist kwlist))
                   (if (eq? (car keys) key) 
                       (car values)
                       (get-first-from-kwlist (make-kwlist (cdr keys) (cdr values)) key)
                    )
            )
          )
)

;在scheme中，比较两个symbol是否相同时，不可以使用"="，而需要使用eq?函数
;(eq? sym1 sym2)比较两个symbol是否为同一对象，若是，返回#f。注意是比较是否为同一对象而不是是否为同一值
;"="相当于一种数学运算符，只能对数字进行比较
;与eq?类似的还有equal?和eqv?。eqv?可以同时判断数字和符号的相等或等价，equal?可以判断两个表达式是否等值