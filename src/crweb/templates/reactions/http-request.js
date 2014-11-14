<script type="text/javascript">
  $(document).ready(function() {
    $('select#request_type').on("change", function(e){
        var postBodyGroup = $('.form-group#post-body');
        if($(this).val() == "post") {
            postBodyGroup.show();
        } else {
            postBodyGroup.hide();
        }
    });

  });

</script>
