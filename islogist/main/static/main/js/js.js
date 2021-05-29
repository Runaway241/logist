$(document).ready(function () {
    $('#table_id').DataTable({
        "language": {

            "decimal": "",
            "emptyTable": "Нет записей в таблице",
            "info": "Показано _END_ из _TOTAL_ записей",
            "infoEmpty": "Нет записей",
            "infoFiltered": "(filtered from _MAX_ total entries)",
            "infoPostFix": "",
            "thousands": ",",
            "lengthMenu": "Показано _MENU_ записей",
            "loadingRecords": "Loading...",
            "processing": "Processing...",
            "search": "Поиск:",
            "zeroRecords": "Записи не найдены",
            "paginate": {
                "next": 'Следующая страница',
                'previous': 'Предыдущая страница',
            }
        }
    });
});