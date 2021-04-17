

const value: string[] = ['****', '**', '***', '*']
var daily: string[] = value.sort(
        (a,b) => a < b ? -1 : a > b ? 1 : 0
)
var coding: number = daily[2].lastIndexOf("*")
var habit: string = daily[1].repeat(coding)
console.log(habit)



// ****