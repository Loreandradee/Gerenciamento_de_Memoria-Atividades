package FifoJava;
import java.util.*;
public class FIFOPageReplacement {

	    public static void main(String[] args) {

	        Scanner scanner = new Scanner(System.in);
	        
	        // Leitura do número de frames
	        System.out.print("Número de frames: ");
	        int numFrames = scanner.nextInt();
	        scanner.nextLine(); // Consumir o newline
	        
	        // Leitura da sequência de referências
	        System.out.print("Sequência de referências (separadas por vírgula): ");
	        String input = scanner.nextLine();
	       
	        // Parse da sequência sem Streams 
	        List<Integer> references = new ArrayList<>();
	        String[] parts = input.split(",");
	        for (String part : parts) {
	            try {
	                references.add(Integer.parseInt(part.trim()));
	            } catch (NumberFormatException e) {
	                System.out.println("Erro: Entrada inválida na sequência. Use apenas números separados por vírgula.");
	                return;
	            }
	        }
	        // Estruturas para simulação
	        Queue<Integer> frames = new LinkedList<>(); // guarda as páginas que estão na memória
	        Set<Integer> present = new HashSet<>(); // verifica rapidamente se uma página já está na memória
	        int pageFaults = 0; //conta quantas vezes uma página não foi encontrada
	        
	        // Simulação do algoritmo FIFO
	        for (int page : references) {
	            boolean isFault = !present.contains(page);
	            Integer removed = null;
	            if (isFault) {
	                pageFaults++;
	                if (frames.size() == numFrames) {
	                    // Substituir a página mais antiga
	                    removed = frames.poll();
	                    present.remove(removed);
	                }
	                // Adicionar a nova página
	                frames.add(page);
	                present.add(page);
	            }
	            // Exibir o estado após cada referência
	            System.out.print("Referência: " + page + " | Frames: " + frames.toString() + " | ");
	            if (isFault) {
	                if (removed != null) {
	                    System.out.print("Page Fault (substituiu " + removed + ")");
	                } else {
	                    System.out.print("Page Fault");
	                }
	            } else {
	                System.out.print("Page Hit");
	            }
	            System.out.println(" | Total Faults: " + pageFaults);
	        }
	        // Estatísticas finais
	        int totalReferences = references.size();
	        System.out.println("\nNúmero total de faltas de página: " + pageFaults);
	        System.out.println("Taxa de faltas de página: " + (double) pageFaults / totalReferences);
	    }
	}


