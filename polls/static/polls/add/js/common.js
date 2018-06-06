$(document).ready(function () {
    $("#addCandidate").on("click", loadAddCandidateDiv);
});

function loadAddCandidateDiv()
{
    $.get('/static' + location.pathname +'/partials/candidateFields.txt', function(data) {
        $(".candidateContainer").append(data);
     }, 'text');
}