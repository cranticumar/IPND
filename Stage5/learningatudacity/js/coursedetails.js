function toggleCourse(js_on) {
    parsed_json = JSON.parse(js_on);
    $('#course').empty();
    $('#course').prepend('<hr />');
    publish = ["title", "expected_duration", "homepage", "level", "short_summary", "teaser_video"];
    console.log(parsed_json);
    for (var prop in publish) {
        if (parsed_json.hasOwnProperty(publish[prop])) {
            $('#course').append('<b>' + publish[prop][0].toUpperCase() + publish[prop].slice(1).toLowerCase().replace(/_/g, ' ') + ' : </b>');
            if (['homepage', 'teaser_video'].indexOf(publish[prop]) > -1) {
                if (parsed_json[publish[prop]].hasOwnProperty('youtube_url')) {
                    if (parsed_json[publish[prop]].youtube_url != "") {
                        $('#course').append('<a href=' + parsed_json[publish[prop]].youtube_url + '>' + parsed_json[publish[prop]].youtube_url + '</a>');
                    } else {
                        $('#course').append('None');
                    }
                } else {
                    $('#course').append('<a href=' + parsed_json[publish[prop]] + '>' + parsed_json[publish[prop]] + '</a>');
                }
                
            } else if (publish[prop] === 'expected_duration') {
                $('#course').append(parsed_json[publish[prop]] + ' ' + parsed_json[publish[prop] + '_unit']);
            } else {
                $('#course').append(parsed_json[publish[prop]]);
            }
            $('#course').append('<br>');
        }
    }
}