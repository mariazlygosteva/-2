prc = int(input('Введите общую стоимость часов: '))
prc_slvr = 48
prc_gld = int(prc_slvr / 8)
ttl_slvr_prc = 96 * prc_slvr
ttl_gld_prc = prc - ttl_slvr_prc
nmbr_gld = int(ttl_gld_prc / prc_gld)
print(int(nmbr_gld))