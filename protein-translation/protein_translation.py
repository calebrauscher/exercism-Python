def proteins(strand):
    ''' Returns a list of amino acids based on RNA sequence. '''

    PROTEINS = {
        'AUG': 'Methionine',
        'UUU': 'Phenylalanine',
        'UUC': 'Phenylalanine',
        'UUA': 'Leucine',
        'UUG': 'Leucine',
        'UCU': 'Serine',
        'UCC': 'Serine',
        'UCA': 'Serine',
        'UCG': 'Serine',
        'UAU': 'Tyrosine',
        'UAC': 'Tyrosine',
        'UGU': 'Cysteine',
        'UGC': 'Cysteine',
        'UGG': 'Tryptophan',
        'UAA': 'STOP',
        'UAG': 'STOP',
        'UGA': 'STOP'
    }
    codons = [strand[i:i+3] for i in range(0, len(strand), 3)]

    amino_acids = []
    for codon in codons:
        if PROTEINS[codon] == 'STOP':
            break
        if PROTEINS[codon] not in amino_acids:
            amino_acids.append(PROTEINS[codon])
    return amino_acids
