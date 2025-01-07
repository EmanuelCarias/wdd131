  for numero in telefono:
                counter += 1
                print(counter)
                #print(_)
                print(numero)
                while True:
                    try: #//*[@id="phoneNumber"] //input[@id='phoneNumber-0']
                        campo_numero = WebDriverWait(driver, 2).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="phoneNumber"]'))
                        )
                        print("Phone_Field done!")
                        break
                    except Exception as e:
                        print("Bucle")
                        print("The web search_operator is unavailable")
                        Urls(driver)
                        time.sleep(random.randint(2,3))
                        cookiesw(driver)
                        time.sleep(random.randint(2,3))
                        elemento_lo_quiero = driver.find_element(By.XPATH, "//a[@id='cta_configurador_contratar']")
                        time.sleep(1)
                        elemento_lo_quiero.click()
                        time.sleep(random.randint(2,3))
                        cookiesw(driver)
                        time.sleep(random.randint(2,3))
                        print("Clic Done, return!")
                        field_try += 1
                        print("Este es el intento numero",field_try)
                        if field_try == 5:
                            asunto = "No se encuentra el campo phone, Bot 1, "+ str(ip_local)
                            mensaje = f"Web no disponible, Realizando ajustes:\n\n{str(e)}"
                            #enviar_notificacion(asunto, mensaje,correo_user)
                            print('Error')
                            #mostrar_erro()
                            field_try=0
                            driver.quit()
                            print("Este es el intento numero",field_try)
                            #break
                        else:
                            continue
                campo_numero.send_keys(numero)
                time.sleep(random.randint(50,70))  # Esperar tiempo aleatorio
                # Obtener todos los elementos con la clase "feedback-error"
                elementos_error = driver.find_elements(By.CLASS_NAME, "feedback-error")
                campo_operador = driver.find_element(By.XPATH,"//*[@id='operator_input']" )#//*[@id="operator_input"]/"//input[@id='operator-0']"
                # Localizar el input usando su ID
                input_element = driver.find_element(By.ID, "operator_input")

                
                if elementos_error:
                    operador1 = "Digi"  # Establecer el operador como "Digi" cuando se encuentre el mensaje de advertencia
                    campo_numero.clear()
                else:
                    
                    # Obtener el valor del atributo 'value'
                    valor = input_element.get_attribute("value")
                    valor_operador = valor
                    # Imprimir el valor obtenido
                    print(f"El valor del input es: {valor}")
                    #driver.execute_script("arguments[0].value = '';", campo_operador)
                    operador1 = valor_operador
                    campo_numero.clear()
                try:
                    modal = driver.find_element(By.XPATH, '//div[@class="modal-content"]')
                    # Verificar si el modal está visible en la pantalla
                    if modal.is_displayed() and "display: none;" not in modal.get_attribute("style"):
                        Exception_advice(driver,correo_user,ip_local)
                        while True:
                            try:
                                campo_numero = WebDriverWait(driver, 2).until(
                                EC.presence_of_element_located((By.XPATH, '//*[@id="phoneNumber"]'))
                                )
                                print("Phone_Field done!")
                                break
                            except Exception as e:
                                print("Bucle")
                                print("The web search_operator is unavailable")
                                Urls(driver)
                                time.sleep(random.randint(2,3))
                                cookiesw(driver)
                                time.sleep(random.randint(2,3))
                                elemento_lo_quiero = driver.find_element(By.XPATH, "//a[@id='cta_configurador_contratar']")
                                time.sleep(1)
                                elemento_lo_quiero.click()
                                time.sleep(random.randint(2,3))
                                cookiesw(driver)
                                time.sleep(random.randint(2,3))
                                print("Clic Done, return!")
                                field_try += 1
                                print("Este es el intento numero",field_try)
                                if field_try == 5:
                                    asunto = "No se encuentra el campo phone, Bot 1, "+ str(ip_local)
                                    mensaje = f"Web no disponible, Realizando ajustes:\n\n{str(e)}"
                                    #enviar_notificacion(asunto, mensaje,correo_user)
                                    print('Error')
                                    #mostrar_erro()
                                    field_try=0
                                    driver.quit()
                                    print("Este es el intento numero",field_try)
                                    #break
                                else:
                                    continue
                        campo_numero.send_keys(numero)
                        time.sleep(random.randint(5,7))  # Esperar tiempo aleatorio
                        # Obtener todos los elementos con la clase "feedback-error"
                        elementos_error = driver.find_elements(By.CLASS_NAME, "feedback-error")
                        campo_operador = driver.find_element(By.XPATH, '//*[@id="operator_input"]')
                        if elementos_error:
                            operador1 = "Digi"  # Establecer el operador como "Digi" cuando se encuentre el mensaje de advertencia
                            campo_numero.clear()
                        else:
                            valor_operador = campo_operador.get_attribute("value")
                            #driver.execute_script("arguments[0].value = '';", campo_operador)
                            # Obtiene el valor actual del campo
                            #valor_actual = operator_input.get_attribute("value")
                            #print(f"Valor actual: {valor_actual}")
                            # Usa JavaScript para habilitar el campo, limpiar el valor y establecer uno nuevo
                            driver.execute_script("arguments[0].removeAttribute('disabled');", campo_operador)  # Habilitar el campo
                            driver.execute_script("arguments[0].value = '';", campo_operador)  # Limpiar el valor
                            operador1 = valor_operador
                            campo_numero.clear()
                        print(numero, "el operador es:", operador)
                        numeros_con_operador.append((numero, operador))
                        #db_connection(numero,operador)
                        saved_phone(operador,numero)
                        escritor_csv.writerow([numero, operador])
                        operador='sin_operador'
                        #saved_phone(operador,numero)
                        print("Este es el registro numero: ",counter)
                        if counter<0:
                            asunto = "Se requiere atencion URGENTE, Bot 1, "+ str(ip_local)
                            mensaje = f"Espera activa de 5min, Realizar ajustes."
                            #enviar_notificacion(asunto, mensaje,correo_user)
                            counter=0
                            time.sleep(5*1)
                        else:
                            continue
                    else:
                        operador = operador1  # Reemplaza esto con la lógica para obtener el operador
                        print(numero, "el operador es:", operador)
                        numeros_con_operador.append((numero, operador))
                        #db_connection(numero,operador)
                        saved_phone(operador,numero)
                        escritor_csv.writerow([numero, operador])
                        operador='sin_operador'
                        print("Este es el registro numero: ",counter)
                        if counter<0:
                            asunto = "Se requiere atencion URGENTE, Bot 1, "+ str(ip_local)
                            mensaje = f"Espera activa de 5min, Realizar ajustes."
                            #enviar_notificacion(asunto, mensaje,correo_user)
                            counter=0
                            time.sleep(5*1)
                        else:
                            continue
                        continue
                except NoSuchElementException:
                    print("NO HAY")
                    continue