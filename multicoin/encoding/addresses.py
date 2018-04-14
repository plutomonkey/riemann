import multicoin
from ..tx import tx_builder as tb


def make_sh_address(script_string, witness=False):
    script_bytes = tb.make_sh_output_script(script_string, witness)
    if witness:
        return multicoin.network.SEGWIT_ENCODER.encode(script_bytes)
    return multicoin.network.LEGACY_ENCODER.encode(script_bytes)


def make_p2wsh_address(script_string):
    return make_sh_address(script_string, witness=True)


def make_p2sh_address(script_string):
    return make_sh_address(script_string, witness=False)


def make_pkh_address(pubkey, witness=False):
    script_bytes = tb.make_pkh_output_script(pubkey)
    if witness:
        return multicoin.network.SEGWIT_ENCODER.encode(script_bytes)
    return multicoin.network.LEGACY_ENCODER.encode(script_bytes)


def make_p2wpkh_address(pubkey):
    return make_pkh_address(pubkey, witness=True)


def make_p2pkh_address(pubkey):
    return make_pkh_address(pubkey, witness=False)