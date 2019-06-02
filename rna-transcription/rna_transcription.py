def to_rna(dna_strand):
    ''' Converts DNA to RNA. '''
    dna_to_rna = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U'
    }

    rna_strand = [dna_to_rna[item] for item in list(dna_strand)]
    return ''.join(rna_strand)
