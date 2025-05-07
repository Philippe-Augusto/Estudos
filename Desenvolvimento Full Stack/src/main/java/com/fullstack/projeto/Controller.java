package com.fullstack.projeto;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/api/calendarios")
public class Controller {

    @Autowired
    private CalendarioRepository calendarioRepository;

    @GetMapping
    public List<Calendario> listarTodos() {
        return calendarioRepository.findAll();
    }

    @GetMapping("/{id}")
    public ResponseEntity<Calendario> buscarPorId(@PathVariable Long id) {
        Optional<Calendario> calendario = calendarioRepository.findById(id);
        return calendario.map(ResponseEntity::ok).orElseGet(() -> ResponseEntity.notFound().build());
    }

    @PostMapping
    public Calendario criar(@RequestBody Calendario calendario) {
        return calendarioRepository.save(calendario);
    }

    @PutMapping("/{id}")
    public ResponseEntity<Calendario> atualizar(@PathVariable Long id, @RequestBody Calendario calendarioAtualizado) {
        Optional<Calendario> calendarioExistente = calendarioRepository.findById(id);
        if (calendarioExistente.isPresent()) {
            calendarioAtualizado.setId(id);
            return ResponseEntity.ok(calendarioRepository.save(calendarioAtualizado));
        }
        return ResponseEntity.notFound().build();
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deletar(@PathVariable Long id) {
        if (calendarioRepository.existsById(id)) {
            calendarioRepository.deleteById(id);
            return ResponseEntity.noContent().build();
        }
        return ResponseEntity.notFound().build();
    }

    @GetMapping("/welcome")
    public String welcome() {
        return "Welcome to Spring Boot";
    }
}