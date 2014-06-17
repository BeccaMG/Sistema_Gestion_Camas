for x in range(10, 33):
    print '''{
        \"model\": \"app_camas.Habitacion\",
        \"pk\": %d,
        \"fields\": {
        \"numero\": \"3%d\",
        \"tipo\": \"H\"
    }
  },''' % (x+39,x)