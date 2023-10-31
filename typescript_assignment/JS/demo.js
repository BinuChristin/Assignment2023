"use strict";
// "use strict";
// class Astronaut {
//     constructor(massKg, name) {
//         this.massKg = massKg;
//         this.name = name;
//     }
// }
// class Cargo {
//     constructor(massKg, material) {
//         this.massKg = massKg;
//         this.material = material;
//     }
// }
// class Rocket {
//     constructor(name, totalCapacityKg) {
//         this.cargoItems = [];
//         this.astronauts = [];
//         this.name = name;
//         this.totalCapacityKg = totalCapacityKg;
//     }
//     sumMass(items) {
//         return items.reduce((totalMass, item) => totalMass + item.massKg, 0);
//     }
//     currentMassKg() {
//         const cargoMass = this.sumMass(this.cargoItems);
//         const astronautMass = this.sumMass(this.astronauts);
//         return cargoMass + astronautMass;
//     }
//     canAdd(item) {
//         return this.currentMassKg() + item.massKg <= this.totalCapacityKg;
//     }
//     addCargo(cargo) {
//         if (this.canAdd(cargo)) {
//             this.cargoItems.push(cargo);
//             return true;
//         }
//         return false;
//     }
//     addAstronaut(astronaut) {
//         if (this.canAdd(astronaut)) {
//             this.astronauts.push(astronaut);
//             return true;
//         }
//         return false;
//     }
// }
// Define the Astronaut class
class Astronaut {
    constructor(massKg, name) {
        this.massKg = massKg;
        this.name = name;
    }
}
// Define the Cargo class
class Cargo {
    constructor(massKg, material) {
        this.massKg = massKg;
        this.material = material;
    }
}
// Define the Rocket class
class Rocket {
    constructor(name, totalCapacityKg) {
        this.cargoItems = [];
        this.astronauts = [];
        this.name = name;
        this.totalCapacityKg = totalCapacityKg;
    }
    // Method to calculate the sum of mass of items
    sumMass(items) {
        return items.reduce((acc, item) => acc + item.massKg, 0);
    }
    // Method to calculate the current total mass of cargo and astronauts
    currentMassKg() {
        return this.sumMass(this.cargoItems) + this.sumMass(this.astronauts);
    }
    // Method to check if an item can be added to the rocket
    canAdd(item) {
        return this.currentMassKg() + item.massKg <= this.totalCapacityKg;
    }
    // Method to add cargo to the rocket
    addCargo(cargo) {
        if (this.canAdd(cargo)) {
            this.cargoItems.push(cargo);
            return true;
        }
        else {
            return false;
        }
    }
    // Method to add an astronaut to the rocket
    addAstronaut(astronaut) {
        if (this.canAdd(astronaut)) {
            this.astronauts.push(astronaut);
            return true;
        }
        else {
            return false;
        }
    }
}
// Example usage
const astro1 = new Astronaut(80, "Alice");
const cargo1 = new Cargo(500, "Food Supplies");
const rocket = new Rocket("Saturn V", 10000);
console.log("Astronaut added ", rocket.addAstronaut(astro1)); // true (Astronaut can be added)
console.log("Cargo added ", rocket.addCargo(cargo1)); // true (Cargo can be added)
