export default class Hamming {
    compute(dna_one, dna_two) {
        if (dna_one.length !== dna_two.length) {
            throw new Error("DNA strands must be of equal length.")
        }
        return dna_one
            .split('')
            .filter( (nucleic_acid, index) =>
                nucleic_acid != dna_two[index]
            ).length;
    }

};
