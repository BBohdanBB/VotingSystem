

function cloneMore() {
    selector = 'fieldset:last';
    type = 'candidate_set';
    var newElement = $(selector).clone(true);
    var total = $('#id_' + type + '-TOTAL_FORMS').val();
    newElement.find(':input').each(function() {
        var name = $(this).attr('name').replace('-' + (total-1) + '-','-' + total + '-');
        var id = 'id_' + name;
        $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
    });
    newElement.find('label').each(function() {
        var newFor = $(this).attr('for').replace('-' + (total-1) + '-','-' + total + '-');
        $(this).attr('for', newFor);
    });

    $('#id_' + type + '-TOTAL_FORMS').val(total);
    $(selector).after(newElement);
    var str = '<input type="hidden" name="candidate_set-'+total+'-postId" id="id_candidate_set-'+total+'-postId" /> <input type="hidden" name="candidate_set-'+total+'-id" id="id_candidate_set-'+total+'-id" />';
    $(selector).after($(str));
    total++;
}