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

// const rocket = new Rocket("Falcon 9", 2000);
// const astronaut1 = new Astronaut(80, "John");
// const cargo1 = new Cargo(500, "Satellite");
// const astronaut2 = new Astronaut(70, "Alice");
// const cargo2 = new Cargo(1800, "Satellite");
// console.log("Rocket can add astronaut 1:", rocket.addAstronaut(astronaut1));
// console.log("Rocket can add cargo 1:", rocket.addCargo(cargo1));
// console.log("Rocket can add astronaut 2:", rocket.addAstronaut(astronaut2));
// console.log("Rocket can add cargo 2:", rocket.addCargo(cargo2));
// console.log("Rocket current mass:", rocket.currentMassKg());



// Define the Payload interface
interface Payload {
    massKg: number;
  }
  
  // Define the Astronaut class
  class Astronaut implements Payload {
    constructor(public massKg: number, public name: string) {}
  }
  
  // Define the Cargo class
  class Cargo implements Payload {
    constructor(public massKg: number, public material: string) {}
  }
  
  // Define the Rocket class
  class Rocket {
    name: string;
    totalCapacityKg: number;
    cargoItems: Cargo[] = [];
    astronauts: Astronaut[] = [];
  
    constructor(name: string, totalCapacityKg: number) {
      this.name = name;
      this.totalCapacityKg = totalCapacityKg;
    }
  
    // Method to calculate the sum of mass of items
    sumMass(items: Payload[]): number {
      return items.reduce((acc, item) => acc + item.massKg, 0);
    }
  
    // Method to calculate the current total mass of cargo and astronauts
    currentMassKg(): number {
      return this.sumMass(this.cargoItems) + this.sumMass(this.astronauts);
    }
  
    // Method to check if an item can be added to the rocket
    canAdd(item: Payload): boolean {
      return this.currentMassKg() + item.massKg <= this.totalCapacityKg;
    }
  
    // Method to add cargo to the rocket
    addCargo(cargo: Cargo): boolean {
      if (this.canAdd(cargo)) {
        this.cargoItems.push(cargo);
        return true;
      } else {
        return false;
      }
    }
  
    // Method to add an astronaut to the rocket
    addAstronaut(astronaut: Astronaut): boolean {
      if (this.canAdd(astronaut)) {
        this.astronauts.push(astronaut);
        return true;
      } else {
        return false;
      }
    }
  }
  
  // Example usage
  const astro1 = new Astronaut(80, "Alice");
  const cargo1 = new Cargo(500, "Food Supplies");
  const rocket = new Rocket("Saturn V", 10000);
  
  console.log("Astronaut added ",rocket.addAstronaut(astro1)); // true (Astronaut can be added)
  console.log("Cargo added ",rocket.addCargo(cargo1));     // true (Cargo can be added)

  