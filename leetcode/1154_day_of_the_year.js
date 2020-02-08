/**
 * @param {string} date
 * @return {number}
 */
var dayOfYear = function (date) {
    //     leap year condition: divisible by 4, divisible by 100 and divisible by 400
    function leap(year) {
        if (year % 400 === 0) return true;
        else if (year % 100 === 0) return false;
        else if (year % 4 === 0) return true;
        else return false;
    }


    a = {
        0: 0, 1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
    }

    date = date.split("-").map((x) => parseInt(x));
    days = 0;
    for (let i = 0; i < date[1]; i++) {
        days += a[i.toString()]
    }

    if (leap(date[0]) && date[1] > 2) days += 1;
    return days + date[2]
};


