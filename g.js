let main = function () {
    let year = 2050
    let leap = false
    if (year % 4 == 0) {
        if (year % 100 == 0) {
            if (year % 400 == 0) {
                leap = true
            } else {
                leap = false
            }
        } else {
            leap = true
        }
    } else {
        leap = false
    }
    leap
}

main()
