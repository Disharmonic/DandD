def Race():
    print 'Select a race from the following'
    print 'Dwarf, Elf, Halfling, Human, Dragonborn,'
    print 'Gnome, HalfElf, HalfOrc, Tiefling'
    Dwarf = 'Dwarf'
    Elf = 'Elf'
    Halfling = 'Halfling'
    Human = 'Human'
    Dragonborn = 'Dragonborn'
    Gnome = 'Gnome'
    HalfElf = 'HalfElf'
    HalfOrc = 'HalfOrc'
    Tiefling = 'Tiefling'
    userRace = input('Select your Race: ')
    if userRace == Dwarf:
        print 'Ability score increase. Your constitution increases by 2.'
        print 'Base Walking speed of 25 feet.'
        print 'Darkvision. Can see in dimlight up to 60 ft as if in brightlight'
        print 'Advantage on saving throws against poison'
        print 'Resistance to poison damage'
        print 'Proficiency with battleaxe, handaxe, throwing hammer, and warhammer'
        print 'Proficiency with smith, brewer, or mason tools'
        print 'Double proficiency on int check related to stonework'
    elif userRace == Elf:
        print 'Ability score increase. Your Dexterity increases by 2.'
        print 'Base walking speed of 30 feet.'
        print 'Darkvision. Can see in dimlight up to 60 ft as if in brightlight'
        print 'Proficiency in perception skill'
        print 'Advantage on save vs. Charm'
        print "Magic can't put you to sleep"
        print 'Meditate for 4 hours instead of sleeping for 8 hours'
    elif userRace == Halfling:
        print 'Ability score increase. Your Dexterity increases by 2.'
        print 'Small creature'
        print 'Base walking speed is 25 feet'
        print 'If you roll a 1 on attack you may reroll but must use new roll'
        print 'Advantage on saving throw vs. fear'
        print 'Can move through the space of any creature larger than you'
    elif userRace == Human:
        print 'Ability score increase. All Ability scores increase by 1.'
        print 'Base walking speed of 30 feet'
        print 'Variant: you may increase 2 abilities by 1, New skill, New Feat'
    elif userRace == Dragonborn:
        print 'Your strength increases by 2 and charisma by 1'
        print 'Base walking speed of 30 feet'
        print 'Choose one dragon type and gain breath weapon accordingly'
        print 'Breath weapon(save = 8 + constitution mod) 2d6 damage'
        print 'Breath weapon damage increases 6th, 11th, and 16th lvls'
        print 'Damage resistance based on draconic ancestry'
    elif userRace == Gnome:
        print 'Ability score increase. Your Intelligence increases by 2.'
        print 'Base walking speed of 25 feet'
        print 'Darkvision. Can see in dimlight up to 60 ft as if in brightlight'
        print 'Advantage on Int., Wis., and Cha. vs. magic'
    elif userRace == HalfElf:
        print 'Charisma increase by 2. Two other score increases by 1'
        print 'Base walking of 30 feet'
        print 'Darkvision. Can see in dimlight up to 60 ft as if in brightlight'
        print 'Advantage on saves vs. Charm'
        print 'Cannot be put to sleep by magic'
        print 'Gain proficiency in any 2 skills'
    elif userRace == HalfOrc:
        print 'strength increases by 2. constitution increases by 1'
        print 'Base walking speed of 30 feet'
        print 'Darkvision. Can see in dimlight up to 60 ft as if in brightlight'
        print 'Gain proficiency in intimidation skill'
        print 'If reduced to 0 hp instead of killed outright, reduce to 1 instead'
        print 'On a critical with melee roll additional damage dice, add to roll'
    elif userRace == Tiefling:
        print 'Intelligence increases by 1. Charisma increases by 2'
        print 'Base walking speed of 30 feet'
        print 'Darkvision. Can see in dimlight up to 60 ft as if in brightlight'
        print 'Resistance to fire damage'
        print 'You know Thaumaturgy cantrip'
        print 'At 3rd lvl you can cast Hellish rebuke at 2nd lvl once per day'
        print 'At 5th lvl you can cast Darkness once per day'
        print 'Use Charisma as spellcasting ability'

Race()
