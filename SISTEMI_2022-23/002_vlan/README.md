# ESERCIZIO VLAN CON COLLEGAMENTO ACCESS
## OBIETTIVO:
Collegare più pc in vlan con collegamento access port-based

## PROCEDIMENTO:
- Inizialmente abbiamo collegato 4 pc ad uno switch centrale e successivamente abbiamo impostato gli indirizzi ip 192.168.1.10/20/30/40 su ogni relativo pc.
- Dopo ciò abbiamo verificato che ogni pc riuscisse ad inviare i pacchetti ad ogni pc della rete.
- Fatto questo abbiamo impostato le vlan dando il nome e il VID (Robotici:10, Informatici:20) e successivamente impostati sui pc:
    - Robotici -> pc posti in alto rispetto allo switch
    - Informatici -> pc posti in basso rispetto allo switch
- Successivamente abbiamo verifica che ci fosse la corretta comunicazione tra pc delle stess vlan
- Abbiamo poi collegato altri 2 pc a un altro switch che poi abbiamo collegato tramite due cavi Cross-Over per permettere la comunicazione delle due vlan con i pc 