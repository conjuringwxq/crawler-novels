var Class = require('./class');
// Class.add('Scott', ['张三', '李四']);


//如果想要将学校这个模块暴露出去
exports.add = function (Classes) {
    Classes.forEach( (item,index) => {
        var _Class = item;
        var teacherName  = item.teacherName;
        var students = item.students;

        Class.add(teacherName, students);
    });
}