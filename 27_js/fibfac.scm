;;EELs :: Eliza Knapp, Ella Krechmer, Lucas Lee
;;Softdev
;;K27 -- Scheme&JS
;;2022-02-04
;;time spent: 1


(define (fac n)
    (if (< n 0)
        "Invalid Input"
        (if (= n 0)
            1
            (* n (fac (- n 1)))
        )
    )
)

(define (fib n)
    (if (< n 0)
        "Invalid Input"
        (if (= n 0)
            0
            (if (= n 1)
                1
                (+ (fib (- n 1)) (fib (- n 2)))
            )
        )
    )
)


(fac 5)
(fib 6)

(fac -1)
(fib 0)
