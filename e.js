let main = function () {
    let a = 3.6
    let b = -3.2
    let t = 0
    if (a > b) {
        t = a
        a = b
        b = t
    }
    a
}

main()
