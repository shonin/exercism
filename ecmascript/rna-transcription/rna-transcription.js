export default class Transcriptor {
    constructor() {
        this.nucleotideMap = {
            G: 'C',
            C: 'G',
            A: 'U',
            T: 'A'
        };
    }

    toRna(dna) {
        let rna = '';
        [...dna].map( nucleotide => {
            this.isValid(nucleotide);
            rna += this.nucleotideMap[nucleotide];
        });
        return rna;
    }

    isValid(nucleotide) {
        if (!this.nucleotideMap[nucleotide]) throw new Error("Invalid input DNA.");
    }
}
