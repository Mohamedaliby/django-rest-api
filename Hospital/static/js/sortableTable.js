$(document).ready(function () {
    var table = $('#sortableTable').DataTable();
    $('.dataTables_length').addClass('bs-select');

   //  const elem = $('#workIdInput');
   //
   //  // Save current value of element
   // elem.data('oldVal', elem.val());
   //
   // // Look for changes in the value
   // elem.bind("propertychange change click keyup input paste", function(event){
   //    // If value has changed...
   //    if (elem.data('oldVal') !== elem.val()) {
   //        // Updated stored value
   //        elem.data('oldVal', elem.val());
   //
   //        // $('#workIdCol')
   //        var filteredData = $('#sortableTable').DataTable().columns( 0 ).data().forEach(function (element) {
   //            element.filter(function (values, index) {
   //                // alert('search for ' + elem.val());
   //                console.log(index + ': ' + values);
   //                return !!values.includes(elem.val());
   //            });
   //        });
   //    }
   // });


    /* Custom filtering function which will search data in column four between two values */
    var tableSearch = $.fn.dataTable.ext.search;
    tableSearch.push(function( settings, data, dataIndex ) {
            // use data for the workId column
            return data[0].toUpperCase().includes($('#workIdFilterField').val().toUpperCase())
        }
    );
    tableSearch.push(function( settings, data, dataIndex ) {
            // use data for the workId column
            return data[1].toUpperCase().includes($('#nameFilterField').val().toUpperCase())
        }
    );
    tableSearch.push(function( settings, data, dataIndex ) {
            // use data for the workId column
            return data[2].toUpperCase().includes($('#instituteFilterField').val().toUpperCase())
        }
    );
    tableSearch.push(function( settings, data, dataIndex ) {
            // use data for the workId column
            return data[3].toUpperCase().includes($('#nationalIdFilterField').val().toUpperCase())
        }
    );

    $(document).ready(function() {
        // Event listener to the two range filtering inputs to redraw on input
        $('#workIdFilterField').keyup( function() {table.draw();} );
        $('#nameFilterField').keyup( function() {table.draw();} );
        $('#instituteFilterField').keyup( function() {table.draw();} );
        $('#nationalIdFilterField').keyup( function() {table.draw();} );
    } );

});

