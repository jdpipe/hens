# Author: Miten Mistry
#         Department of Computing, Imperial College London

from pyomo.core.base.constraint import Constraint

from .index_generators import reclmtd_index, reclmtd_cu_index, reclmtd_hu_index, z_q_index, z_q_cu_index, z_q_hu_index, var_delta_fh_index, var_delta_fhx_index, var_delta_fc_index, var_delta_fcx_index

from .constraint_rules import *

def declare_constraints(model):
    model.z_th_sum = Constraint(model.HP, model.ST, rule=z_th_sum_rule)
    model.th_lower = Constraint(model.HP, model.ST, rule=th_lower_rule)
    model.th_upper = Constraint(model.HP, model.ST, rule=th_upper_rule)

    model.var_delta_fh_sum = Constraint(model.HP, model.CP, model.ST, rule=var_delta_fh_sum_rule)
    model.var_delta_fh_upper = Constraint(var_delta_fh_index, rule=var_delta_fh_upper_rule)

    model.z_thx_sum = Constraint(model.HP, model.CP, model.ST, rule=z_thx_sum_rule)
    model.thx_lower = Constraint(model.HP, model.CP, model.ST, rule=thx_lower_rule)
    model.thx_upper = Constraint(model.HP, model.CP, model.ST, rule=thx_upper_rule)

    model.var_delta_fhx_sum = Constraint(model.HP, model.CP, model.ST, rule=var_delta_fhx_sum_rule)
    model.var_delta_fhx_upper = Constraint(var_delta_fhx_index, rule=var_delta_fhx_upper_rule)

    model.z_tc_sum = Constraint(model.CP, model.ST, rule=z_tc_sum_rule)
    model.tc_lower = Constraint(model.CP, model.ST, rule=tc_lower_rule)
    model.tc_upper = Constraint(model.CP, model.ST, rule=tc_upper_rule)

    model.var_delta_fc_sum = Constraint(model.HP, model.CP, model.ST, rule=var_delta_fc_sum_rule)
    model.var_delta_fc_upper = Constraint(var_delta_fc_index, rule=var_delta_fc_upper_rule)

    model.z_tcx_sum = Constraint(model.HP, model.CP, model.ST, rule=z_tcx_sum_rule)
    model.tcx_lower = Constraint(model.HP, model.CP, model.ST, rule=tcx_lower_rule)
    model.tcx_upper = Constraint(model.HP, model.CP, model.ST, rule=tcx_upper_rule)

    model.var_delta_fcx_sum = Constraint(model.HP, model.CP, model.ST, rule=var_delta_fcx_sum_rule)
    model.var_delta_fcx_upper = Constraint(var_delta_fcx_index, rule=var_delta_fcx_upper_rule)

    # Overall heat balance
    model.overall_heat_balance_hot  = Constraint(model.HP, rule=overall_heat_balance_hot_rule)
    model.overall_heat_balance_cold = Constraint(model.CP, rule=overall_heat_balance_cold_rule)

    model.energy_balance_hot  = Constraint(model.HP, model.ST, rule=energy_balance_hot_rule,  doc="Energy exchanged by hot stream i in stage k" )
    model.energy_balance_cold = Constraint(model.CP, model.ST, rule=energy_balance_cold_rule, doc="Energy exchanged by cold stream j in stage k" )
    model.energy_balance_cu   = Constraint(model.HP,           rule=energy_balance_cu_rule,   doc="Energy exchanged by hot stream i with the cold utility" )
    model.energy_balance_hu   = Constraint(model.CP,           rule=energy_balance_hu_rule,   doc="Energy exchanged by cold stream j with the hot utility" )

    # Inlet temperatures
    model.hot_inlet  = Constraint(model.HP, rule=hot_inlet_rule)
    model.cold_inlet = Constraint(model.CP, rule=cold_inlet_rule)

    # Mass balance
    model.mass_balance_hot  = Constraint(model.HP, model.ST, rule=mass_balance_hot_rule)
    model.mass_balance_cold = Constraint(model.CP, model.ST, rule=mass_balance_cold_rule)

    # Monotonicity
    model.decreasing_hot   = Constraint(model.HP, model.ST, rule=decreasing_hot_rule)
    model.decreasing_cold  = Constraint(model.CP, model.ST, rule=decreasing_cold_rule)
    model.hot_upper_bound  = Constraint(model.HP,           rule=hot_upper_bound_rule)
    model.cold_lower_bound = Constraint(model.CP,           rule=cold_lower_bound_rule)

    # Heat load big M
    model.q_big_m    = Constraint(model.HP, model.CP, model.ST, rule=q_big_m_rule)
    model.q_cu_big_m = Constraint(model.HP, rule=q_cu_big_m_rule)
    model.q_hu_big_m = Constraint(model.CP, rule=q_hu_big_m_rule)

    # Temperature approach big M
    model.temp_app_in  = Constraint(model.HP, model.CP, model.ST, rule=temp_app_in_rule)
    model.temp_app_out = Constraint(model.HP, model.CP, model.ST, rule=temp_app_out_rule)
    model.temp_app_cu  = Constraint(model.HP, rule=temp_app_cu_rule)
    model.temp_app_hu  = Constraint(model.CP, rule=temp_app_hu_rule)

    # Bilinear McCormick bounds
    model.mccor_convex_h_in_1  = Constraint(model.HP, model.CP, model.ST, rule=mccor_convex_h_in_1_rule)
    model.mccor_convex_h_in_2  = Constraint(model.HP, model.CP, model.ST, rule=mccor_convex_h_in_2_rule)
    model.mccor_concave_h_in_1 = Constraint(model.HP, model.CP, model.ST, rule=mccor_concave_h_in_1_rule)
    model.mccor_concave_h_in_2 = Constraint(model.HP, model.CP, model.ST, rule=mccor_concave_h_in_2_rule)

    model.mccor_convex_h_out_1  = Constraint(model.HP, model.CP, model.ST, rule=mccor_convex_h_out_1_rule)
    model.mccor_convex_h_out_2  = Constraint(model.HP, model.CP, model.ST, rule=mccor_convex_h_out_2_rule)
    model.mccor_concave_h_out_1 = Constraint(model.HP, model.CP, model.ST, rule=mccor_concave_h_out_1_rule)
    model.mccor_concave_h_out_2 = Constraint(model.HP, model.CP, model.ST, rule=mccor_concave_h_out_2_rule)

    model.mccor_convex_c_in_1  = Constraint(model.HP, model.CP, model.ST, rule=mccor_convex_c_in_1_rule)
    model.mccor_convex_c_in_2  = Constraint(model.HP, model.CP, model.ST, rule=mccor_convex_c_in_2_rule)
    model.mccor_concave_c_in_1 = Constraint(model.HP, model.CP, model.ST, rule=mccor_concave_c_in_1_rule)
    model.mccor_concave_c_in_2 = Constraint(model.HP, model.CP, model.ST, rule=mccor_concave_c_in_2_rule)

    model.mccor_convex_c_out_1  = Constraint(model.HP, model.CP, model.ST, rule=mccor_convex_c_out_1_rule)
    model.mccor_convex_c_out_2  = Constraint(model.HP, model.CP, model.ST, rule=mccor_convex_c_out_2_rule)
    model.mccor_concave_c_out_1 = Constraint(model.HP, model.CP, model.ST, rule=mccor_concave_c_out_1_rule)
    model.mccor_concave_c_out_2 = Constraint(model.HP, model.CP, model.ST, rule=mccor_concave_c_out_2_rule)

    #Per heat exchanger energy balance
    model.q_energy_bal_hot  = Constraint(model.HP, model.CP, model.ST, rule=q_energy_bal_hot_rule)
    model.q_energy_bal_cold = Constraint(model.HP, model.CP, model.ST, rule=q_energy_bal_cold_rule)

    #Per mixer energy balance
    model.mixer_energy_bal_hot  = Constraint(model.HP, model.ST, rule=mixer_energy_bal_hot_rule)
    model.mixer_energy_bal_cold = Constraint(model.CP, model.ST, rule=mixer_energy_bal_cold_rule)

    model.grad_reclmtd    = Constraint(reclmtd_index, rule=grad_reclmtd_rule)
    model.grad_reclmtd_cu = Constraint(reclmtd_cu_index, rule=grad_reclmtd_cu_rule)
    model.grad_reclmtd_hu = Constraint(reclmtd_hu_index, rule=grad_reclmtd_hu_rule)

    # Area McCormick bounds
    model.z_q_sum = Constraint(model.HP, model.CP, model.ST, rule=z_q_sum_rule)
    model.q_lower = Constraint(model.HP, model.CP, model.ST, rule=q_lower_rule)
    model.q_upper = Constraint(model.HP, model.CP, model.ST, rule=q_upper_rule)
    model.var_delta_reclmtd_sum = Constraint(model.HP, model.CP, model.ST, rule=var_delta_reclmtd_sum_rule)
    model.var_delta_reclmtd_upper = Constraint(z_q_index, rule=var_delta_reclmtd_upper_rule)

    model.area_mccor_convex_1 = Constraint(model.HP, model.CP, model.ST, rule=area_mccor_convex_1_rule)
    model.area_mccor_convex_2 = Constraint(model.HP, model.CP, model.ST, rule=area_mccor_convex_2_rule)
    model.area_mccor_concave_1 = Constraint(model.HP, model.CP, model.ST, rule=area_mccor_concave_1_rule)
    model.area_mccor_concave_2 = Constraint(model.HP, model.CP, model.ST, rule=area_mccor_concave_2_rule)

    model.z_q_cu_sum = Constraint(model.HP, rule=z_q_cu_sum_rule)
    model.q_cu_lower = Constraint(model.HP, rule=q_cu_lower_rule)
    model.q_cu_upper = Constraint(model.HP, rule=q_cu_upper_rule)
    model.var_delta_reclmtd_cu_sum = Constraint(model.HP, rule=var_delta_reclmtd_cu_sum_rule)
    model.var_delta_reclmtd_cu_upper = Constraint(z_q_cu_index, rule=var_delta_reclmtd_cu_upper_rule)

    model.area_cu_mccor_convex_1 = Constraint(model.HP, rule=area_cu_mccor_convex_1_rule)
    model.area_cu_mccor_convex_2 = Constraint(model.HP, rule=area_cu_mccor_convex_2_rule)
    model.area_cu_mccor_concave_1 = Constraint(model.HP, rule=area_cu_mccor_concave_1_rule)
    model.area_cu_mccor_concave_2 = Constraint(model.HP, rule=area_cu_mccor_concave_2_rule)

    model.z_q_hu_sum = Constraint(model.CP, rule=z_q_hu_sum_rule)
    model.q_hu_lower = Constraint(model.CP, rule=q_hu_lower_rule)
    model.q_hu_upper = Constraint(model.CP, rule=q_hu_upper_rule)
    model.var_delta_reclmtd_hu_sum = Constraint(model.CP, rule=var_delta_reclmtd_hu_sum_rule)
    model.var_delta_reclmtd_hu_upper = Constraint(z_q_hu_index, rule=var_delta_reclmtd_hu_upper_rule)

    model.area_hu_mccor_convex_1 = Constraint(model.CP, rule=area_hu_mccor_convex_1_rule)
    model.area_hu_mccor_convex_2 = Constraint(model.CP, rule=area_hu_mccor_convex_2_rule)
    model.area_hu_concave_mccor_1 = Constraint(model.CP, rule=area_hu_mccor_concave_1_rule)
    model.area_hu_concave_mccor_2 = Constraint(model.CP, rule=area_hu_mccor_concave_2_rule)

    model.z_area_beta_sum = Constraint(model.HP, model.CP, model.ST, rule=z_area_beta_sum_rule)
    model.area_low = Constraint(model.HP, model.CP, model.ST, rule=area_low_rule)
    model.area_up = Constraint(model.HP, model.CP, model.ST, rule=area_up_rule)
    model.area_pow_beta = Constraint(model.HP, model.CP, model.ST, rule=area_pow_beta_rule)

    model.z_area_cu_beta_sum = Constraint(model.HP, rule=z_area_cu_beta_sum_rule)
    model.area_cu_low = Constraint(model.HP, rule=area_cu_low_rule)
    model.area_cu_up = Constraint(model.HP, rule=area_cu_up_rule)
    model.area_cu_pow_beta = Constraint(model.HP, rule=area_cu_pow_beta_rule)

    model.z_area_hu_beta_sum = Constraint(model.CP, rule=z_area_hu_beta_sum_rule)
    model.area_hu_low = Constraint(model.CP, rule=area_hu_low_rule)
    model.area_hu_up = Constraint(model.CP, rule=area_hu_up_rule)
    model.area_hu_pow_beta = Constraint(model.CP, rule=area_hu_pow_beta_rule)
