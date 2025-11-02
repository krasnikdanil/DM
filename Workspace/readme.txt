Общая суть: разбить проект на мелкие модули для более удобного контроля за версиями и написанием кода. 
Принцип работы: 
1) Ядро: в папках common, natural, integer, rational и polynomial лежит работа арифметики, каждая функция в своём файле (прим. "ADD_NN_N", "LCM_NN_N" и тд (см. документ Коллоквиум ДМ))
2) Интерфейсы: за основу интерфейса отвечает PySide6 (ui_desktop), опенсорс аналог Qt. Выводит главное окно, окна по разделам, виджеты ввод/вывод. На всякий случай будет аналог в папке ui_cli, если нужно будет быро прогнать модули через тесты
3) Тут уделю внимание точке входа, оно же main.py. Хочется внедрить запуск с аргументами и без. Без аргументов будет запускаться GUI версия, с аргументом --cli - консольная соответственно.
4) Реестр: Отдельный док registry.json, там будут перечислены учебные модули, файлы, авторы модулей. .json формат выбран для более удобного формирования статистики и окно О программе. 



Структура проекта: 
dm-cas/
  main.py
  pyproject.toml
  requirements.txt
  registry.json
  .gitignore

  src/
    __init__.py

    common/
      __init__.py
      digits.py
      errors.py
      typing.py
      testing.py

    natural/
      __init__.py
      n1_com_nn_d.py
      n2_nzer_n_b.py
      n3_add_1n_n.py
      n4_add_nn_n.py
      n5_sub_nn_n.py
      n6_mul_nd_n.py
      n7_mul_nk_n.py
      n8_mul_nn_n.py
      n9_sub_ndn_n.py
      n10_div_nn_dk.py
      n11_div_nn_n.py
      n12_mod_nn_n.py
      n13_gcf_nn_n.py
      n14_lcm_nn_n.py

    integer/
      __init__.py
      z1_abs_z_n.py
      z2_poz_z_d.py
      z3_mul_zm_z.py
      z4_trans_n_z.py
      z5_trans_z_n.py
      z6_add_zz_z.py
      z7_sub_zz_z.py
      z8_mul_zz_z.py
      z9_div_zz_z.py
      z10_mod_zz_z.py

    rational/
      __init__.py
      q1_red_q_q.py
      q2_int_q_b.py
      q3_trans_z_q.py
      q4_trans_q_z.py
      q5_add_qq_q.py
      q6_sub_qq_q.py
      q7_mul_qq_q.py
      q8_div_qq_q.py

    polynomial/
      __init__.py
      base.py
      p1_add_pp_p.py
      p2_sub_pp_p.py
      p3_mul_pq_p.py
      p4_mul_pxk_p.py
      p5_led_p_q.py
      p6_deg_p_n.py
      p7_fac_p_q.py
      p8_mul_pp_p.py
      p9_div_pp_p.py
      p10_mod_pp_p.py
      p11_gcf_pp_p.py
      p12_der_p_p.py
      p13_nmr_p_p.py

    ui_cli/
      __init__.py
      cli.py
      commands_natural.py
      commands_integer.py
      commands_rational.py
      commands_polynomial.py
      formatters.py

    ui_desktop/
      __init__.py
      qt_app.py
      resources.qrc
      qss/
        main.qss
      windows/
        __init__.py
        main_window.py
        natural_window.py
        integer_window.py
        rational_window.py
        polynomial_window.py
        about_window.py
      widgets/
        __init__.py
        number_input.py
        poly_input.py
        result_view.py
      assets/
        app.ico
        app.png

  tests/
    __init__.py
    natural/
      test_n1_com_nn_d.py
      test_n2_nzer_n_b.py
      test_n3_add_1n_n.py
      test_n4_add_nn_n.py
      test_n5_sub_nn_n.py
      test_n6_mul_nd_n.py
      test_n7_mul_nk_n.py
      test_n8_mul_nn_n.py
      test_n9_sub_ndn_n.py
      test_n10_div_nn_dk.py
      test_n11_div_nn_n.py
      test_n12_mod_nn_n.py
      test_n13_gcf_nn_n.py
      test_n14_lcm_nn_n.py
    integer/
      test_z1_abs_z_n.py
      test_z2_poz_z_d.py
      test_z3_mul_zm_z.py
      test_z4_trans_n_z.py
      test_z5_trans_z_n.py
      test_z6_add_zz_z.py
      test_z7_sub_zz_z.py
      test_z8_mul_zz_z.py
      test_z9_div_zz_z.py
      test_z10_mod_zz_z.py
    rational/
      test_q1_red_q_q.py
      test_q2_int_q_b.py
      test_q3_trans_z_q.py
      test_q4_trans_q_z.py
      test_q5_add_qq_q.py
      test_q6_sub_qq_q.py
      test_q7_mul_qq_q.py
      test_q8_div_qq_q.py
    polynomial/
      test_p1_add_pp_p.py
      test_p2_sub_pp_p.py
      test_p3_mul_pq_p.py
      test_p4_mul_pxk_p.py
      test_p5_led_p_q.py
      test_p6_deg_p_n.py
      test_p7_fac_p_q.py
      test_p8_mul_pp_p.py
      test_p9_div_pp_p.py
      test_p10_mod_pp_p.py
      test_p11_gcf_pp_p.py
      test_p12_der_p_p.py
      test_p13_nmr_p_p.py
    ui_cli/
      test_cli.py
    ui_desktop/
      test_qt_app.py

  docs/
    modules.md
    ui.md
    dev.md
    formats.md

  tools/
    count_loc.py
    check_registry.py
    gen_stubs.py



Немного архитектуры каталогов: 
src/
  common/        # общее: ошибки, типы, заглушки
  natural/       # N-1...N-14
  integer/       # Z-1...Z-10
  rational/      # Q-1...Q-8
  polynomial/    # P-1...P-13
  ui_cli/        # консоль
  ui_desktop/    # PySide6 GUI
docs/            # форматы, описание модулей
tests/           # pytest-автотесты
tools/           # служебные скрипты

