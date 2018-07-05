var student = require('./student');
var teacher = require('./teacher');



function add (teacherName, students){
    teacher.add(teacherName);

    students.forEach( (item, index) => {
        student.add(item)
    })
}
exports.add = add;//如果想要让你的模块成为传统的模块实例
//module.exports = add;//如果想要让你的模块成为特别的对象类型