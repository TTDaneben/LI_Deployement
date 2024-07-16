"""
Definition of models.
"""

from django.db import models

# Create your models here.

class EnKapitel(models.Model):
    enkap_id = models.IntegerField(db_column='ENKap_ID', blank=True, null=False, primary_key=True)  # This is the ID Field.
    enkap_titel = models.CharField(db_column='ENKap_Titel', blank=True, null=True, max_length=100)  # This is the title Field.
    enkap_kurz = models.TextField(db_column='ENKap_Kurz', blank=True, null=True)  
    enkap_lang = models.TextField(db_column='ENKap_Lang', blank=True, null=True)  
    enkap_oid = models.TextField(db_column='ENKap_OID', blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'EN_Kapitel'
    def __str__(self):
        return self.enkap_titel
    
class EnKode(models.Model):
    en_id = models.TextField(db_column='EN_ID', blank=True, null=False, primary_key=True)  
    en_kap = models.TextField(db_column='EN_Kap', blank=True, null=True)  
    en_child = models.IntegerField(db_column='EN_Child', blank=True, null=True)  
    en_hauptkode = models.TextField(db_column='EN_HauptKode', blank=True, null=True)  
    en_lang = models.TextField(db_column='EN_Lang', blank=True, null=True)  
    en_beschreibung = models.TextField(db_column='EN_Beschreibung', blank=True, null=True)  
    en_c1 = models.TextField(db_column='EN_C1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    en_c2 = models.TextField(db_column='EN_C2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    en_sa = models.TextField(db_column='EN_SA', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    en_q1 = models.TextField(db_column='EN_Q1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    en_q2 = models.TextField(db_column='EN_Q2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    en_l1 = models.TextField(db_column='EN_L1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    en_l2 = models.TextField(db_column='EN_L2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    en_q2abweichend = models.TextField(db_column='EN_Q2abweichend', blank=True, null=True)  
    en_hinweis = models.TextField(db_column='EN_HINWEIS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    en_c1text = models.TextField(db_column='EN_C1Text', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    en_c2text = models.TextField(db_column='EN_C2Text', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    en_q1text = models.TextField(db_column='EN_Q1Text', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    en_q2text = models.TextField(db_column='EN_Q2Text', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    en_c1check = models.TextField(db_column='EN_C1Check', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    en_c2check = models.TextField(db_column='EN_C2Check', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    en_lagetext = models.TextField(db_column='EN_Lagetext', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    en_kat = models.TextField(db_column='EN_Kat', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    en_beispielanzahl = models.TextField(db_column='EN_Beispielanzahl', blank=True, null=True)  
    en_videoanzahl = models.TextField(db_column='EN_Videoanzahl', blank=True, null=True)  
    en_spezial = models.TextField(db_column='EN_Spezial', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    en_kombi = models.TextField(db_column='EN_Kombi', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'EN_Kode'

class EnBeispielkode(models.Model):
    enk_id = models.TextField(db_column='ENK_ID', blank=True, null=False, primary_key = True)  # Field name made lowercase. This field type is a guess.
    enk_enbid = models.TextField(db_column='ENK_ENBID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    enk_kode = models.TextField(db_column='ENK_Kode', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    enk_c1 = models.TextField(db_column='ENK_C1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    enk_c2 = models.TextField(db_column='ENK_C2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    enk_ca = models.TextField(db_column='ENK_CA', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    enk_q1 = models.TextField(db_column='ENK_Q1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    enk_q2 = models.TextField(db_column='ENK_Q2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    enk_v = models.TextField(db_column='ENK_V', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    enk_pos1 = models.TextField(db_column='ENK_Pos1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    enk_pos2 = models.TextField(db_column='ENK_Pos2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    enk_bereich = models.TextField(db_column='ENK_Bereich', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    enk_langtext = models.TextField(db_column='ENK_Langtext', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    enk_anmerkung = models.TextField(db_column='ENK_Anmerkung', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    enk_ok = models.TextField(db_column='ENK_Ok', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'EN_BeispielKode'


class EnBeispiele(models.Model):
    enb_id = models.TextField(db_column='ENB_ID', blank=True, null=False, primary_key= True)  # Field name made lowercase. This field type is a guess.
    enb_enid = models.TextField(db_column='ENB_ENID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    enb_bild = models.TextField(db_column='ENB_Bild', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    enb_druck = models.TextField(db_column='ENB_druck', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    enb_auskleidung = models.TextField(db_column='ENB_Auskleidung', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    enb_reparatur = models.TextField(db_column='ENB_Reparatur', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    enb_punktuell = models.TextField(db_column='ENB_Punktuell', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    enb_typ = models.TextField(db_column='ENB_Typ', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    enb_raus = models.TextField(db_column='ENB_raus', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    enb_pruefung = models.TextField(db_column='ENB_Pruefung', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    enb_bemerkung = models.TextField(db_column='ENB_Bemerkung', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'EN_Beispiele'


class EnC1(models.Model):
    enc1_id = models.TextField(db_column='ENC1_ID', blank=True, null=False, primary_key = True)  # Field name made lowercase. This field type is a guess.
    enc1_child = models.TextField(db_column='ENC1_Child', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    enc1_kurz = models.TextField(db_column='ENC1_Kurz', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    enc1_text = models.TextField(db_column='ENC1_Text', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    enc1_lang = models.TextField(db_column='ENC1_Lang', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    enc1_quantkurz = models.TextField(db_column='ENC1_Quantkurz', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    enc1_quantlang = models.TextField(db_column='ENC1_Quantlang', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    enc1_dim = models.TextField(db_column='ENC1_Dim', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    enc1_c2aus = models.TextField(db_column='ENC1_C2aus', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    enc1_c2nicht = models.TextField(db_column='ENC1_C2Nicht', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    enc1_min = models.TextField(db_column='ENC1_min', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    enc1_max = models.TextField(db_column='ENC1_max', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    enc1_grenz = models.TextField(db_column='ENC1_grenz', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    enc1_stan = models.TextField(db_column='ENC1_stan', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'EN_C1'


# class EnC2(models.Model):
#     enc2_id = models.TextField(db_column='ENC2_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     enc2_child = models.TextField(db_column='ENC2_Child', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     enc2_kurz = models.TextField(db_column='ENC2_Kurz', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     enc2_text = models.TextField(db_column='ENC2_Text', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     enc2_lang = models.TextField(db_column='ENC2_Lang', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     enc2_stan = models.TextField(db_column='ENC2_Stan', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

#     class Meta:
#         managed = False
#         db_table = 'EN_C2'

# class EnQ1(models.Model):
#     enq1_id = models.TextField(db_column='ENQ1_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     enq1_child = models.TextField(db_column='ENQ1_Child', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     enq1_dim = models.TextField(db_column='ENQ1_Dim', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     enq1_lang = models.TextField(db_column='ENQ1_Lang', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     enq1_kurz = models.TextField(db_column='ENQ1_Kurz', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

#     class Meta:
#         managed = False
#         db_table = 'EN_Q1'


# class EnQ2(models.Model):
#     enq2_id = models.TextField(db_column='ENQ2_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     enq2_child = models.TextField(db_column='ENQ2_Child', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     enq2_dim = models.TextField(db_column='ENQ2_DIM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     enq2_lang = models.TextField(db_column='ENQ2_Lang', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     enq2_kurz = models.TextField(db_column='ENQ2_Kurz', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

#     class Meta:
#         managed = False
#         db_table = 'EN_Q2'


# class EnSanierung(models.Model):
#     id = models.TextField(db_column='ID', blank=True, null=False, primary_key=True)  # Field name made lowercase. This field type is a guess.
#     verfahren = models.TextField(db_column='Verfahren', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     kurz = models.TextField(db_column='Kurz', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     lang = models.TextField(db_column='Lang', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     bemerkung = models.TextField(db_column='Bemerkung', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

#     class Meta:
#         managed = False
#         db_table = 'EN_Sanierung'


# class EnStandardanmerkung(models.Model):
#     sa_id = models.TextField(db_column='SA_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_kurz = models.TextField(db_column='SA_Kurz', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_lang = models.TextField(db_column='SA_Lang', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_q1 = models.TextField(db_column='SA_Q1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_q1text = models.TextField(db_column='SA_Q1text', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_q1dim = models.TextField(db_column='SA_Q1Dim', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_verfahren = models.TextField(db_column='SA_Verfahren', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_bemerkung = models.TextField(db_column='SA_Bemerkung', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_aa = models.TextField(db_column='SA_AA', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_ab = models.TextField(db_column='SA_AB', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_ac = models.TextField(db_column='SA_AC', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_ad = models.TextField(db_column='SA_AD', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_ae = models.TextField(db_column='SA_AE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_af = models.TextField(db_column='SA_AF', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_ag = models.TextField(db_column='SA_AG', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_az = models.TextField(db_column='SA_AZ', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_ra = models.TextField(db_column='SA_RA', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_rb = models.TextField(db_column='SA_RB', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_rc = models.TextField(db_column='SA_RC', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_rd = models.TextField(db_column='SA_RD', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_re = models.TextField(db_column='SA_RE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_rf = models.TextField(db_column='SA_RF', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_rg = models.TextField(db_column='SA_RG', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_rh = models.TextField(db_column='SA_RH', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_ri = models.TextField(db_column='SA_RI', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_rj = models.TextField(db_column='SA_RJ', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_rk = models.TextField(db_column='SA_RK', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_rl = models.TextField(db_column='SA_RL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_rm = models.TextField(db_column='SA_RM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_rn = models.TextField(db_column='SA_RN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_rz = models.TextField(db_column='SA_RZ', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_ta = models.TextField(db_column='SA_TA', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_tb = models.TextField(db_column='SA_TB', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_tc = models.TextField(db_column='SA_TC', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_td = models.TextField(db_column='SA_TD', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_te = models.TextField(db_column='SA_TE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_tf = models.TextField(db_column='SA_TF', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_tg = models.TextField(db_column='SA_TG', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_th = models.TextField(db_column='SA_TH', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_ti = models.TextField(db_column='SA_TI', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_tj = models.TextField(db_column='SA_TJ', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_tk = models.TextField(db_column='SA_TK', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_tl = models.TextField(db_column='SA_TL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_tm = models.TextField(db_column='SA_TM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_tn = models.TextField(db_column='SA_TN', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_to = models.TextField(db_column='SA_TO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_tz = models.TextField(db_column='SA_TZ', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_iz = models.TextField(db_column='SA_IZ', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_sa = models.TextField(db_column='SA_SA', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_sb = models.TextField(db_column='SA_SB', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_sc = models.TextField(db_column='SA_SC', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_sd = models.TextField(db_column='SA_SD', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_se = models.TextField(db_column='SA_SE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_sz = models.TextField(db_column='SA_SZ', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_pa = models.TextField(db_column='SA_PA', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_pb = models.TextField(db_column='SA_PB', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_pc = models.TextField(db_column='SA_PC', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_pd = models.TextField(db_column='SA_PD', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_pe = models.TextField(db_column='SA_PE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_pz = models.TextField(db_column='SA_PZ', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_va = models.TextField(db_column='SA_VA', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_vb = models.TextField(db_column='SA_VB', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_vc = models.TextField(db_column='SA_VC', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_vd = models.TextField(db_column='SA_VD', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_ve = models.TextField(db_column='SA_VE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_vf = models.TextField(db_column='SA_VF', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_vg = models.TextField(db_column='SA_VG', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_vh = models.TextField(db_column='SA_VH', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_vz = models.TextField(db_column='SA_VZ', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_bz = models.TextField(db_column='SA_BZ', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     sa_gz = models.TextField(db_column='SA_GZ', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

#     class Meta:
#         managed = False
#         db_table = 'EN_StandardAnmerkung'


# class EnVideobeispiele(models.Model):
#     env_idalt = models.TextField(db_column='ENV_IDalt', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     env_id = models.TextField(db_column='ENV_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     env_enobid = models.TextField(db_column='ENV_ENOBID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     env_video = models.TextField(db_column='ENV_Video', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     env_bild = models.TextField(db_column='ENV_Bild', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     env_typ = models.TextField(db_column='ENV_Typ', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     env_druck = models.TextField(db_column='ENV_Druck', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

#     class Meta:
#         managed = False
#         db_table = 'EN_Videobeispiele'


# class EnVideobeispielekode(models.Model):
#     envb_id = models.TextField(db_column='ENVB_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     envb_envid = models.TextField(db_column='ENVB_ENVID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     envb_kode = models.TextField(db_column='ENVB_Kode', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     envb_c1 = models.TextField(db_column='ENVB_C1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     envb_c2 = models.TextField(db_column='ENVB_C2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     envb_ca = models.TextField(db_column='ENVB_CA', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     envb_q1 = models.TextField(db_column='ENVB_Q1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     envb_q2 = models.TextField(db_column='ENVB_Q2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     envb_v = models.TextField(db_column='ENVB_V', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     envb_pos1 = models.TextField(db_column='ENVB_Pos1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     envb_pos2 = models.TextField(db_column='ENVB_Pos2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     envb_bereich = models.TextField(db_column='ENVB_Bereich', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     envb_langtext = models.TextField(db_column='ENVB_Langtext', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     envb_anmerkung = models.TextField(db_column='ENVB_Anmerkung', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     envb_ok = models.TextField(db_column='ENVB_OK', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

#     class Meta:
#         managed = False
#         db_table = 'EN_Videobeispielekode'
