let students = [
    {name: 'Remy', cohort: 'Jan'},
    {name: 'Genevieve', cohort: 'March'},
    {name: 'Chuck', cohort: 'Jan'},
    {name: 'Osmund', cohort: 'June'},
    {name: 'Nikki', cohort: 'June'},
    {name: 'Boris', cohort: 'June'}
];

let users = {
    employees: [
        {'first_name':  'Miguel', 'last_name' : 'Jones'},
        {'first_name' : 'Ernie', 'last_name' : 'Bertson'},
        {'first_name' : 'Nora', 'last_name' : 'Lu'},
        {'first_name' : 'Sally', 'last_name' : 'Barkyoumb'}
    ],
    managers: [
       {'first_name' : 'Lillian', 'last_name' : 'Chambers'},
       {'first_name' : 'Gordon', 'last_name' : 'Poe'}
    ]
};

function display(students){
  for (var i=0;i<students.length;i++){
    console.log(`Name: ${students[i].name}, Cohort: ${students[i].cohort}`)
  }
}

function expose(users){
  for (i=0;i<users.employees.length;i++){
    var current = users.employees[i];
    console.log(`${i+1}: ${current.first_name} ${current.last_name}, ${current.first_name.length + current.last_name.length}` )
  }
  for (i=0;i<users.managers.length;i++){
    var current = users.managers[i];
    console.log(`${i+1}: ${current.first_name} ${current.last_name}, ${current.first_name.length + current.last_name.length}` )

  }
}

display(students)
expose(users)