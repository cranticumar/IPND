var work = {
    "jobs": [
        {
            "employer": "Qualcomm INDIA Private Limited",
            "title": "Senior Lead Engineer",
            "location": "Hyderabad, INDIA",
            "dates": "May 2014 - Till Date",
            "description": "Camera Test Lead, CASE Framework Developer (Python/Django)"
        },
        {
            "employer": "Qualcomm INDIA Private Limited",
            "title": "Senior Engineer",
            "location": "Hyderabad, INDIA",
            "dates": "May 2012 - April 2014",
            "description": "CASE Framework Developer, WFD Test Lead, Concurrency Test Lead, Camera IQPP Developer (Matlab), Video Quality Test Development"
        },
        {
            "employer": "Qualcomm INDIA Private Limited",
            "title": "Engineer",
            "location": "Hyderabad, INDIA",
            "dates": "March 2010 - April 2012",
            "description": "Concurrency Test Engineer, Camera IQPP Developer (Matlab) and Camera Test Engineer"
        },
        {
            "employer": "Qualcomm INDIA Private Limited",
            "title": "Project Engineer",
            "location": "Hyderabad, INDIA",
            "dates": "July 2007 - February 2010",
            "description": "System Level Testing of Windows Mobile"
        }
    ]
};

var projects = {
    "projects": [
        {
            "title": "Camera IQ and Functional Test",
            "dates": "Aug 2014 - Till Date",
            "description": "Camera IQ testing and Functional testing lead, managing products and resources for test planning, test execution and test reporting"
        },
        {
            "title": "Camera IQ Development",
            "dates": "Oct 2015 - Till Date",
            "description": "Camera IQ tools development, developing algorithms"
        },
        {
            "title": "CASE Development",
            "dates": "Aug 2013 - Dec 2014",
            "description": "CASE Web Framework development used for Test Management, Reporting and Test Execution Manager, based on Python/Django"
        },
        {
            "title": "WFD Functional Test and Certification",
            "dates": "May 2012 - Aug 2014",
            "description": "Miracast Functional test planning, execution and reporting, Certification of products for Mircast"
        },
        {
            "title": "Video Quality Development",
            "dates": "Oct 2012 - Dec 2013",
            "description": "Video Quality Test Suite development using NI PQA"
        },
        {
            "title": "Concurrrency Test Lead",
            "dates": "May 2011 - May 2013",
            "description": "Concurrency Functional Functional test planning, execution and reporting"
        },
        {
            "title": "Camera IQ Development",
            "dates": "June 2011 - Mar 2014",
            "description": "Camera IQ tools development, developing algorithms"
        },
        {
            "title": "Camera Test Engineer",
            "dates": "Mar 2010 - Nov 2011",
            "description": "Camera Test Execution for various products"
        }
    ]
};

var bio = {
    "name": "Kranthi Kumar",
    "role": "Senior Lead Engineer - SDET",
    "welcomemessage": "Welcome",
    "contacts": {
        "mobile": 9618253216,
        "email": "cranticumar@yahoo.com",
        "github": "cranticumar",
        "twitter": "cranticumar",
        "location": "Hyderabad"
    }
};

var education = {
    "schools" : [
        {
            "name": "Velammal Engineering College",
            "location": "Chennai, INDIA",
            "majors": ["Electronics", "Instrumentation"],
            "dates": "2003-2007"
        },
        {
            "name": "Pardha Junior College and Narayana Junior College",
            "location": "Nellore, INDIA",
            "majors": ["Maths", "Physics", "Chemistry"],
            "dates": "2011-2013"
        },
        {
            "name": "Veda Vyasa E.M School and Ratnam E.M School",
            "location": "Nellore, INDIA",
            "majors": "I-X",
            "dates": "2011"
        }
    ],
    "onlinecourses": [
        {
            "title": "Introduction to Programming Nanodegree",
            "school": "Udacity",
            "dates" : 2015
        },
        {
            "title": "Python Programming for Everybody",
            "school": "Coursera",
            "dates": 2015
        }
    ]
};

function loopList(arr) {
    for (var key in arr) {
        if (arr[key].constructor == Array) {
            loopList(arr[key]);
        } else if (arr[key].constructor == Object) {
            loopObject(arr[key]);
        } else {
            $('#header').append(arr[key]);
            $('#header').append('<br>');
        }
    }
}

function loopObject(obj) {
    for (var key in obj) {
        if (obj[key].constructor == Array) {
            $('#header').append(key[0].toUpperCase() + key.slice(1).toLowerCase());
            $('#header').append(' : ');
            $('#header').append('<br>');
            loopList(obj[key]);
        } else if (obj[key].constructor == Object) {
            $('#header').append(key[0].toUpperCase() + key.slice(1).toLowerCase());
            $('#header').append(' : ');
            $('#header').append('<br>');
            loopObject(obj[key])
        } else {
            $('#header').append(key[0].toUpperCase() + key.slice(1).toLowerCase());
            $('#header').append(' : ');
            $('#header').append(obj[key]);
            $('#header').append('<br>');
        }
    }
    $('#header').append('<br>');
}

loopObject(bio);
$('#header').append('<hr>');
loopObject(education);
$('#header').append('<hr>');
loopObject(work);
$('#header').append('<hr>');
loopObject(projects);