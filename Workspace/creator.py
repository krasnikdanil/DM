from pathlib import Path

# твой реальный корень проекта
ROOT = Path(r"C:\Users\Fedor_K\Documents\GitHub\DM\N2P").resolve()

DIRS = [
    "src",
    "src/common",
    "src/natural",
    "src/integer",
    "src/rational",
    "src/polynomial",
    "src/ui_cli",
    "src/ui_desktop",
    "src/ui_desktop/qss",
    "src/ui_desktop/windows",
    "src/ui_desktop/widgets",
    "src/ui_desktop/assets",
    "tests",
    "tests/natural",
    "tests/integer",
    "tests/rational",
    "tests/polynomial",
    "tests/ui_cli",
    "tests/ui_desktop",
    "docs",
    "tools",
]

FILES = [
    "main.py",
    "pyproject.toml",
    "requirements.txt",
    "registry.json",
    ".gitignore",

    "src/__init__.py",
    "src/common/__init__.py",
    "src/common/digits.py",
    "src/common/errors.py",
    "src/common/typing.py",
    "src/common/testing.py",

    "src/natural/__init__.py",
    "src/natural/n1_com_nn_d.py",
    "src/natural/n2_nzer_n_b.py",
    "src/natural/n3_add_1n_n.py",
    "src/natural/n4_add_nn_n.py",
    "src/natural/n5_sub_nn_n.py",
    "src/natural/n6_mul_nd_n.py",
    "src/natural/n7_mul_nk_n.py",
    "src/natural/n8_mul_nn_n.py",
    "src/natural/n9_sub_ndn_n.py",
    "src/natural/n10_div_nn_dk.py",
    "src/natural/n11_div_nn_n.py",
    "src/natural/n12_mod_nn_n.py",
    "src/natural/n13_gcf_nn_n.py",
    "src/natural/n14_lcm_nn_n.py",

    "src/integer/__init__.py",
    "src/integer/z1_abs_z_n.py",
    "src/integer/z2_poz_z_d.py",
    "src/integer/z3_mul_zm_z.py",
    "src/integer/z4_trans_n_z.py",
    "src/integer/z5_trans_z_n.py",
    "src/integer/z6_add_zz_z.py",
    "src/integer/z7_sub_zz_z.py",
    "src/integer/z8_mul_zz_z.py",
    "src/integer/z9_div_zz_z.py",
    "src/integer/z10_mod_zz_z.py",

    "src/rational/__init__.py",
    "src/rational/q1_red_q_q.py",
    "src/rational/q2_int_q_b.py",
    "src/rational/q3_trans_z_q.py",
    "src/rational/q4_trans_q_z.py",
    "src/rational/q5_add_qq_q.py",
    "src/rational/q6_sub_qq_q.py",
    "src/rational/q7_mul_qq_q.py",
    "src/rational/q8_div_qq_q.py",

    "src/polynomial/__init__.py",
    "src/polynomial/base.py",
    "src/polynomial/p1_add_pp_p.py",
    "src/polynomial/p2_sub_pp_p.py",
    "src/polynomial/p3_mul_pq_p.py",
    "src/polynomial/p4_mul_pxk_p.py",
    "src/polynomial/p5_led_p_q.py",
    "src/polynomial/p6_deg_p_n.py",
    "src/polynomial/p7_fac_p_q.py",
    "src/polynomial/p8_mul_pp_p.py",
    "src/polynomial/p9_div_pp_p.py",
    "src/polynomial/p10_mod_pp_p.py",
    "src/polynomial/p11_gcf_pp_p.py",
    "src/polynomial/p12_der_p_p.py",
    "src/polynomial/p13_nmr_p_p.py",

    "src/ui_cli/__init__.py",
    "src/ui_cli/cli.py",
    "src/ui_cli/commands_natural.py",
    "src/ui_cli/commands_integer.py",
    "src/ui_cli/commands_rational.py",
    "src/ui_cli/commands_polynomial.py",
    "src/ui_cli/formatters.py",

    "src/ui_desktop/__init__.py",
    "src/ui_desktop/qt_app.py",
    "src/ui_desktop/resources.qrc",
    "src/ui_desktop/qss/main.qss",
    "src/ui_desktop/windows/__init__.py",
    "src/ui_desktop/windows/main_window.py",
    "src/ui_desktop/windows/natural_window.py",
    "src/ui_desktop/windows/integer_window.py",
    "src/ui_desktop/windows/rational_window.py",
    "src/ui_desktop/windows/polynomial_window.py",
    "src/ui_desktop/windows/about_window.py",
    "src/ui_desktop/widgets/__init__.py",
    "src/ui_desktop/widgets/number_input.py",
    "src/ui_desktop/widgets/poly_input.py",
    "src/ui_desktop/widgets/result_view.py",
    "src/ui_desktop/assets/app.ico",
    "src/ui_desktop/assets/app.png",

    "tests/__init__.py",
    "tests/natural/test_n1_com_nn_d.py",
    "tests/natural/test_n2_nzer_n_b.py",
    "tests/natural/test_n3_add_1n_n.py",
    "tests/natural/test_n4_add_nn_n.py",
    "tests/natural/test_n5_sub_nn_n.py",
    "tests/natural/test_n6_mul_nd_n.py",
    "tests/natural/test_n7_mul_nk_n.py",
    "tests/natural/test_n8_mul_nn_n.py",
    "tests/natural/test_n9_sub_ndn_n.py",
    "tests/natural/test_n10_div_nn_dk.py",
    "tests/natural/test_n11_div_nn_n.py",
    "tests/natural/test_n12_mod_nn_n.py",
    "tests/natural/test_n13_gcf_nn_n.py",
    "tests/natural/test_n14_lcm_nn_n.py",

    "tests/integer/test_z1_abs_z_n.py",
    "tests/integer/test_z2_poz_z_d.py",
    "tests/integer/test_z3_mul_zm_z.py",
    "tests/integer/test_z4_trans_n_z.py",
    "tests/integer/test_z5_trans_z_n.py",
    "tests/integer/test_z6_add_zz_z.py",
    "tests/integer/test_z7_sub_zz_z.py",
    "tests/integer/test_z8_mul_zz_z.py",
    "tests/integer/test_z9_div_zz_z.py",
    "tests/integer/test_z10_mod_zz_z.py",

    "tests/rational/test_q1_red_q_q.py",
    "tests/rational/test_q2_int_q_b.py",
    "tests/rational/test_q3_trans_z_q.py",
    "tests/rational/test_q4_trans_q_z.py",
    "tests/rational/test_q5_add_qq_q.py",
    "tests/rational/test_q6_sub_qq_q.py",
    "tests/rational/test_q7_mul_qq_q.py",
    "tests/rational/test_q8_div_qq_q.py",

    "tests/polynomial/test_p1_add_pp_p.py",
    "tests/polynomial/test_p2_sub_pp_p.py",
    "tests/polynomial/test_p3_mul_pq_p.py",
    "tests/polynomial/test_p4_mul_pxk_p.py",
    "tests/polynomial/test_p5_led_p_q.py",
    "tests/polynomial/test_p6_deg_p_n.py",
    "tests/polynomial/test_p7_fac_p_q.py",
    "tests/polynomial/test_p8_mul_pp_p.py",
    "tests/polynomial/test_p9_div_pp_p.py",
    "tests/polynomial/test_p10_mod_pp_p.py",
    "tests/polynomial/test_p11_gcf_pp_p.py",
    "tests/polynomial/test_p12_der_p_p.py",
    "tests/polynomial/test_p13_nmr_p_p.py",

    "tests/ui_cli/test_cli.py",
    "tests/ui_desktop/test_qt_app.py",

    "docs/modules.md",
    "docs/ui.md",
    "docs/dev.md",
    "docs/formats.md",

    "tools/count_loc.py",
    "tools/check_registry.py",
    "tools/gen_stubs.py",
]


def main() -> None:
    for d in DIRS:
        (ROOT / d).mkdir(parents=True, exist_ok=True)

    for f in FILES:
        path = ROOT / f
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists():
            path.write_text("", encoding="utf-8")

    print(f"Структура создана в {ROOT}")


if __name__ == "__main__":
    main()
