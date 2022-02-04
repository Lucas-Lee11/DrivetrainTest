// EELs :: Eliza Knapp, Ella Krechmer, Lucas Lee
// Softdev
// K27 -- Scheme&JS
// 2022-02-04
// time spent: 1

function fac(n){
    if(n < 0){
        return "Invalid Input";
    }
    else if(n == 0){
        return 1;
    }
    else{
        return n * fac(n-1);
    }
}

function fib(n){
    if(n < 0){
        return "Invalid Input";
    }
    else if(n == 0){
        return 0;
    }
    else if(n == 1){
        return 1;
    }
    else{
        return fib(n-1) + fib(n-2);
    }
}
