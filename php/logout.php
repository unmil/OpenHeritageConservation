<?php
 session_start();
    session_unset();
    session_destroy();
    session_write_close();

echo "<script>location.href='index.html';</script>";
?>
