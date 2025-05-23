def get_crafting(value):
    if value == "carpentiere":
        return [
            [ # boccetta
                'carbonella', 0.5,
                'sabbia', 1,
            ],
            [ # giara
                'carbonella', 0.25,
                'sabbia', 0.5,
                'slab_legno', 0.5,
            ],
            [ # strip pelle
                'pelle', 1,
            ],
            [ # nave piccola
                'piastra di rame', 1,
                'vela', 1,
                'corda', 2,
                'barche', 2,
            ],
            [ # nave media
                'piastra_ferro', 1,
                'vela', 2,
                'corda', 1,
                'barche_cassa', 3,
            ],
            [ # nave veloce
                'piastra_ferro', 3,
                'vela', 1,
                'corda', 1,
                'barche', 3,
            ]
        ]
    if value == "alchimista":
        return [
            [   # cura t0
                'carbonella', 0.5,
                'boccette', 1,
                'heal cata 0', 0.5,
            ],
            [   # cura t1
                'carbonella', 0.3333,
                'boccette', 1,
                'heal cata 1', 0.3333,
            ],
            [   # cura t2
                'carbonella', 2,
                'boccette', 1,
                'heal cata 2', 1,
            ],
            [   # antidoto
                'carbonella', 1,
                'boccette', 1,
                'brim powder', 1,
                'carne marcia', 1,
            ],
            [   # antidoto t2
                'carbonella', 1,
                'revival star', 0.5,
                'boccette', 0.5,
                'organic resin', 0.5,
            ],
            [   # Mending T0
                'carbonella', 1,
                'core fragment', 1,
                'boccette', 1,
                'brim powder', 1,
            ],
            [   # Mending T1
                'carbonella', 1,
                'core fragment', 1,
                'boccette', 1,
                'organic resin', 1,
                'spider eye', 1,
            ],
            [   # Mending T2
                'carbonella', 2,
                'core fragment', 1,
                'boccette', 1,
                'organic resin', 1,
                'membrane', 1,
            ],
            [   # slowness
                'carbonella', 1,
                'boccette', 1,
                'core fragment', 1,
                'carne marcia', 1,
            ],
            [   # swiftness t1
                'carbonella', 1,
                'boccette', 1,
                'core fragment', 1,
                'zucchero', 1,
            ],
            [   # swiftness t2
                'carbonella', 1,
                'core fragment', 1,
                'blaze powder', 1,
                'item random', 1,
            ],
            [   # slow fall
                'carbonella', 1,
                'boccette', 1,
                'core fragment', 1,
                'piume', 1,
            ],
            [   # jump T1
                'carbonella', 1,
                'boccette', 1,
                'core fragment', 1,
                'rabbit foot', 1,
            ],
            [   # jump t2
                'carbonella', 1,
                'core fragment', 1,
                'blaze powder', 1,
                'item random', 1,
            ],
            [   # weakness
                'carbonella', 1,
                'boccette', 1,
                'core fragment', 1,
            ],
            [   # revify
                'carbonella', 1,
                'boccette', 1,
                'core fragment', 1,
                'revival star', 1,
            ],
            [   # danno
                'carbonella', 1,
                'boccette', 1,
                'core fragment', 1,
                'spider eye', 1,
            ],
            [   # shrink
                'carbonella', 1,
                'boccette', 1,
                'core fragment', 1,
                'fungo marrone', 1,
            ],
            [   # levitation
                'carbonella', 1,
                'boccette', 1,
                'core fragment', 1,
                'ametista', 1,
            ],
            [   # grow
                'carbonella', 1,
                'boccette', 1,
                'core fragment', 1,
                'fungo rosso', 1,
            ],
            [   # poison
                'carbonella', 1,
                'boccette', 1,
                'core fragment', 1,
                'spider eye', 1,
                'fungo marrone', 1,
                'zucchero', 1,
            ],
            [   # invisibility
                'carbonella', 2,
                'boccette', 1,
                'core fragment', 1,
                'antracite', 1,
                'item random', 1,
            ],
            [   # dolphin 
                'carbonella', 2,
                'boccette', 1,
                'core fragment', 1,
            ],
            [   # combustion
                'carbonella', 2,
                'boccette', 1,
                'core fragment', 1,
                'antracite', 1,
            ],
            [   # strength
                'carbonella', 2,
                'boccette', 1,
                'core fragment', 1,
            ],
            [   # impact
                'carbonella', 2,
                'boccette', 1,
                'core fragment', 1,
                'antracite', 1,
                'item random', 1,
            ],
            [   # holy
                'carbonella', 2,
                'boccette', 1,
                'core fragment', 1,
            ],
            [   # fire
                'carbonella', 2,
                'boccette', 1,
                'core fragment', 1,
            ],
            [   # frost
                'carbonella', 2,
                'boccette', 1,
                'core fragment', 1,
            ],
            [   # arcane
                'carbonella', 2,
                'boccette', 1,
                'core fragment', 1,
            ]
        ]